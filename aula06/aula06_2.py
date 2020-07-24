# Selenium com Python #06 - Procurando e interagindo com elementos p.II
# Um pouco de teoria dos seletores
# CSS selector

from selenium.webdriver import Firefox
from time import sleep

driver = Firefox()

url = "http://selenium.dunossauro.live/aula_06_a.html"
driver.get(url)

sleep(4)

nome = driver.find_element_by_css_selector("[name='nome']")
nome.send_keys("Teste")

senha = driver.find_element_by_css_selector("[name='senha']")
senha.send_keys("1234456")

form_group = driver.find_elements_by_css_selector("[class='form-group']")
# print(len(form_group)) # 2

form_group = driver.find_elements_by_css_selector("[class*='group']")
# print(len(form_group)) # 3