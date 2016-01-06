from selenium import webdriver
from selenium.webdriver.support.ui import Select
import csv
import time
from BeautifulSoup import BeautifulSoup
import re
import string
import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')

#open file to extract individual page links
temp = open("links.txt", "a")

#open browser
driver = webdriver.Firefox()
count=0
driver.get("http://www.sexoffender.nd.gov/OffenderWeb/search/basic")
time.sleep(60)

#click "search" and then change items per page from 10 to 100

hey = raw_input("Number of sex offenders listed: ")
response  = round((int(hey)/100)+1)
while count < response:
	page = driver.page_source
	soup = BeautifulSoup(page)
	print >> temp, soup.prettify()
	count = count+1
	print "saved page " + str(count)
	time.sleep(20)

driver.quit()
temp.close()

#pull links

infile = open("links.txt", "r")
outfile2 = open("offenders.csv", "w")

for line in infile:
	m = re.search("<a href=\"/OffenderWeb/Search/Details/(.+)\">", line)
	if m:
		print >> outfile2, m.group(1)

outfile2.close()

#eliminate any duplicates

dirty = csv.reader(open("offenders.csv","rb"))
clean = csv.writer(open("offenders_clean.csv","wb"))
cases = set()
for row in dirty:
	if row[0] not in cases:
		clean.writerow(row)
		cases.add(row[0])

#pull data

outfile = open("nd_sex_offenders.csv","a")

