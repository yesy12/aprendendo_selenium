# Selenium com Python #04 - Navegação e atributos
# Busca aninhada
# Atributos
# Navegação
from selenium.webdriver import Firefox
from time import sleep

driver = Firefox()

url = "http://selenium.dunossauro.live/aula_04_a.html"
driver.get(url)
sleep(2)
ul = driver.find_element_by_tag_name("ul")
lis = ul.find_elements_by_tag_name("li")

for li in lis:
    a = li.find_element_by_tag_name("a")
    
    href = a.get_attribute("href")
    print(href)






sleep(2)
# driver.quit()