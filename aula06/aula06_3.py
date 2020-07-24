# Selenium com Python #06 - Procurando e interagindo com elementos p.II
# Um pouco de teoria dos seletores
# CSS selector

from selenium.webdriver import Firefox
from time import sleep

driver = Firefox()

url = "http://selenium.dunossauro.live/aula_06_a.html"
driver.get(url)

sleep(4)

div_form_group = driver.find_elements_by_css_selector("div.form-group")

brs = driver.find_elements_by_css_selector("div.form-group + br") 
# encontra br no mesmo nivel hieraquico que div
# <div>
# <br>

for br in brs:
    print(br.get_attribute("id"))
    
brs = driver.find_elements_by_css_selector("div.form-group > br")
# encontra todas as tags brs que sejam filhas de div
# <div>
#     <br>
# </div>
for br in brs:
    print(br.get_attribute("id"))


divs = driver.find_elements_by_css_selector("h2 ~ div")
# Encontra todas as tags divs que estejam no mesmo nível que h2
# Nome:
# Senha:
# 

for div in divs:
    print(div.text)

brs = driver.find_elements_by_css_selector("form br")
# Encontra todas as tags br que sejam filhas de form direta ou indiretamente
# "Filhos" e "Netos"
# <selenium.webdriver.firefox.webelement.FirefoxWebElement (session="11bf3bd4-119c-4522-b2c1-eab1f847570e", element="65bf8185-8b65-4629-8a82-b0d1302fee71")>
# <selenium.webdriver.firefox.webelement.FirefoxWebElement (session="11bf3bd4-119c-4522-b2c1-eab1f847570e", element="d59b271b-34ad-428c-80aa-9ddc1cc6bb35")>
# <selenium.webdriver.firefox.webelement.FirefoxWebElement (session="11bf3bd4-119c-4522-b2c1-eab1f847570e", element="bdf4919c-a098-49ed-9ee5-cb0ded08485f")>
# <selenium.webdriver.firefox.webelement.FirefoxWebElement (session="11bf3bd4-119c-4522-b2c1-eab1f847570e", element="687dc5c9-f306-44cb-898f-2a0783fbc931")>

for br in brs:
    print(br)