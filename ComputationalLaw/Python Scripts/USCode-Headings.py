"""
Licensed under Creative Commons: Attribution 4.0 International (CC BY 4.0)
http://creativecommons.org/licenses/by/4.0/
"""
import xml.etree.ElementTree as ET
import requests
import os
import re

titleList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
sumCounter = 0

for uniqueTitleNumber in titleList:
    tempURL = str("%02d" % uniqueTitleNumber)
    URL = 'https://raw.github.com/HumanDynamics/FreeLaw/master/USLM-US-Code/usc'+tempURL+'.xml'
    r = requests.get(URL)
    text = r.text.encode('utf-8')

    tree = ET.ElementTree(ET.fromstring(text))

    namespace = ".//{http://xml.house.gov/schemas/uslm/1.0}"

    title = tree.find(namespace + "title")
    titleNum = title.find(namespace + "num").attrib["value"]
    print "Title",titleNum
    print title.find(namespace + "heading").text

    chapterList = tree.findall(namespace + "chapter")
    counter = 0

    def getText(section):
        output = ""
        if section.tag == ("{http://xml.house.gov/schemas/uslm/1.0}section"):            
                title = section.find(namespace + "heading")
                sectionNum = section.find(namespace + "num").attrib["value"]
                #sectionNumTemp = sectionNum.encode('utf8')
                output += title.text + "\tTitle:"+titleNum+"\tChapter:"+chapterNum+"\tSection:"+sectionNum+"\n"
        return output
    def compareString(str1,str2):
        if len(str1)<len(str2):
            return True
        else:
            return str1<str2

    chaptersFound = []
    
    for chapter in chapterList:
        counter += 1
        output = ""
        chapterNum = chapter.find(namespace + "num").attrib["value"]
        chapterNumTemp = chapterNum.encode('utf8') #To bypass the encoding error
        if chapterNum not in chaptersFound:
            if len(chaptersFound) > 0 and compareString(chaptersFound[-1],chapterNum):
                chaptersFound.append(chapterNum)
            elif len(chaptersFound) == 0:
                chaptersFound.append(chapterNum)
            else:
                continue
        else:
            continue
        chapterHeading = chapter.find(namespace + "heading").text
        output += chapterHeading.rstrip() + "\tTitle:"+titleNum.rstrip()+"\tChapter:"+chapterNum+"\tSection:0\n"
        
        for child in chapter:
            if child.tag == ("{http://xml.house.gov/schemas/uslm/1.0}subchapter"):
                for section in child:
                    output += getText(section)
            output += getText(child)
        fileName = "USCodeHeadings/Title"+str("%02d"%int(titleNum))+"-"+str(chapterNumTemp)+".txt"
        f = open(fileName, 'w')
        f.write(output.encode('utf8'))
        f.close()
    print "Number of Chapters:",len(chaptersFound) #Chapters in each Title
    sumCounter += len(chaptersFound)
    
print sumCounter #Total Chapters in all of US Code
