import re
import json
from collections import defaultdict
def primary(
        startYear=1927,endYear=2013,
        jsonFileName="tempFile.json",csvFileName="tempFile.csv",
        optionsDict={}):
    import parseAllTables as pat
    #This is a long fucking line to execute, but that's OK.
    full_list = pat.all_years(lambda x:(pat.title_mods(
        pat.directory_to_changes_list(x))))
    full_dict=titles_list_to_dict(full_list)
    dict_to_json_file(full_dict,jsonFileName)
    changes_json_to_CSV(jsonFileName,csvFileName,startYear,endYear)

def full_list_to_dict(l):
    """Takes in a list.
    The sample list would be
    import parseAllTables as p
    p.all_years(lambda x:(p.title_mods(p.directory_to_changes_list(x)))
    """

    #Sets up the keys for the dictionary.
    x=[d.keys() for d in l]
    titles = set([y for z in x for y in z])
    titles.discard("")
    #Grabs everything that matches one of the keys
    final_dict={t:[d[t] for d in l] for t in titles}
    return final_dict

def dict_to_json_file(dct,newFileName):
    #Helper for the lazy.
    with open(newFileName,"a") as nf:
        nf.write(json.dumps(dct))


def changes_json_to_CSV(jsonFile,newFileName,
                        startingYear=1789,endingYear=2014):
    """Converts a json file to a csv file. Will throw appropriate 
    errors. """
    # A utility function not needed elsewhere. Sorts numbers in a
    # sensible fashion, unlike default sorting techniques. Modified
    # from the script here:
    # http://blog.codinghorror.com/sorting-for-humans-natural-sort-order/
    def humansort(l):
        convert = lambda text: int(text) if text.isdigit() else text
        alphanum_key = lambda key:[
            convert(c) for c in re.split('([0-9]+)', key)]
        return sorted(l,key=alphanum_key)

    dct=json.loads(open(jsonFile).read())
    if endingYear-startingYear+1 != len(dct[dct.keys()[0]]):
        print("""The number of years provided for is not the same as the length. 
            The resulting file is likely to have errors.""")
    for key in dct.keys():
        dct[key]=",".join([str(eb) for eb in dct[key][startingYear-1789:endingYear+1]])
    dct["0"]="".join([str(k)+"," for k in range(startingYear,endingYear+1)])
    
    with open(newFileName,"a") as a:
        for key in humansort(dct.keys()):
            a.write(key+","+dct[key]+"\n")
    #Currently generally aimed at titleOverTime.json
