"""
1. Pegar todos os links de aulas - ok
2. Navegar até o exercicio 3
"""

from selenium.webdriver import Firefox
from time import sleep
driver = Firefox()

url = "https://selenium.dunossauro.live/aula_04.html"

driver.get(url)

sleep(4)
as_ = driver.find_elements_by_xpath("//aside[@id='aside']/ul/li/a")
hrefs = []

for a in as_:
    href = a.get_attribute("href")
    hrefs.append(href)
    
exe03 = driver.find_elements_by_xpath("//main[@id='main']/ul/li")[2]
exe03_a = exe03.find_element_by_tag_name("a")
exe03_link = exe03_a.get_attribute("href")

driver.get(exe03_link)