from urllib.parse import urlparse
url = 'http://www.pm25x.com/city/beijing.htm'
o = urlparse(url)
print(o) 

print("scheme={}".format(o.scheme)) # http
print("netloc={}".format(o.netloc)) # www.pm25x.com
print("port={}".format(o.port))     # None
print("path={}".format(o.path))     # /city/beijing.htm
print("query={}".format(o.query))   # 空