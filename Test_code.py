from datetime import datetime
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import urllib.request
import json

#GET ​/metrics​/pageviews​/top-by-country​/{project}​/{access}​/{year}​/{month} Get pageviews by country and access method.

output = open('en_wiki_cn_rank.csv', 'w', encoding='utf-8')

for year in range(2016,2021):
    for month in range(1,13):
        if month < 10:
            api_location = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/top-by-country/en.wikipedia/all-access/{year}/0{month}'
        else:
            api_location = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/top-by-country/en.wikipedia/all-access/{year}/{month}'
        response = urllib.request.urlopen(api_location)
        response_text = response.read().decode('utf-8')
        
        country_rank = json.loads(response_text)
        country_rank['items'][0]['countries']
        
        for rank in country_rank['items'][0]['countries']:
            if rank['country'] == 'CN':
                output.write(str(year))
                output.write(',')
                output.write(str(month))
                output.write(',')
                output.write(str(rank['rank']))
                output.write(',')
                output.write(str(rank['views']))
                output.write('\n')
output.close()
# This one very successful!
# en.wikipedia was blocked since 2019 April!

output = open('ja_wiki_cn_rank.csv', 'w', encoding='utf-8')

for year in range(2016,2021):
    for month in range(1,13):
        if month < 10:
            api_location = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/top-by-country/ja.wikipedia/all-access/{year}/0{month}'
        else:
            api_location = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/top-by-country/ja.wikipedia/all-access/{year}/{month}'
        response = urllib.request.urlopen(api_location)
        response_text = response.read().decode('utf-8')
        
        country_rank = json.loads(response_text)
        country_rank['items'][0]['countries']
        
        for rank in country_rank['items'][0]['countries']:
            if rank['country'] == 'CN':
                output.write(str(year))
                output.write(',')
                output.write(str(month))
                output.write(',')
                output.write(str(rank['rank']))
                output.write(',')
                output.write(str(rank['views']))
                output.write('\n')
output.close()

output = open('zh_wiki_cn_rank.csv', 'w', encoding='utf-8')

for year in range(2016,2021):
    for month in range(1,13):
        if month < 10:
            api_location = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/top-by-country/zh.wikipedia/all-access/{year}/0{month}'
        else:
            api_location = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/top-by-country/zh.wikipedia/all-access/{year}/{month}'
        response = urllib.request.urlopen(api_location)
        response_text = response.read().decode('utf-8')
        
        country_rank = json.loads(response_text)
        country_rank['items'][0]['countries']
        
        for rank in country_rank['items'][0]['countries']:
            if rank['country'] == 'CN':
                output.write(str(year))
                output.write(',')
                output.write(str(month))
                output.write(',')
                output.write(str(rank['rank']))
                output.write(',')
                output.write(str(rank['views']))
                output.write('\n')
output.close()

# Page View Fluctuation

api_location = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/zh.wikipedia/all-access/all-agents/Wikipedia:%E9%A6%96%E9%A1%B5/daily/20150701/20210228'

response = urllib.request.urlopen(api_location)
response_text = response.read().decode('utf-8')
    
zh_frontpage_result = json.loads(response_text)
    
output = open('zh_frontpage_pageviews_20150701_20210228.csv', 'w', encoding='utf-8')

# output.write('article')
# output.write(',')
# output.write("timestamp")
# output.write(',')
# output.write("views")
# output.write('\n')

for pageview in zh_frontpage_result["items"]:
    output.write(pageview['article'])
    output.write(',')
    output.write(str(pageview["timestamp"]))
    output.write(',')
    output.write(str(pageview["views"]))
    output.write('\n')

output.close()

# Plot this into a graph then

headers = ['article', 'timestamp', 'views']

zh_frontpage_df = pd.read_csv("zh_frontpage_pageviews_20150701_20210228.csv", names=headers)

print(zh_frontpage_df)

zh_frontpage_df['timestamp'] = zh_frontpage_df['timestamp'].map(lambda x: datetime.strptime(str(x), '%Y%m%d%H'))
x = zh_frontpage_df['timestamp']
y = zh_frontpage_df['views']

fig1 = plt.plot(x,y)
fig1.show()
