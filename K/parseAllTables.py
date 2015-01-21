#!/usr/bin/python
import os
from ParseTable import parseTable

titleDict = {
    1: "General Provisions",2: "The Congress",3: "The President",
    4: "Flag and Seal, Seat of Government, and the States",
    5: "Government Organization and Employees",6: "Domestic Security",
    7: "Agriculture", 8: "Aliens and Nationality", 9: "Arbitration",
    10:"Armed Forces", 11:"Bankruptcy", 12:"Banks and Banking",13:"Census",
    14:"Coast Guard", 15:"Commerce and Trade", 16:"Conservation", 
    17:"Copyrights",18:"Crimes and Criminal Procedure", 19:"Customs Duties",
    20:"Education",21:"Food and Drugs", 
    22:"Foreign Relations and Intercourse",23:"Highways",
    24:"Hospitals and Asylums", 25:"Indians",26:"Internal Revenue Code",
    27:"Intoxicating Liquors",28:"Judiciary and Judicial Procedure",
    29:"Labor",30:"Mineral Lands and Mining",31:"Money and Finance",
    32:"National Guard",33:"Navigation and Navigable Waters",
    34:"Navy(discontinued in 1956)",35:"Patents",
    36:"Patriotic and national observances, ceremonies, and organizations.",
    37:"Pay and Allowances of the Uniformed Services",
    38:"Veterans' Benefits",39:"Postal Service",
    40:"Public Buildings, Property, and Works",41:"Public Contracts",
    42:"The Public Health and Welfare",43:"Public Lands",
    44:"Public Printing and Documents",45:"Railroads",46:"Shipping",
    47:"Telecommunications",48:"Territories and Insular Possessions",
    49:"Transportation",50:"War and National Defense",
    51:"National and Commercial Space Programs",52:"Voting and Elections"
    }
econTitles=['7','11','12','15','21','27','30','31','35','45','46','47','49']
defenseTitles=[]
<<<<<<< Updated upstream
strictEconTitles=[]

def directory_to_changes_list(directoryName):
    "Given a directory to target, extracts all relevant information on tables."
    files=[f for f in sorted(os.listdir(directoryName))]
    results = [parseTable(os.path.join(directoryName,f)) for f in files]
    final=[item for sublist in results for item in sublist]
    return final


def title_mods(changesList,focus=2,onlyInclude=0):
    """
    Takes in a list of changes, and returns the number of changes in a
    given title by default. If you set focus to 4, it can instead grab
    the number of additions(null string), eliminations, revisions, and
    other types of change. Return a dict where keys are titles and the
    values are each lists containing the number of results found to be
    acceptable in a given year. Unless onlyInclude is modified, that's
    going to be all of them.
    """
=======
def directoryToChangesList(directoryName):
    files=[f for f in os.listdir(directoryName) if os.path.isfile(
        os.path.join(directoryName,f))]
    results = [parseTable(os.path.join(directoryName,f)) for f in files]
    final=[item for sublist in results for item in sublist]
    return final
def titleMods(changesList,conditions=0):
    #Has been tested and seems like it works. 
    #At the moment, not tossing errors, at least.
>>>>>>> Stashed changes
    #Structure
    #changesList[change][0] = Section
    #changesList[change][1] = Statue Page
    #changesList[change][2] = USCodeTitle
    #changesList[change][3] = USCodeSection
    #changesList[change][4] = USCodeStatus
<<<<<<< Updated upstream
        #
    from collections import defaultdict
    d = defaultdict(int)
    if not onlyInclude:
        for change in changesList:
            d[change[2]] +=1
    else:
        for change in changesList:
            if change[4] in onlyInclude:
                d[change[2]]+=1
    return d


def target_changes(titleMods,targetTitles=econTitles):
    """
    Returns the number of changes that were about economic titles by 
    default. You can set your own, different, target if you prefer.
    """
    return sum(titleMods[key] for key in titleMods if key in targetTitles)


def all_years(f):
    """
    Will apply the function f to every year recorded, and return the
    results.
    """
    d = os.curdir+"/table3_pages"
    return [f("table3_pages/"+i) for i in sorted(os.listdir(d))]

if __name__ == "__main__":
    #print(target_changes(title_mods(directory_to_changesList("table3_pages/1958"))))
    #print(all_years(lambda x:(title_mods(directory_to_changesList(x)))))
    pass
=======
    from collections import defaultdict
    d = defaultdict(int)
    for change in changesList:
        if not conditions:
            d[change[2]] +=1
        else:
            if d[change][4] in conditions:
                d[change[2]]+=1
    return d
def titleAdds(changesList):
    return titleMods(changesList,"")
def sections(titleMods):
    pass
def changesListTofile(changesList,newFileName):
    pass
if __name__ == "__main__":
    pass
>>>>>>> Stashed changes
