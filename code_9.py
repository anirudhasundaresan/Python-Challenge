import requests
import pprint
import pdb

username = 'huge'
password = 'file'

url = "http://www.pythonchallenge.com/pc/return/good.html"
r = requests.get(url, auth=(username, password))
x = r.content.decode('UTF-8')
print(x)

