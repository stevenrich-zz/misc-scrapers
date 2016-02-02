#requires selenium, firefox, pyvirtualdisplay, xvfb

from selenium import webdriver
from pyvirtualdisplay import Display

print "Scraping DC Superior Court site..."

display = Display(visible=0, size=(800,600))
display.start()

url = #Enter URL

driver = webdriver.Firefox()
driver.get(url)

driver.quit()
