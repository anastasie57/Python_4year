## -*- coding: utf-8 -*-

import urllib.request
import xml.etree.ElementTree as ET

def load_dump():
	lang = input('Input here language of needed Wikipedia dump: ')
	url = "https://dumps.wikimedia.org/" + lang + "wiki/latest/" + lang + "wiki-latest-pages-articles.xml.bz2"

	urllib.request.urlretrieve(url, lang + 'wiki-latest-pages-articles.xml.bz2')

	return "Database is successfully downloaded."

def find_articles():
	lang = input('Input here language of needed Wikipedia dump: ')
	filename = lang + 'wiki-latest-pages-articles.xml'
	articles = open('article_names.txt', "w")
	articles_list = []
	
	tree = ET.parse(filename)
	root = tree.getroot()

	for child in root:
		if child.tag[-4:] == "page":
			page_tag = child
			for child in page_tag:
				if child.tag[-5:] == "title":
					articles_list.append(child.text)

	for title in sorted(articles_list):
		try:
			articles.write(title + '\r\n')
		except:
			pass

	return "List of articles is ready."

print(load_dump())

print(find_articles())