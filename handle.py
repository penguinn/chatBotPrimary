# -*- coding: utf-8 -*-
# filename: handle.py
import hashlib
import reply
import receive
import web
import threading
eventEngine = threading.Event()
eventHandle = threading.Event()
question = ""
answer = ""


class Handle(object):
    def POST(self):
        global eventEngine, eventHandle, question, answer
        try:
            eventEngine.set()
            webData = web.data()
            #print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    print recMsg.Content
                    question = recMsg.Content
                    eventEngine.set()
                    eventHandle.wait()
                    eventHandle.clear()
                    content = answer.strip()
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            return Argment