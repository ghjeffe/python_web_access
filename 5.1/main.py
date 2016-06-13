#!/usr/local/bin/python3

from urllib import request

import xml.etree.ElementTree as et


file = request.urlopen('http://python-data.dr-chuck.net/comments_275575.xml').read()
root = et.fromstring(file)
print(sum([int(item.text) for item in root.findall('comments/comment/count')]))
