# -*- coding: utf-8 -*-
# filename: main.py
import web
import threading
import thread
from handle import Handle
from main_train import predict

urls = (
    '/wx', 'Handle',
)

def app_start():
    app = web.application(urls, globals())
    app.run()

if __name__ == '__main__':
    threads = []
    t1 = threading.Thread(target=app_start)
    threads.append(t1)
    t2 = threading.Thread(target=predict)
    threads.append(t2)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
