
import json
import urllib.request

r = urllib.request.urlopen("http://httpbin.org/get")

text = r.read()
print(r.status, r.reason)
obj = json.loads(text)
print(obj)