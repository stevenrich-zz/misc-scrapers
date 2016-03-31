# a script to translate multiple documents using Google translate

from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800,600))
display.start()

url = "translate.google.com"

driver = webdriver.Firefox()
driver.get(url)

#upload document

driver.quit()
display.stop()
