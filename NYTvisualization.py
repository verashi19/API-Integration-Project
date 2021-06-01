#bar graph of number of unique words extracted from each section title

import matplotlib.pyplot as plt
import json

new={}
source=open('NYTcleaned.json','r')
mainD=json.load(source)
#structure: {Business:{count:wordlist,count2:wordList2}}

for section in mainD:
    new[section]=0
    for key in mainD[section]:
        new[section]+=len(mainD[section][key])

tList=list(new.items())
useList=sorted(tList,key=lambda tup:tup[1], reverse=True)[:5]

print(useList)
xvals = [tup[0] for tup in useList]
yvals = [tup[1] for tup in useList]
plt.bar(xvals, yvals)#, align = "center", color = ["green", "yellow"])
plt.ylabel("Number of Words")
plt.xlabel("NYT Section")
plt.title("Number of Unique Words in Titles of Top Stories Retrieved")
plt.savefig("NYTbar.png")
plt.show()