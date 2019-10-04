import os

path = 'Модуль B3. Классы и контексты\\B3.13 Домашнее задание\\'
workspace = os.path.join(os.getcwd(),path)

class HTML(object):
    def __init__(self, output=None):
        if output:
            self.file = open(workspace+output, 'w')
        else:
            open(workspace+'test.html', 'r').close()
            self.file = open(workspace+'test.html', 'a')
        self.children = []

    def __enter__(self):
        return self

    def __iadd__(self, other):
        self.children.append(other)
        return self

    def compileStartTag(self):
        startTag = "<html>\n"
        return startTag

    def compileEndTag(self):
        endTag = ''
        for child in self.children:
            if child:
                endTag += child.compile()
        endTag +='</html>'
        return endTag

    def compile(self):
        return self.compileStartTag()+self.compileEndTag()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write(self.compile())
        self.file.close()

class TopLevelTag(object):
    def __init__(self, *args, **kwargs):
        self.tag = args[0]
        self.attributes = {key: value for key, value in zip(kwargs.keys(), kwargs.values()) if key != "text"}
        self.children = []

    def __enter__(self):
        return self

    def __iadd__(self, other):
        self.children.append(other)
        return self

    def __radd__(self, other):
        other.children.add(self)
        return self

    def compileStartTag(self):
        startTag = "<"+self.tag
        for attr in self.attributes.items():
            if attr[0] == "klass":
                startTag +=' class=="'+' '.join(attr[1])+'"'
            else:
                startTag +=' '+str(attr[0]) + '="'+str(attr[1])+'"'
        startTag += '>'
        return startTag

    def compileEndTag(self):
        endTag = ''
        for child in self.children:
            endTag += '\t'+child.compile()+"\n"
        endTag +='</'+self.tag+'>'
        return endTag

    def compile(self):
        return self.compileStartTag()+self.compileEndTag()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.compile()

    def __str__(self):
        return self.compile()

class Tag(object):
    def __init__(self, *args, **kwargs):
        self.tag = args[0]
        self.attributes = {key: value for key, value in zip(kwargs.keys(), kwargs.values()) if key != "text"}
        self.children = []

    def __enter__(self):
        return self

    def __getattr__(self, name):
        return None

    def compileStartTag(self):
        startTag = "\n<"+self.tag
        for attr in self.attributes.items():
            if attr[0] == "klass":
                startTag +=' class=="'+' '.join(attr[1])+'"'
            else:
                startTag +=' '+str(attr[0]) + '="'+str(attr[1])+'"'
        startTag += '>'
        return startTag

    def compileEndTag(self):
        endTag = ''
        for child in self.children:
            endTag += '\t'+child.compile()+"\n"
        if self.text:
            endTag += self.text+'</'+self.tag+'>'
        else:
            endTag +='</'+self.tag+'>\n'
        return endTag

    def compile(self):
        return self.compileStartTag()+self.compileEndTag()

    def __str__(self):
        return self.compile()

    def __iadd__(self, other):
        self.children.append(other)
        return self

    def __radd__(self, other):
        other.children.add(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.compile()


def main():
    with HTML(output="test.html") as doc:
        with TopLevelTag("head") as head:
            with Tag("title") as title:
                title.text = "hello"
                head += title
            doc += head

        with TopLevelTag("body") as body:
            with Tag("h1", klass=("main-text",)) as h1:
                h1.text = "Test"
                body += h1

            with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
                with Tag("p", klass=("klass","id")) as paragraph:
                    paragraph.text = "another test"
                    div += paragraph

                with Tag("img", is_single=True, src="/icon.png", data_image="responsive") as img:
                    div += img
                body += div
            doc += body

if __name__=="__main__":
    main()
