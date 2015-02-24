"""web main"""

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, authenticated
from xml.etree import ElementTree
import time
import hashlib
import json
#from rockps.auth import AuthHandler


class MainHandler(RequestHandler):
    a=1
    t1="""<xml>
<ToUserName><![CDATA[{0}]]></ToUserName>
<FromUserName><![CDATA[{1}]]></FromUserName>
<CreateTime>{2}</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[{3}]]></Content>
</xml>""";
    #wowDictStr="""{"stsm":"斯坦索姆","dk":"死亡骑士"}"""
    #wowDict=json.loads(MainHandler.wowDictStr,encoding="UTF-8")
    f=open(r"wowDict.json","rb")
    wows=f.read().decode()
    wowDict=json.loads(wows)
    f.close()
    def get(self):   
        signature=self.get_argument("signature")
        timestamp=self.get_argument("timestamp")
        nonce=self.get_argument("nonce")
        echostr =self.get_argument("echostr")
        #signature=self.request.query_arguments.signature
        #timestamp=self.request.query_arguments.timestamp
        #nonce=self.request.query_arguments.nonce
        #echostr=self.request.query_arguments.echostr
        token="testweixin"
        #字典排序
        tmpArr=[token,timestamp,nonce]
        tmpArr.sort()
        tmpStr = "%s%s%s" % tuple(tmpArr)
        tmpStr = hashlib.sha1(tmpStr.encode())#获得签名后字节码再签名
        hashcode=tmpStr.hexdigest()
        #sha1加密算法
        if hashcode==signature:
            self.write(echostr)
    def post(self):
        xml=self.request.body.decode();
        root = ElementTree.fromstring(xml)
        content=root.find("Content").text
        msgType=root.find("MsgType").text
        fromUser=root.find("FromUserName").text
        toUser=root.find("ToUserName").text
        msgID=root.find("MsgId").text
        print(xml)
        self.set_header ('Content-Type', 'text/xml; charset=UTF-8')
        k=content.upper()
        if k in MainHandler.wowDict.keys():
            content="war3百科全书:\n%s:%s"%(k,MainHandler.wowDict[k])
        self.write(MainHandler.t1.format(fromUser,toUser,int(time.time()),content))
class JsHandler(RequestHandler):
    def get(self,fileName):
        self.render(fileName+".js");
    def post(self,fileName):
        self.render(fileName+".js");
class WeixinHandler(RequestHandler):
    def get(self):
        self.render("weixintest.html");
settings = {
}

application = Application([
    (r"/", MainHandler),
    (r"/([^?]+).js",JsHandler),
    (r"/weixin",WeixinHandler)
], **settings)


if __name__ == "__main__":
    http_server = HTTPServer(application)
    http_server.listen(8089)
    IOLoop.instance().start()
    print("webServer 已启动")
