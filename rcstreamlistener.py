# rcstreamlistener.py
import urllib3.contrib.pyopenssl
import logging
from ipaddress import ip_address
from socketIO_client import SocketIO, BaseNamespace
import templateadder

urllib3.contrib.pyopenssl.inject_into_urllib3()
logging.basicConfig(level=logging.WARNING)

class MainNamespace(BaseNamespace):
    def on_change(self, change): 
        if change['namespace'] == 3:
            strippedTitle = change['title'].lstrip('User talk:')
            try:
                ip_address(strippedTitle)
            except ValueError:
                pass
            else:
                print ''

    def on_connect(self):
        self.emit('subscribe', 'en.wikipedia.org')
        print 'Connected.'

print 'Connecting...'
socketIO = SocketIO('https://stream.wikimedia.org')
socketIO.define(MainNamespace, '/rc')

socketIO.wait()
