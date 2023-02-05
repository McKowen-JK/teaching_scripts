import requests
import re
from bs4 import BeautifulSoup
gradefile=open('gradefile.csv', 'w')
with open('res.txt') as f:
	for line in f:
		uname = str(line).rstrip()
		site = "https://www.inaturalist.org/people/"
		link = site + uname

		response = requests.get(link)

		if response.status_code == 200:
			page = requests.get(link)
			soup = BeautifulSoup(page.text, 'html.parser')
			lbs = soup.select("a.list-group-item:nth-child(1) > span:nth-child(1)")
			pbs = str(lbs).strip('[]')
			ubs = pbs.split('>')
			ubs2 = str(ubs[1])
			xbs = ubs2.split('<')
			obs = int(xbs[0])


		elif response.status_code == 404:
			obs = int(0)


		if(obs>=6):
			grade = ("3");
		elif(obs==5):
			grade = ("2.5");
		elif(obs==4):
			grade = ("2");
		elif(obs==3):
			grade = ("1.5");
		elif(obs==2):
			grade = ("1");
		elif(obs==1):
			grade = ("0.5");
		elif(obs==0):
			grade = ("0");
	

		gradefile.writelines(grade +"\n")

#input("Press any key")