driver = webdriver.Firefox()
driver.get("http://www.sexoffender.nd.gov/OffenderWeb/search/basic")
time.sleep(10)
with open("offenders_clean.csv", "rb") as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
		temp = open("temp2.txt","w")
		offender_num = row[0]
		driver.get("http://www.sexoffender.nd.gov/OffenderWeb/Search/Details/" + str(offender_num))
		page = driver.page_source
		soup = BeautifulSoup(page)
		print >> temp, soup.prettify()
		temp.close()
		temp_search = open("temp2.txt","r")
		dob = ""
		flag = 0
		count = 0
		for line in temp_search:
			if line.strip() == "Date of Birth:":
				flag = 1
				count = 0
			if line.strip() == "<br />":
				flag = 0
				if count > 0:
					break
			if flag == 1:
				count = count+1
				if count > 2:
					dob = dob + " " + line.strip()
		temp_search.close()
		temp_search = open("temp2.txt","r")
		sex = ""
		flag = 0
		count = 0
		for line in temp_search:
			if line.strip() == "Sex:":
				flag = 1
				count = 0
			if line.strip() == "<br />":
				flag = 0
				if count > 0:
					break
			if flag == 1:
				count = count+1
				if count > 2:
					sex = sex + " " + line.strip()
		temp_search.close()
		temp_search = open("temp2.txt","r")
		race = ""
		flag = 0
		count = 0
		for line in temp_search:
			if line.strip() == "Race:":
				flag = 1
				count = 0
			if line.strip() == "<br />":
				flag = 0
				if count > 0:
					break
			if flag == 1:
				count = count+1
				if count > 2:
					race = race + " " + line.strip()
		temp_search.close()
		temp_search = open("temp2.txt","r")
		height = ""
		flag = 0
		count = 0
		for line in temp_search:
			if line.strip() == "Height:":
				flag = 1
				count = 0
			if line.strip() == "<br />":
				flag = 0
				if count > 0:
					break
			if flag == 1:
				count = count+1
				if count > 2:
					height = height + " " + line.strip()
		temp_search.close()
		temp_search = open("temp2.txt","r")
		weight = ""
		flag = 0
		count = 0
		for line in temp_search:
			if line.strip() == "Weight:":
				flag = 1
				count = 0
			if line.strip() == "<br />":
				flag = 0
				if count > 0:
					break
			if flag == 1:
				count = count+1
				if count > 2:
					weight = weight + " " + line.strip()
		temp_search.close()
		temp_search = open("temp2.txt","r")
		eyes = ""
		flag = 0
		count = 0
		for line in temp_search:
			if line.strip() == "Eye Color:":
				flag = 1
				count = 0
			if line.strip() == "<br />":
				flag = 0
				if count > 0:
					break
			if flag == 1:
				count = count+1
				if count > 2:
					eyes = eyes + " " + line.strip()
		temp_search.close()
		temp_search = open("temp2.txt","r")
		hair = ""
		flag = 0
		count = 0
		for line in temp_search:
			if line.strip() == "Hair Color:":
				flag = 1
				count = 0
			if line.strip() == "<br />":
				flag = 0
				if count > 0:
					break
			if flag == 1:
				count = count+1
				if count > 2:
					hair = hair + " " + line.strip()
		temp_search.close()
		temp_search = open("temp2.txt","r")
		expiration = ""
		flag = 0
		count = 0
		for line in temp_search:
			if line.strip() == "Expiration Date:":
				flag = 1
				count = 0
			if line.strip() == "<br />":
				flag = 0
				if count > 0:
					break
			if flag == 1:
				count = count+1
				if count > 2:
					expiration = expiration + " " + line.strip()
		temp_search.close()
		temp_search = open("temp2.txt","r")
		risk = ""
		flag = 0
		count = 0
		for line in temp_search:
			if line.strip() == "Risk Level:":
				flag = 1
				count = 0
			if line.strip() == "</a>":
				flag = 0
				if count > 0:
					break
			if flag == 1:
				count = count+1
				if count > 4:
					risk = risk + " " + line.strip()
		temp_search.close()
		temp_search = open("temp2.txt","r")
		status = ""
		flag = 0
		count = 0
		for line in temp_search:
			if line.strip() == "Status:":
				flag = 1
				count = 0
			if line.strip() == "</a>":
				flag = 0
				if count > 0:
					break
			if flag == 1:
				count = count+1
				if count > 4:
					status = status + " " + line.strip()
		temp_search.close()
		temp_search = open("temp2.txt","r")
		name = ""
		flag = 0
		count = 0
		for line in temp_search:
			if line.strip() == "Name:":
				flag = 1
				count = 0
			if line.strip() == "</h4>":
				flag = 0
				if count > 0:
					break
			if flag == 1:
				count = count+1
				if count > 2:
					name = name + " " + line.strip()
		temp_search.close()
		temp_search = open("temp2.txt","r")
		offense = ""
		flag = 0
		count = 0
		for line in temp_search:
			if line.strip() == "Offense:":
				flag = 1
				count = 0
			if line.strip() == "<br />":
				if count > 3:
					if flag == 1:
						flag = 0
						offense = offense + " + "
			if flag == 1:
				count = count+1
				if count > 3:
					offense = offense + " " + line.strip()
		temp_search.close()
		temp_search = open("temp2.txt","r")
		conviction = ""
		flag = 0
		count = 0
		for line in temp_search:
			if line.strip() == "DATE:":
				flag = 1
				count = 0
			if line.strip() == "<br />":
				if flag == 1:
					flag = 0
					conviction = conviction + " + "
			if flag == 1:
				count = count+1
				if count > 2:
					conviction = conviction + " " + line.strip()
		temp_search.close()
		temp_search = open("temp2.txt","r")
		disposition = ""
		flag = 0
		count = 0
		for line in temp_search:
			if line.strip() == "DISPOSITION:":
				flag = 1
				count = 0
			if line.strip() == "<br />":
				if flag == 1:
					flag = 0
					disposition = disposition + " + "
			if flag == 1:
				count = count+1
				if count > 2:
					disposition = disposition + " " + line.strip()
		temp_search.close()

		record = (str(name).strip(),str(dob).strip(),str(sex).strip(),str(race).strip(),str(height).strip(),str(weight).strip(),str(eyes).strip(),str(hair).strip(),str(expiration).strip(),str(risk).strip(),str(status).strip(),str(offense).strip(),str(conviction).strip(),str(disposition).strip())
		print >> outfile, "|".join(record)

driver.quit()
os.remove("temp2.txt")
os.remove("links.txt")
os.remove("offenders.csv")
os.remove("offenders_clean.csv")
