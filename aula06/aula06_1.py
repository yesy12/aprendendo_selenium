# Selenium com Python #06 - Procurando e interagindo com elementos p.II
# Um pouco de teoria dos seletores
# CSS selector

from selenium.webdriver import Firefox
from time import sleep

drive = Firefox()

url = "http://selenium.dunossauro.live/aula_06_a.html"
drive.get(url)

sleep(4)

nome = drive.find_element_by_css_selector("input")
nome.send_keys("Teste")