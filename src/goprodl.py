'''
Created on Jun 10, 2013

@author: Benjamin Hill
'''

import urllib2
from bs4 import BeautifulSoup
import urlparse
import shutil
import re, os

base_url = "http://10.5.5.9:8080/DCIM/DCIM/100GOPRO/"
content = urllib2.urlopen(base_url).read()
soup = BeautifulSoup(content)

media_re = re.compile(r'(jpg|jpeg|mp4)$', re.IGNORECASE)
home_image_dir = os.path.join(os.path.expanduser("~"),'Pictures', 'gopro')
print home_image_dir

try:
    os.makedirs(home_image_dir)
    print "Created:",home_image_dir
except (OSError):
    print 'Already exists:',home_image_dir

for a in soup.findAll('a', attrs={'href': media_re}):
    print "Found the URL:", a['href']
    req = urllib2.urlopen(urlparse.urljoin(base_url, a['href']))
    file_name = os.path.join(home_image_dir, a['href'].split('/')[-1])
    if(os.path.isfile(file_name)):
        print 'Already exists:',file_name
    else:
        print "Downloading to:", file_name
        with open(file_name, 'wb') as fp:
            shutil.copyfileobj(req, fp)




