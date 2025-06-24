import bs4 as bs
import requests

url = "https://genius.com/a/cardi-b-is-going-outside-on-defiant-new-single"

html = requests.get(url)
soup = bs.BeautifulSoup(html.content, "html.parser")

title = soup.find("h1", {"class": "article_title"})
print("問1 タイトルタグ: ", title)

pTag = soup.find_all("p")
print("問2 すべてのpタグ: ", pTag)
print("問3 pタグの数: ", len(pTag))
print("問4 2番目のpタグの中身: ", pTag[1].text)
print("問5 タイトルの文字数: ", len(title.text))

aTag = soup.find_all("a")
print("問6 最初のaタグの中身: ", aTag[0].text)