# Gmail app password: qlngqqyqiaqvqgro

import yagmail
import pandas
from news import NewsFeed
import datetime

df = pandas.read_excel('files/people.xls')

for index, row in df.iterrows():
    emails = row['name']
    name = row['name']
    interest = row['interest']

    # Introducing datetime variables ir required str format
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    today = datetime.datetime.now().strftime('%Y-%m-%d')

    news_feed = NewsFeed(interest=interest, from_date=yesterday, to_date=today)

    email = yagmail.SMTP(user="reptile1601@gmail.com", password="qlngqqyqiaqvqgro")

    # Constructing email in yagmail format
    email.send(to=row['email'],
               subject=f'Your latest {interest} news for today!',
               contents=f"Good morning {name}, this is what's new on {interest} today, check it out!\n {news_feed.get()}",
               attachments=None)

