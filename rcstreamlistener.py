# rcstreamlistener.py
import urllib3.contrib.pyopenssl
import logging
from socketIO_client import SocketIO, BaseNamespace

urllib3.contrib.pyopenssl.inject_into_urllib3()
#logging.basicConfig(level=logging.DEBUG)

class MainNamespace(BaseNamespace):
    def on_change(self, change): 
        if change['namespace'] == 3:
            strippedTitle = change['title'].lstrip('User talk:')
            print 'Page: ' + strippedTitle

    def on_connect(self):
        self.emit('subscribe', 'en.wikipedia.org')

socketIO = SocketIO('https://stream.wikimedia.org')
socketIO.define(MainNamespace, '/rc')

socketIO.wait()
