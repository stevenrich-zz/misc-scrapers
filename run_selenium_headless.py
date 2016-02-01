from selenium import webdriver
from pyvirtualdisplay import Display

print "Scraping DC Superior Court site..."

display = Display(visible=0, size=(800,600))
display.start()

driver = webdriver.Firefox()
driver.get("https://www.dccourts.gov/cco/maincase.jsf")
