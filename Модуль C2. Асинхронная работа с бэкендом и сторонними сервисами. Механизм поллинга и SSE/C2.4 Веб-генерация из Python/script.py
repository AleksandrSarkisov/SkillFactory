import time
import bottle

@bottle.route('/words')
def number_generator():
    bottle.response.content_type = "text/event-stream"
    bottle.response.cache_control = "no-cache"
    bottle.response.headers["Access-Control-Allow-Origin"] = "*"

    words = ["one","two","three","four","five","six","seven"]
    for word in words:
        yield "data {}.\n\n".format(word)
        time.sleep(2)


if __name__ == "__main__":
    bottle.run(server='gunicorn')
