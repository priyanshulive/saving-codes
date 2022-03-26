import urllib.request
p=urllib.request.urlopen("www.google.com")
print(p)
t=p.getcode()
print(t)
code= p.read()
print(code)
meta=p.headers
meta1=p.info()
print(meta)
print(meta1)
u=p.geturl()
webbrowser.open(u)