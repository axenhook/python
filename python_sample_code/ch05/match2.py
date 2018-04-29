import re
m = re.match(r'[a-z]+','tem12po')
print(m)

if not m==None:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())