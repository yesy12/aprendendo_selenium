from selenium.webdriver import Firefox
from time import sleep
import re

driver = Firefox()
url = "https://curso-python-selenium.netlify.app/exercicio_02.html"

driver.get(url)
sleep(6)

a = driver.find_element_by_tag_name("a")
p0 = driver.find_elements_by_tag_name("p")[0].text
p1 = driver.find_elements_by_tag_name("p")[1].text
p_error = "você está fazendo algo errado"

regex = re.compile("[0-9]+")
numero_esperado = int(regex.findall(p1)[0])

regex = re.compile(rf".+ganhou: {numero_esperado}")
conseguiu = False
while conseguiu == False:
    a.click()

    ps = driver.find_elements_by_tag_name("p")

    for p in ps:
        if(p.text != p0 and p.text != p1 and p.text != p_error):
            numero = regex.findall(p.text)
            if(len(numero)>0):
                conseguiu = True
                break

            # numero = int(p.text)
            # if(numero == numero_esperado):
                # print("a")
                # break
        