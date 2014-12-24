import os
from ParseTable import parseTable
from itertools import chain
def directoryToChangesList(directoryName):
	files=[f for f in os.listdir(directoryName) if os.path.isfile(
		os.path.join(directoryName,f))]
	results = [parseTable(os.path.join(directoryName,f)) for f in files]
	final=[item for sublist in results for item in sublist]
	return final
def changesListTofile(changesList,newFileName):
	pass
if __name__ == "__main__":
	pass