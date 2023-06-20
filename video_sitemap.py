import requests
import re

url='https://video.tooziya.com/rss/baidu.xml'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4464.4 Safari/537.36',
}
response = requests.get(url=url,headers=headers)
response.encoding = 'utf-8'
url_list= re.findall('<loc>(.*?)</loc>',response.text,re.S)
with open('video_urls.txt','w') as f:
    f.write('https://tooziya.com'+'\n')
    f.write('https://api.tooziya.com'+'\n')
    f.write('https://img.tooziya.com'+'\n')
    f.write('https://sng.tooziya.com'+'\n')
    f.write('https://video.tooziya.com'+'\n')
    f.write('https://jx.tooziya.com'+'\n')
    f.write('https://music.tooziya.com'+'\n')
    f.write('https://blog.tooziya.com'+'\n')
    f.write('https://www.tooziya.com'+'\n')
    for url in url_list:
        f.write(url+'\n')