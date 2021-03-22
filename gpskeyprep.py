"""This file cleans the gps-key file and imports it as a dictionary"""

import string

#cleaning up the gpskey file
#identifies and revmoes bad returns in the file, printing to gpskey-cleaned.csv.
def findbadreturns(x):
    file = open(x)
    gpskey = file.readlines()
    file.close()
    cleanedgpskey = open("gpskey-cleaned.csv", "w")
    for i in gpskey:
        if len(i)>2:
            cleanedgpskey.write(i[::])
    cleanedgpskey.close()
findbadreturns("gpskey.csv")

#now that the lines in the file are correct, it will be read in and stored as list.
def readtolist(x):
    file = open(x)
    gpskeyl = file.readlines()
    file.close()
    return gpskeyl

keylist = readtolist("gpskey-cleaned.csv")

#remove end of line symbols
def removereturns(x):
    newlist = []
    for i in x:
        olen = len(i)
        nlen = len(i)- 1
        newlist.append(i[:nlen])
    newlist[0] = "longitude, lattitude, location"
    return newlist

keylist = removereturns(keylist)

#remove double quotation marks within the file
def removedoublequotes(x):
    newlist = []
    for i in x:
        rlen = len(i)
        newentry = ""
        for j in i:
            if j != "\"":
                newentry += j
        newlist.append(newentry)
    return newlist

keylist = removedoublequotes(keylist)

#uppercase converted to lower case
def uppercaseout(x):
    new = []
    for i in x:
        mysubs = i.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")
        cleaned = i.translate(mysubs)
        new.append(cleaned)
    return new

keylist = uppercaseout(keylist)

#extract the values into a nested list using the comma separation format
def extractvalues(x):
    listoflist = []
    for i in range(len(x)):
        sublist = x[i].split(",")
        listoflist.append(sublist)
    return listoflist

keylist = extractvalues(keylist)

#create a dictionairy {(name), (long, lat)} with the values.
def addtodict(x):
    gpsdict = {}
    for i in range(len(x)):
            name = x[i][2]
            gpsdict[name] = (x[i][0], x[i][1])
    return gpsdict

keydict = addtodict(keylist)
print(keydict)

