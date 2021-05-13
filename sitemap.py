import requests
import re

url='https://blog.tooziya.com/sitemap.xml'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4464.4 Safari/537.36',
}
response = requests.get(url=url,headers=headers)
response.encoding = 'utf-8'
url_list= re.findall('<loc>(.*?)</loc>',response.text,re.S)
with open('urls.txt','w') as f:
    for url in url_list:
        f.write(url+'\n')