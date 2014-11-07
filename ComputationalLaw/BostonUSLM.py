"""
Licensed under Creative Commons: Attribution 4.0 International (CC BY 4.0)
http://creativecommons.org/licenses/by/4.0/
"""

import xml.etree.ElementTree as ET
import requests
import os
import re

TEST_URL = 'https://raw.github.com/HumanDynamics/FreeLaw/master/ExperimentsAndExamples/USCode-03.xml'
URL = 'https://raw.github.com/HumanDynamics/FreeLaw/master/USLM%20US%20Code/usc02_test.xml'
r = requests.get(URL)
text = r.text.encode('utf-8')
##text = text.lower()
##splitText = text.split('\n')

tree = ET.ElementTree(ET.fromstring(text))

namespace = ".//{http://xml.house.gov/schemas/uslm/1.0}"


ids = ["id3cd25b8f-2e14-11e4-9af5-e14406bc0d92","id3cd25b93-2e14-11e4-9af5-e14406bc0d92","id3cd4ccb5-2e14-11e4-9af5-e14406bc0d92"]

section = tree.findall(namespace + "section")
##for elt in tree.getiterator():
for sec in section:
    if sec.attrib.get('id','-1') in ids:
        title = sec.find(namespace + "heading")
        para = sec.find(namespace + "p")
        sourceCredit = sec.find(namespace+ "sourceCredit")
        print "\n" + title.text
        print para.text
        print sourceCredit.text



        
##attributes = section.attrib
##sectionID = attributes.get('id',-1)
##if sectionID == "id3cc1ba5c-2e14-11e4-9af5-e14406bc0d92":
##    print "Found the Title"

#[m.start() for m in re.finditer('test', 'test test test test')]  -> Find multiple occurences of a substring

#Number of times the word President is repeated in Title 3
##presidentList = [m.start() for m in re.finditer('president', text)]
##print len(presidentList)

        
##tagAndAttributes = []
##tempBoth  = []
##count = 0
##for elt in tree.getiterator():
##    temp = elt.tag
##    tempAttribute = elt.attrib
##    tempBoth += [(temp,tempAttribute)]
##    count += 1
##    if count > 5:
##        break
##for i in tempBoth:
##    print i
##print tempBoth[0][1]['identifier']
