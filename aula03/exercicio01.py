from selenium.webdriver import Firefox
from time import sleep


driver = Firefox()
url = "https://curso-python-selenium.netlify.app/exercicio_01.html"

driver.get(url)
sleep(4)

h1 = driver.find_element_by_tag_name("h1")
ps = driver.find_elements_by_tag_name("p")

print(h1.text)
for p in ps:
    print(p.text)

driver.quit()