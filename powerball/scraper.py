from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd  
import numpy as np
import re
import os
from operator import itemgetter 


with open('logic.html') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')


csv_file = open('dataSet.csv','w')

csv_writer = csv.writer(csv_file)



headingsArr =[]
try:
	headingI = soup.find('thead')
	for episode in headingI.find_all('th'):
		headingsArr.append(episode.text)
except Exception as e:
	headingI = None

# headingsArr=[x.encode('utf-8') for x in headingsArr]
# with open('output.txt', 'w') as f:
#     for item in headingsArr:
#         f.write("%s\n" % item)

csv_writer.writerow(['Date','Time' , 'Count' , 'Power' , 'PowerBall' , 'Type' , 'NormalBalls'])



try:
	enteries = soup.find('div',class_="dt_list_box bd_all")
except Exception as e:
	enteries = None

Date = []

try:
	for date in enteries.find_all('span',class_='time'):
		Date.append(date.get_text().strip())
except Exception as e:
	date = None




Date=[x.encode('utf-8') for x in Date]



Count = []
try:
	for count in enteries.find_all('strong'):
 		Count.append(count.get_text().strip())
except Exception as e:
	count = None



Power = []

try:
	for power in enteries.find_all('div',class_='power_the tahoma'):
		Power.append(power.get_text().strip())
except Exception as e:
	power = None




PowerAfterBrackets= []

for i in Power:
	PowerAfterBrackets.append(re.sub("[\(\)]", "", i))


PowerBall = []

try:
	for powerball in enteries.find_all('span',class_='pb'):
		PowerBall.append(powerball.get_text().strip())
except Exception as e:
	powerball = None

try:
	for powerball in enteries.find_all('span',class_='pd'):
		PowerBall.append(powerball.get_text().strip())
except Exception as e:
	powerball = None




PowerBallType = []

try:
	for powerballType in enteries.find_all('span',class_='ptype'):
		PowerBallType.append(powerballType.get_text().strip())
except Exception as e:
	powerball = None

NormalBalls = []

try:
	for normalBalls in enteries.find_all('span',class_='b1'):
		NormalBalls.append(normalBalls.get_text().strip())
except Exception as e:
	normalBalls = None


NormalBalls=[x.encode("utf-8") for x in NormalBalls]

time = []
newDate = []
newDate = Date[::2]
time = Date [1::2]


rows = zip(newDate, time ,Count , PowerAfterBrackets ,PowerBall , PowerBallType ,NormalBalls)



# newDate=[x.encode('utf-8') for x in newDate]


# with open('output.txt', 'w') as f:
#     for item in newDate:
#         f.write("%s\n" % item)


#csv_writer.writerow(Date)
for i in rows:
 	csv_writer.writerow(i)


csv_file.close()

data = pd.read_csv('dataSet.csv')

data.dropna(inplace = True) 
  
# new data frame with split value columns 
new = data["NormalBalls"].str.split(" , | . ", n = 5, expand = True) 

#new1 = data["NormalBalls"].str.split(".", n = 5, expand = True) 
 


# making separate first name column from new data frame 
N1= new[0] 
 
# making separate last name column from new data frame 
N2= new[1] 

# making separate last name column from new data frame 
N3= new[2] 

# making separate last name column from new data frame 
N4= new[3] 

# making separate last name column from new data frame 
N5= new[4] 

# print(new1)

# Np1 = new1[0]
# Np2 = new2[1]
# Np3 = new3[2]
# Np4 = new4[3]
# Np5 = new5[4]

rows = zip(newDate, time ,Count , PowerAfterBrackets ,PowerBall , PowerBallType ,N1, N2,N3,N4,N5)

csv_file = open('data.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Date','Time' , 'Count' , 'Power' , 'PowerBall' , 'Type' , 'N1','N2','N3','N4','N5'])

for i in rows:
 	csv_writer.writerow(i)
  
csv_file.close() 
os.remove("dataSet.csv")









