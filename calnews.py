import sqlite3
import matplotlib
import matplotlib.pyplot as plt

conn = sqlite3.connect('news.sqlite')
cur = conn.cursor()
# Calculate the number and percentage of the news that miss the author's name
"""
cur.execute('SELECT count(news_name) as anonymity FROM News WHERE author IS NULL')
for row in cur:
    print(row[0])
xvals = ["having no author names", "having author names"]
yvals = [row[0],(100-row[0])]

# bar chart
plt.bar(xvals, yvals, align = "center", color = ["skyblue", "cadetblue"])
plt.ylabel("Count of News")
plt.xlabel("Anomity of authors")
plt.title("Number of anonymous news among 100 news")
plt.savefig("bar.png")
plt.show()
"""

# generate a dictionary that counts the number of news from different media
cur.execute("SELECT * FROM News")
media_dict={}
for row in cur:
    media = row[0]
    media_dict[media] = media_dict.get(media, 0) + 1
print(media_dict)

"""
# draw the top 5 media sources
cur.execute("SELECT news_name, count(news_name) as num FROM News GROUP BY news_name HAVING num > 1 ORDER BY num DESC LIMIT 5")
for row in cur:
    print(row)
xvals = ["CNN", "Youtube.com", "Gizmodo.com", "Espn.com", "Fox News"]
yvals = [7,7,4,3,3]
plt.bar(xvals, yvals, align = "center", color = ["#ba68c8", "#ba68c8", "#ce93d8", "#e1bee7", "#f3e5f5"])
plt.ylabel("Number of Articles")
plt.xlabel("Media Name")
plt.title("Top 5 media sources")
plt.savefig("bar2.png")
plt.show()


# generate top 3 media for business articles
cur.execute("SELECT news_name, count(news_name) as num FROM News GROUP BY news_name HAVING subject == 'business' ORDER BY num DESC LIMIT 3")
print("the top 3 media channels for business articles: ")
for row in cur:
    print(row)

# generate top 3 media for sports articles
cur.execute("SELECT news_name, count(news_name) as num FROM News GROUP BY news_name HAVING subject == 'sports' ORDER BY num DESC LIMIT 3")
print("the top 3 media channels for sports articles: ")
for row in cur:
    print(row)

# generate top 3 media for entertainment articles
cur.execute("SELECT news_name, count(news_name) as num FROM News GROUP BY news_name HAVING subject == 'entertainment' ORDER BY num DESC LIMIT 3")
print("the top 3 media channels for entertainment articles: ")
for row in cur:
    print(row)

# generate top 3 media for science articles
cur.execute("SELECT news_name, count(news_name) as num FROM News GROUP BY news_name HAVING subject == 'science' ORDER BY num DESC LIMIT 3")
print("the top 3 media channels for science articles: ")
for row in cur:
    print(row)

# generate top 3 media for technology articles
cur.execute("SELECT news_name, count(news_name) as num FROM News GROUP BY news_name HAVING subject == 'technology' ORDER BY num DESC LIMIT 3")
print("the top 3 media channels for technology articles: ")
for row in cur:
    print(row)
"""