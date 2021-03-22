"""This (in-progress) file reads in and cleans up the botany data"""

import string
import datetime

#here I import the files. I import a csv of my data and a csv of species names from flora helvetica via GBIF
def importfile(x):
    file = open(x, "r")
    thedata = file.readlines()
    return thedata



#this function removes the /n return symbol at the end of each line
def removereturns(x):
    newlist = []
    for i in x:
        olen = len(i)
        nlen = len(i)- 1
        newlist.append(i[:nlen])
    return newlist
mylist = removereturns(mylist)
floralist = removereturns(floralist)

#make a nested list out of my list of strings using the fact the files are csvs to access the data
def nestedlist(x):
    newlist = []
    for i in x:
        clean = i.split(",")
        newlist.append(clean)
    return newlist

mynestedlist = nestedlist(mylist)
floranestedlist = nestedlist(floralist)

#swap rows and columns to make reference easier
def mymatrix(x):
    newmatrix = []
    newplace = []
    newdate =[]
    newtime = []
    newsci = []
    newname = []
    for i in range(len(x)):
        newplace.append(x[i][0])
        newdate.append(x[i][1])
        newtime.append(x[i][2])
        newsci.append(x[i][3])
        newname.append(x[i][4])
    newmatrix.append(newplace)
    newmatrix.append(newdate)
    newmatrix.append(newtime)
    newmatrix.append(newsci)
    newmatrix.append(newname)
    return newmatrix

def myfloramatrix(x):
    newmatrix = []
    newzero = []
    newone = []
    newtwo = []
    newthree = []
    newfour = []
    newfive = []
    newsix = []
    newseven = []
    neweight = []
    newnine = []
    for i in range(len(x)):
        newzero.append(x[i][0])
        newone.append(x[i][1])
        newtwo.append(x[i][2])
        newthree.append(x[i][3])
        newfour.append(x[i][4])
        newfive.append(x[i][5])
        newsix.append(x[i][6])
        newseven.append(x[i][7])
        neweight.append(x[i][8])
        newnine.append(x[i][9])
    newmatrix.append(newzero)
    newmatrix.append(newone)
    newmatrix.append(newtwo)
    newmatrix.append(newthree)
    newmatrix.append(newfour)
    newmatrix.append(newfive)
    newmatrix.append(newsix)
    newmatrix.append(newseven)
    newmatrix.append(neweight)
    newmatrix.append(newnine)
    return newmatrix

mynewmatrix = mymatrix(mynestedlist)
mynewfloramatrix = myfloramatrix(floranestedlist)

#removes the spaces and the "agg." at the end of each species line in the botany data
def cleanagain(x):
    clean = []
    for i in x:
        if "agg" in i:
            clean.append(i[:len(i)-5])
        elif i[len(i)-1] == " ":
            clean.append(i[:len(i)-1])
        else:
            clean.append(i)
    return clean

mynewmatrix[3] = cleanagain(mynewmatrix[3])

#extract the column of species data I want to compare vs. my list of species


#returns tuple of (list unique items, number unique items) for each column of the matrix.
def occurencelist(x):
    target = []
    for i in x:
        total = 0
        clean = []
        for j in i:
            if j not in clean:
                clean.append(j)
                total += 1
        target.append((total, clean))
    return target

occurencesummary = occurencelist(mynewmatrix)

#prints the occurence tuples for each variable
def printoccsum(x):
    for i in range(len(x)):
        print(x[i][0], mynewmatrix[i][0])

printoccsum(occurencesummary)

#compare the unique species in my sample to the list of species from flora helvetica via GBIF.org (6 December 2020) GBIF Occurrence Download https://doi.org/10.15468/dl.qjrj7a
def compared(x,y):
    clean= []
    for i in x:
        if i not in y:
            clean.append(i)
    return clean

comparison = compared(occurencesummary[3][1], mynewfloramatrix[9])

