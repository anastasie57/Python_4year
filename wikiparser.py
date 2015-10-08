# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import re

filename = input('Input here filename: ')

csvfile = open('wiki_csv.csv', 'w')
xmlfile = open(filename, 'r')

PAGE = re.compile('<page>.+?</page>', flags=re.U)
TITLE = re.compile('<title>.+?</title>', flags=re.U)
LINK = re.compile('[[.+?]]', flags=re.U)


def read_xml(xmlfile):
    for page in PAGE.findall(xmlfile.read()):
        yield page

for page in read_xml(xmlfile):
    title = TITLE.search(page)[0]
    links = LINK.findall(page)
    csvfile.write(';'.join([title, len(links)]) + ';')
