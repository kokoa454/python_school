import requests
import re

url = "https://news.yahoo.co.jp/topics/top-picks?page=1"
urlData = requests.get(url).text

# ex. <div class="sc-3ls169-0 dHAJpi">首相 コメ発言の農水相を更迭へ</div>
pattern = r'<div\sclass="sc-3ls169-0\sdHAJpi">(.*?)</div>'
result = re.findall(pattern, urlData)

print(result)