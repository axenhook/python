import requests,re
regex = re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
url = 'http://www.wsbookshow.com/'
html = requests.get(url)
emails = regex.findall(html.text)
for email in emails:
    print(email)