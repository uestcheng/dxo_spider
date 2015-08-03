from selenium import webdriver

URL = "http://www.dxomark.com/Lenses#year=1987%2C2015&price=0%2C13000&xDataType=year&yDataType=global&viewMode=list"

dr = webdriver.Firefox()

dr.get(URL)
close_button = dr.find_element_by_xpath("//div[@class='popupClose']")
if close_button.is_displayed():
    close_button.click()

button = dr.find_element_by_xpath("//a[@id='filterLensesLink']")
print dir(button)
print button.text

