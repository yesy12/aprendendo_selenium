from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
import re

driver = Firefox()
url_exercicio = "https://selenium.dunossauro.live/exercicio_03.html"

driver.get(url_exercicio)
driver.implicitly_wait(8)

link_exercicio_pt1 = driver.find_element_by_xpath("//main[@id='main']/li/a")
link_exercicio_pt1.click()
driver.implicitly_wait(4)

#page_1.html

p_operacao = driver.find_elements_by_xpath("//main[@id='main']/p")[1]
lis_sugestoes = driver.find_elements_by_xpath("//main[@id='main']/li")

regex = re.compile("[0-9]+")
regex2 = re.compile("[*-+]")

numeros = regex.findall(p_operacao.text)
sinal = regex2.findall(p_operacao.text)[0]
resultados = 0

if(sinal == "*"):
    resultados = int(numeros[0]) * int(numeros[1])

   
for li_sugestao in lis_sugestoes:
    if(int(li_sugestao.text) != resultados):
        link_exercicio_pt2 = li_sugestao.find_element_by_tag_name("a")

link_exercicio_pt2.click()
        

#page_2.html

driver.refresh()

# Não foi possivel realizar a conclusao do exercicio 
# Necessita do conhecimento de wait
# Página simplesmente não carrega apartir daqui

title = driver.title
lis_sugestoes = driver.find_elements_by_xpath("//main[@id='main']/li")

for li_sugestao in lis_sugestoes:
    if(li_sugestao.text == title):
        link_exercicio_pt3 = li_sugestao.find_element_by_tag_name("a")

link_exercicio_pt3.click()


#page_3.html

driver.implicitly_wait(8)

final_url = urlparse(driver.current_url).path

lis_sugestoes = driver.find_elements_by_xpath("//main[@id='main']/li")

for li_sugestao in lis_sugestoes:
    if(f"/{li_sugestao.text}" == final_url):
        link_exercicio_pt4 = li_sugestao.find_element_by_tag_name("a")
        
link_exercicio_pt4.click()


#page_4.html

driver.implicitly_wait(10)

driver.refresh()