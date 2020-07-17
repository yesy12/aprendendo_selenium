from selenium.webdriver import Firefox

driver = Firefox()

url = "https://selenium.dunossauro.live/aula_05_c.html"
driver.get(url)

filme = driver.find_element_by_name("filme")
email = driver.find_element_by_name("email")
telefone = driver.find_element_by_name("telefone")
enviar = driver.find_element_by_name("enviar")

filme.send_keys("teste")
email.send_keys("a@a.com")
telefone.send_keys("(011)123456789")
enviar.click()