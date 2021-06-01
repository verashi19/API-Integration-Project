import textcleaner as tc
import sqlite3
import json

#pull data from database
conn = sqlite3.connect('news.sqlite')
cur = conn.cursor()
cur.execute('SELECT title, section FROM NYT')
results=cur.fetchall()

#set up initial dictionary: {section:list}
sectionD={}
for result in results:
    title=result[0]
    section=result[1]
    sectionD[section]=sectionD.get(section,0)
    if sectionD[section]==0:
        sectionD[section]=[title]
    else:
        sectionD[section].append(title)

#set up dictionary with list of dictionaries: {section:{word:count}}
for section in sectionD:
    temp={}
    for title in sectionD[section]:
        p1=tc.main_cleaner(title)
        p2=tc.remove_stpwrds(p1)
        p3=p2[0].split()
        for word in p3:
            temp[word]=temp.get(word,0)+1
    sectionD[section]=temp

#condense dictionaries into {section:{number:listofWords}}
for section in sectionD:
    tempD={}
    for pair in sectionD[section].items():
        word=pair[0]
        num=pair[1]
        tempD[num]=tempD.get(num,0)
        if tempD[num]==0:
            tempD[num]=[word]
        else:
            tempD[num].append(word)

    sectionD[section]=tempD

#store results in json
clean=open('cleaned.json','w')
jsoned=json.dumps(sectionD)
clean.write(jsoned)
clean.close()