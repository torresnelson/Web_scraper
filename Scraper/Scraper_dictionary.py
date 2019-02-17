from bs4 import BeautifulSoup
import requests
links = []
f = open('lista','r')
for i in range(31):
	links.append(str(f.readline()))
f.close()
link = links[0].split('\n')
for i in range (31):
	src = requests.get(link[0])
	src.encoding = 'UTF-8'
	src = src.text
	soup = BeautifulSoup(src, 'lxml')
	results1 = soup.body.find('div', id='columna_resultados_generales')
	results2 = soup.body.find('div', id='columna_resultados_conjugaciones')
	results1 = results1.text.split(')')
	results2 = results2.text.split(')')
	print(results1[1],results2[1])
	link = links[i].split('\n')