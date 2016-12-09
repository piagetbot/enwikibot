# rcstreamlistener.py
import urllib3.contrib.pyopenssl
import logging
from ipaddress import ip_address
from socketIO_client import SocketIO, BaseNamespace

urllib3.contrib.pyopenssl.inject_into_urllib3()
logging.basicConfig(level=logging.WARNING)

class MainNamespace(BaseNamespace):
    def on_change(self, change): 
        if change['namespace'] == 3:
            strippedTitle = change['title'].lstrip('User talk:')
            try:
                ipAddressObject = ip_address(strippedTitle)
                print 'True'
            except ValueError:
                print 'False'

    def on_connect(self):
        self.emit('subscribe', 'en.wikipedia.org')
        print 'Connected.'

print 'Connecting...'
socketIO = SocketIO('https://stream.wikimedia.org')
socketIO.define(MainNamespace, '/rc')

socketIO.wait()
