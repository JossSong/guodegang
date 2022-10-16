import requests
import re
import os

#代{过}{滤}理
# os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["https_proxy"] = "http://127.0.0.1:7890"

def download_music(url, time):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'}
    r = requests.get(url, headers=headers)
    html = r.text
    names = re.compile('{name: "\d+《(.*?)》"').findall(html)
    urls = re.compile(',artist: ".*?",url: "(.*?)",').findall(html)
    for i in range(0, len(names)):
        a = os.path.exists("郭德纲相声" + str(time))
        if not a:
            os.makedirs("郭德纲相声"+str(time))
        if os.path.exists("郭德纲相声"+str(time)+"/"+names[i]+".mp3"):
            print(str(names[i])+" 在表中")
        else:
            request_url = "https:" + urls[i]
            request_html = requests.get(request_url, headers=headers).content
            fh = open("郭德纲相声"+str(time)+"/"+names[i]+".mp3", "ab")
            fh.write(request_html)
            fh.flush()
            print(str(i+1)+"："+names[i]+" ok")
            fh.close()

for time in range(1, 8):
    url = "https://www.xsmp3.com/gdg-yq/gdg-yq-"+str(time)+".html"
    download_music(url, time)
    print("第"+str(time)+"个文件夹已下载完成！\n")
