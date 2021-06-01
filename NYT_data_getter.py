# The purpose of this file is to get 20 stories each time it is ran
# with 4 stories from 5 news categories
# then add information from those stories into a database table
# If there aren't at least 20 stories in each category
# stories from other categories will be used
# until the database table reaches 100 rows

#necessities: import, API key, create database table
import json
import csv
import requests
import sqlite3

APIKEY = 'KIBl6ffb7lJrM6UAdpiOwAms0ppqvNf2'
conn = sqlite3.connect('news.sqlite')
cur = conn.cursor()
cur.execute(
    'CREATE TABLE IF NOT EXISTS NYT (title TEXT, author TEXT, published TIMESTAMP, section TEXT)')

#subjects to use
subjects = ['Business', 'Health', 'World', 'Science', 'Technology']
stories=0
totals={}

#get number of stories in each subject
for sub in subjects:
    r = requests.get(
        'https://api.nytimes.com/svc/topstories/v2/'+sub+'.json?api-key='+APIKEY)
    res = r.json()
    total=res["num_results"]
    totals[sub]=total
    stories+=total

#check number of stories in each subject
def usability():
    for sub in subjects:
        if totals[sub]<20:
            return False
    return True

#if the file can be ran 5 times, get an equal distribution of stories
if usability():
    for sub in subjects:
        num=0
        r = requests.get(
            'https://api.nytimes.com/svc/topstories/v2/'+sub+'.json?api-key='+APIKEY)
        res = r.json()
        for news in res['results']:
            _title = news['title']
            _author = news['byline'][3:]
            _published = news['published_date']
            _section = sub
            cur.execute("SELECT title FROM NYT WHERE title = ? LIMIT 1", (_title,) )
            if (num<4) and (cur.fetchone()==None):
                num=num+1
                cur.execute('INSERT INTO NYT (title, author, published, section) VALUES (?,?,?,?)',(_title, _author, _published, _section))
    conn.commit()
else:
    #equal distribution of stories is not possible
    print('One section has insufficient number of stories. File cannot be ran 5 times')
    print("Database will not have an equal number of stories from each section")
    leastStories=sorted(totals.items(),key=lambda x:x[1])[0][1]
    diff=100-(leastStories*5)
    num=0
    for sub in subjects:
        r = requests.get(
            'https://api.nytimes.com/svc/topstories/v2/'+sub+'.json?api-key='+APIKEY)
        res = r.json()
        #one section will be emptied of results, the rest have to make up for it
        for news in res['results'][:leastStories]:
            _title = news['title']
            _author = news['byline'][3:]
            _published = news['published_date']
            _section = sub
            cur.execute('INSERT INTO NYT (title, author, published, section) VALUES (?,?,?,?)',(_title, _author, _published, _section))
    for sub in subjects:
        r = requests.get(
            'https://api.nytimes.com/svc/topstories/v2/'+sub+'.json?api-key='+APIKEY)
        res = r.json()
        for news in res['results']:
            _title = news['title']
            _author = news['byline'][3:]
            _published = news['published_date']
            _section = sub
            cur.execute("SELECT title FROM NYT WHERE title = ? LIMIT 1", (_title,) )
            if (num<diff) and (cur.fetchone()==None):
                num=num+1
                cur.execute('INSERT INTO NYT (title, author, published, section) VALUES (?,?,?,?)',(_title, _author, _published, _section))
    conn.commit()