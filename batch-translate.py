# a script to translate multiple documents using Google translate

import time
from BeautifulSoup import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import csv

print "Translating documents..."

driver = webdriver.Firefox()
driver.get("https://translate.google.com/?tr=f&hl=en")

#files.csv has two columns, the filepath and the name of the file

with open("files.csv", "rb") as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
		filepath = row[0]
		filename = row[1]
		time.sleep(3)
		fileInput = driver.find_element_by_css_selector("input[type='file']")
		fileInput.send_keys(str(filepath) + "/" + str(filename) + ".pdf")
		translate = driver.find_element_by_css_selector("input[type='submit']")
		translate.click()
		output = open(str(filepath) + "/" + str(filename) + "_translated.html", "w")
		page = driver.page_source
		soup = BeautifulSoup(page)
		print >> output, soup.prettify()
		print "Translated " + str(filename)
		time.sleep(3)
		driver.back()
		
driver.quit()
		
