#!/usr/bin/python2.7

import urllib
import urllib2
import json
import os

agent = "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"
url = "https://www.hopperapp.com/include/files-api.php?request=releases&public=true"

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', agent)]
page = opener.open(url)

data = json.load(page)
link = data["Ubuntu / Mint"]["filename"]
filename = link.split("/")[-1]
currentPath = os.path.dirname(os.path.realpath(__file__))
destPath = os.path.join(currentPath, filename)

# Only if it doesn't exist
if not os.path.isfile(destPath):
    print("Removing old file(s)")
    for file in os.listdir(currentPath):
        if file.endswith(".deb"):
            os.remove(os.path.join(currentPath, file))

    print("Downloading " + link + " --> " + destPath)
    urllib.urlretrieve(link, destPath)

else:
    print("File already exists, exiting")
