function jQuery(selector, context = document){
  this.elements = Array.from(context.querySelectorAll(selector));
  return this
}

jQuery.prototype.each = function (fn){
	this.elements.forEach((element, index) => fn.call(element, element, index));
	return this;
}

jQuery.prototype.click = function(fn){
  this.each(element => element.addEventListener('click', fn))
  return this
}

jQuery.prototype.remove = function(){
  this.each(element => element.remove())
  return this;
}

jQuery.prototype.hide = function(){
  this.each(element => element.style.display('hide'))
  return this;
}

jQuery.prototype.show = function(){
  this.each(element => element.style.display(''))
  return this;
}

jQuery.prototype.class = function(name){
  this.each(element => element.className = name)
  return this;
}

jQuery.prototype.html = function(context=null){

  if (context){
    this.each(element => element.innerHTML = context)
    return this
  }else {
    html = []
    this.each(element => html.push(element.innerHTML)+'\n')
    return html.join('')
  }
}

jQuery.prototype.text = function(context=null){
  if (context){
    this.each(element => element.innerText = context)
    return this
  } else{
    text = []
    this.each(element => text.push(element.innerText))
    return text.join(' ')
  }
}

const $ = (e) => new jQuery(e);

/*Раскомментируй строки для Задания 1*/

/*$('button').click(function(e){
  console.log($('h1').html())
  $('div').html("<p>Тэг p в в блоках div</p>")
})*/

/*Раскомментируй строки для Задания 2*/

/*$('button').click(function(e){
  console.log($('h1').text())
  $('h1').text("Замена текста")
})
*/
