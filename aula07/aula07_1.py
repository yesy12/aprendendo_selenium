# DOM
# CSSOM
# Eventos
# Ouvinte de Eventos

from selenium.webdriver import Firefox
from time import sleep

driver = Firefox()

url = "https://selenium.dunossauro.live/aula_07_d"

driver.get(url)

sleep(4)

input_ = driver.find_element_by_tag_name("input")
input_.click()

span = driver.find_element_by_tag_name("span")
span.click()

p = driver.find_element_by_tag_name("p")
p.click()

input_.click()
p.click()
print(span.text)
# 'está sem foco'

input_.click()
print(span.text)
# 'está com foco'

print(p.text)
# "0"
input_.send_keys("1") 
p.click()

print(p.text)
# '1'