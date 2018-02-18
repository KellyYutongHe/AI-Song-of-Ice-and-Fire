import random
import string
import os.path
import cherrypy
import mc


class Generator(object):
    @cherrypy.expose
    def index(self):
        return open("index.html")

    @cherrypy.expose
    def generate(self, length = 3):
        return mc.test(length)

    @cherrypy.expose
    def example(self):
        return open("example.html")


if __name__ == '__main__':
    configfile = os.path.join(os.path.dirname(__file__), "server.conf")
    cherrypy.quickstart(Generator(), config = configfile)
