# Selenium com Python #05 - Procurando e interagindo com elementos p.I

# Atributos (Globais, Css, Dom)
# Find (id, class, name)
# Elementos Web (input, form)

from selenium.webdriver import Firefox

driver = Firefox()

url = "https://selenium.dunossauro.live/aula_05_a.html"
driver.get(url)

python = driver.find_element_by_id("python")
haskell = driver.find_element_by_id("haskell")

print(python.text)
print(haskell.text)