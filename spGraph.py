from bs4 import BeautifulSoup
import requests
from random import randint
import re
import networkx as nx
from networkx.readwrite import json_graph
import json
import time


sp100 = requests.get("http://slickcharts.com/sp500")
sp100Text = sp100.text
soup = BeautifulSoup(sp100Text, 'html.parser')
#for link in soup.findAll('a'):
#    print(link.string) # stackoverflow.com/questions/11716380/python-beautifulsoup-extract-text-from-anchor-tag



# stockSymbols = re.findall(r'submit" value="(.*?)"',sp100Text)

stockNames = soup.findAll('a')
stockWeights = re.findall(r'"/> </div></form></td>\n\t\t\t\t\t\t\t\t<td>(.*?)</td>',sp100Text)
stockSymbols = re.findall(r'submit" value="(.*?)"',sp100Text)
nodeNames = []

symbolList = []
G=nx.Graph()

count = 0
for stock in stockNames:
    name = stockNames[count+14].string[0:8]
    if name != "Goog":
        symbol = stockSymbols[count]
        symbol = str(symbol)
        weight = float(stockWeights[count])*20
        weight = str(weight)
        G.add_node(name, sym= symbol, group='a', size=weight, score='0', type='cirlce') 
        symbolList.append(symbol.lower())
        nodeNames.append(name)
        
    count = count + 1
    if count > 505:
        break
    
print("starting links") 
#append 

url = 'http://www.marketwatch.com/investing/stock/'


count = 0
for symbol in stockSymbols:
    

    time.sleep(randint(0, 2))  # relax and don't let google be angry
    stockURL = url+symbol
    getComps = requests.get(stockURL)
    text = getComps.text
    companies = re.findall(r' <td class="table__cell w50"><a class="link" href="http://www.marketwatch.com/investing/stock/(.*?)">',text)
    for company in companies:
        if company in symbolList:
            firstIndex = symbolList.index(company.lower())
            secondIndex = symbolList.index(symbol.lower())
            G.add_edge(nodeNames[firstIndex], nodeNames[secondIndex])
    if count == 100:
        print("100")
    
    if count == 200:
        print("200")
        
    if count == 300:
        print("300")
        
    if count == 400:
        print("400")
    
    if count == 498:
        print("498")
     
    if count > 505:
        break    
    count = count + 1
        
data = json_graph.node_link_data(G)
s = json.dumps(data)

nodeDegrees =  G.degree(weight='weight')

corrList = []
weights = a[1]
weightsAndDegrees = []
for node in nodeDegrees:
    degrees = nodeDegrees.get(node)
    for weight in weights:
        if weight.get('id') == node:
            w = weight.get('size')
            entry = node, weight.get('id'), degrees, w
            corrList.append(entry)


a[1][2].get('id')
nodeDegrees.get(node)


(weights[3]).get('size')
