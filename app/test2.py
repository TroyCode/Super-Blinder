# import urllib.request
# import re

# # http://www.youtube.com/watch?v=fpyre5Jrrew
# # email_re = re.compile(r'([\w\.,]+@[\w\.,]+\.\w+)')
# # youtube_re = re.compile(r'(http\:\/\/www\.youtube\.com\/watch\?v\=[\w])')
# result = []

# user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
# headers={'User-Agent':user_agent,} 

# with urllib.request.Request('https://tw.voicetube.com/videos/261?ref=imdb', headers = hdr) as response:
#    html = response.read().decode()

#    # result += youtube_re.findall(html)
#    # print(result)

import urllib.request
import re

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = "https://tw.voicetube.com/videos/261?ref=imdb"
headers = {'User-Agent': user_agent} 
youtube_re = re.compile(r'youtube')
email_re = re.compile(r'([\w\.,]+@[\w\.,]+\.\w+)')
result = []

request = urllib.request.Request(url, None, headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() # The data u need
# print(data.decode())
result += youtube_re.findall(data.decode())
print(result)