"""web main"""

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, authenticated
from xml.etree import ElementTree
import urllib.parse
import time
from os import path
import sys
#from rockps.auth import AuthHandler


class MainHandler(RequestHandler):
    def get(self):
        #print("%d" %time.time())
        #print(self.request.body)
        self.set_header('Content-Type', 'text/html; charset=UTF-8')
        #self.write("""ä¸æµ·""");
        self.render(path.join(DDIR,"public","templates","index.html"),title="Tornodo版我爱学");
class JsHandler(RequestHandler):
    def get(self,filename,arg1):
        #qpath=self.request.path
        #print(os.path.join(os.path.dirname(os.getcwd()),"public",filename))
        #os.chdir("目标路径")  切换当前工作目录到目标路径
        self.render(path.join(DDIR,"public",filename))
settings = {
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "xsrf_cookies": True,
}
application = Application([
    (r"/", MainHandler),
    (r"/(.+\.(js|css))",JsHandler),
], **settings)


if __name__ == "__main__":
    #global DDIR
    #DDIR = sys.path[0]
    ##对py2exe打包程序进行处理
    #if os.path.isfile(DDIR):
    #    DDIR,filen = os.path.split(DDIR)
    #DDIR=os.path.dirname(DDIR)
    global DDIR
    DDIR=path.dirname(path.dirname(__file__))
    http_server = HTTPServer(application)
    http_server.listen(8089)
    IOLoop.instance().start()