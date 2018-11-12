import requests
import pprint
import pdb
import matplotlib.pyplot as plt
import numpy as np

'''
username = 'huge'
password = 'file'

url = "http://www.pythonchallenge.com/pc/return/good.html"
r = requests.get(url, auth=(username, password))
x = r.content.decode('UTF-8')
print(x)
'''
first = []
second = []

def scatter_connected(xList, yList):
    xList = np.array(xList)
    yList = np.array(yList)
    inds = yList.argsort()
    sorted_yList = yList[inds]
    sorted_xList = xList[inds]
    return sorted_xList, sorted_yList

with open('code_9_op_first.txt', 'r') as infile:
    for line in infile:
        row = line.strip().split(',')
        if row[-1]=='':
            row.pop()
        first.extend(row)
    print(first)
    print(len(first))

xList = [int(first[i]) for i in range(len(first)) if i%2==0]
print(xList)
yList = [int(first[i]) for i in range(len(first)) if i%2!=0]
print(yList)

x, y = scatter_connected(xList, yList)
plt.scatter(x, y)
plt.show()


with open('code_9_op_second.txt', 'r') as infile:
    for line in infile:
        row = line.strip().split(',')
        if row[-1]=='':
            row.pop()
        second.extend(row)
    print(second)
    print(len(second))

xList_ = [int(second[i]) for i in range(len(second)) if i%2==0]
print(xList_)
yList_ = [int(second[i]) for i in range(len(second)) if i%2!=0]
print(yList_)

x, y = scatter_connected(xList_, yList_)
plt.scatter(x, y)
plt.show()

# adding both first and second
xList.extend(xList_)
yList.extend(yList_)

x, y = scatter_connected(xList, yList)
plt.scatter(x, y)
plt.show()

# plot shows a bull!

