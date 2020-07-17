from selenium.webdriver import Firefox

driver = Firefox()

url = "https://selenium.dunossauro.live/aula_05_b.html"
driver.get(url)

divs = driver.find_elements_by_class_name("linguagens")
for div in divs:
    nome = div.find_element_by_tag_name("h2").text
    criada = div.find_element_by_tag_name("p").text
    json = {
        nome : criada
    }
    print(json)
topico = driver.find_element_by_class_name("topico")
topico.text