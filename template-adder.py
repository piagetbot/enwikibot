from wikitools import *
import re

site = wiki.Wiki()
site.login('username', 'password') #For later

def getWarningLevel(user=None, content=None):
  params = {'action':'query',
            'prop':'revisions',
            'titles':user,
            'rvdir':'newer',
            'rvprop':'content'
  }
  req = api.APIRequest(site, params)
  content = req.query(False)

#In main() later, it would be:
#if '<!-- Template:uw-\D*2 -->' in content:
# continue
#Or similar
