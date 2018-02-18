import random
import string
import os
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


config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    },
    '/assets': {
        'tools.staticdir.root': os.path.dirname(os.path.abspath(__file__)),
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'assets',
    }
}

if __name__ == '__main__':
    configfile = os.path.join(os.path.dirname(__file__), "server.conf")
    cherrypy.quickstart(Generator(), config = config)
