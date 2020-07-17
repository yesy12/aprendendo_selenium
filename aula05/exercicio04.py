from selenium.webdriver import Firefox
from time import sleep
from json import loads

driver = Firefox()

url = "https://selenium.dunossauro.live/exercicio_04.html"
driver.get(url)

sleep(10)
nome = driver.find_element_by_name("nome")
email = driver.find_element_by_name("email")
senha = driver.find_element_by_name("senha")
telefone = driver.find_element_by_name("telefone")
enviar = driver.find_element_by_name("btn")


nome.send_keys("Alison")
email.send_keys("a@a.com")
senha.send_keys("12345678")
telefone.send_keys("11123456789")
enviar.click()

sleep(8)

dados = {
    "nome" : "Alison",
    "email" : "a@a.com",
    "senha" : "12345678",
    "telefone" : "11123456789"
}

main = driver.find_element_by_tag_name("main")
resultado = main.find_element_by_tag_name("textarea").text
resultado_replace = resultado.replace("\'","\"")

dados_retornados = loads(resultado_replace)
dados_retornados == dados

driver.quit()