#fix spelling mistakes/adjust synonyms to match with species list
def fixsci(x,y):
    for k in range(len(y[3])):
        if y[3][k] == "verbanum bonariensis":
            y[3][k] = "verbena bonariensis"
        if y[3][k] == "medicago varia":
            y[3][k] = "medicago sativa"
        if y[3][k] == "geranium pratens":
            y[3][k] = "geranium pratense"
        if y[3][k] == "oenothera":
            y[3][k] = "oenothera biennis"
        if y[3][k] == "senecio jacobaea":
            y[3][k] = "jacobaea vulgaris"
        if y[3][k] == "oenothera biennis ":
            y[3][k] = "oenothera biennis"
        if y[3][k] == "solidalgo canadensis":
            y[3][k] = "solidago canadensis"
        if y[3][k] == "verbascum lynchitis":
            y[3][k] = "verbascum lychnitis"
        if y[3][k] == "verbascum negris":
            y[3][k] = "verbascum nigrum"
        if y[3][k] == "securigea varia":
            y[3][k] = "securigera varia"
        if y[3][k] == "melilotus officianalis":
            y[3][k] = "melilotus officinalis"
        if y[3][k] == "knautia maxima":
            y[3][k] = "knautia dipsacifolia"
        if y[3][k] == "hieracium aurantiacum":
            y[3][k] = "pilosella aurantiaca"
        if y[3][k] == "sysimbrium officinale":
            y[3][k] = "sisymbrium officinale"
        if y[3][k] == "geranium robertanium":
            y[3][k] = "geranium robertianum"
        if y[3][k] == "mycelis muralis":
            y[3][k] = "lactuca muralis"
        if y[3][k] == "calamintha nepeta":
            y[3][k] = "clinopodium nepeta"
        if y[3][k] == "polygonum persicaria":
            y[3][k] = "persicaria maculosa"
        if y[3][k] == "sorbus aria":
            y[3][k] = "aria edulis"
    return mynewmatrix


mynewmatrix = fixsci(comparison,mynewmatrix)
occurencesummary = occurencelist(mynewmatrix)
comparison = compared(occurencesummary[3][1], mynewfloramatrix[9])
print(len(comparison), comparison)

#standardizes date to YYYY-MM-DD format
def fixdate(x):
    cleandate = []
    for i in x[1]:
        if i[2] == "." or i[1] == ".":
            i = datetime.datetime.strptime(i,'%d.%m.%Y').strftime('%Y-%m-%d')
        cleandate.append(i)
    x[1] = cleandate
    return x

mynewmatrix = fixdate(mynewmatrix)

#standardizes time to 24 hour format HH:MM:SS, unrecorded times are stored as empty
def fixtime(x):
    cleantime = []
    for i in x[2]:
        if len(i) > 0:
            if i[len(i)-2] == "A" or i[len(i)-2] == "P":
                i = datetime.datetime.strptime(i, "%I:%M:%S %p").strftime('%H:%M:%S')
            cleantime.append(i)
        else:
            cleantime.append([])
    x[2] = cleantime
    return x

mynewmatrix = fixtime(mynewmatrix)

speciesdict = {}

#makes a dictionary of values for
def makespeciesdict(x):
    clean = []
    for i in range(len(x[1])):
        clean = [x[8][i], x[7][i], x[6][i], x[5][i], x[4][i], x[3][i]]
        speciesdict[x[9][i]] = clean
    return speciesdict

speciesdict = makespeciesdict(mynewfloramatrix)

print(speciesdict["juncus effusus"])

#uses the speciesdict dictionary to append the taxonomic information to the species name. appends [] if none available.
def appendspecies(x,y):
    clean = []
    for i in x[3]:
        for j in y:
            if i == j:
                clean.append(y[j])
        if i not in y:
            clean.append([])
    x.append(clean)
    return x

mynewmatrix = appendspecies(mynewmatrix,speciesdict)

#renaturalizations
def listofnaturalizations():
    natlist = ["madretsch cygnes", "ile de la suze", "mühlebach lücherz", "müllibach ehrlach", "dorfbach lücherz", "ruelbach vinelz", "nidau-büren canal im spärs", "hagneck canal Gauchert", "kallnach kallnach", "epsenmoos Walperswil"]


##replace with gbif international plant names index?
#move into pandas
#method to create date-location slug to identify each survey.

#method to turn data into binary via sparse matrix dictionary matrix? Or panda dataframe with slug as reference?


