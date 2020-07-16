# Selenium com Python #04 - Navegação e atributos
# Busca aninhada
# Atributos
# Navegação
from selenium.webdriver import Firefox
from time import sleep

driver = Firefox()

url = "http://selenium.dunossauro.live/aula_04_b.html"
driver.get(url)

sleep(2)
boxs = ["box-1","box-2","box-3","box-4"]
    
for box in boxs:
    box = driver.find_element_by_id(box)
    box.click()
    sleep(0.2)

for i in range(4):
    driver.back()
    sleep(0.4)

for i in range(4):
    driver.forward()
    sleep(0.4)
