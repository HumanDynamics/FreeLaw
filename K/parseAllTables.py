import os
from ParseTable import parseTable
from itertools import chain
def directoryToChangesList(directoryName):
	files=[f for f in os.listdir(directoryName) if os.path.isfile(
		os.path.join(directoryName,f))]
	results = [parseTable(os.path.join(directoryName,f)) for f in files]
	final=[item for sublist in results for item in sublist]
	return final
def titleMods(changesList):
	#Sorts the changesList by title
	#Translates title into section for each entry.
	#reports summary statistics for different entries.
	#Structure
	#changesList[change][0] = Section
	#changesList[change][1] = Statue Page
	#changesList[change][2] = USCodeTitle
	#changesList[change][3] = USCodeSection
	#changesList[change][4] = USCodeStatus
	from collections import defaultdict
	d = defaultdict(int)
	for change in changeList:
		d[change[2]] +=1
	return d
def changesListTofile(changesList,newFileName):
	pass
if __name__ == "__main__":
	pass