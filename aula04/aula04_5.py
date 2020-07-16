"""
1. Pegar todos os links de aulas - ok
2. Navegar até o exercicio 3 - ok
"""

from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

driver = Firefox()

url = "https://selenium.dunossauro.live/aula_04.html"

driver.get(url)

sleep(4)
aulas_as = driver.find_elements_by_xpath("//aside[@id='aside']/ul/li/a")
conteudo = []
aula = 3

for aula_a in aulas_as:
    href = aula_a.get_attribute("href")
    json = {
       f"aula {aula}" : href
    }
    conteudo.append(json)
    aula += 1
    
pprint(conteudo)


exe03 = driver.find_elements_by_xpath("//main[@id='main']/ul/li")[2]
exe03_a = exe03.find_element_by_tag_name("a")
exe03_link = exe03_a.get_attribute("href")

driver.get(exe03_link)