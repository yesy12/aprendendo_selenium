from selenium.webdriver import Firefox
from time import sleep
driver = Firefox()

url = "http://selenium.dunossauro.live/aula_06.html"

driver.get(url)

sleep(2)

forms = [".form-l0c0",".form-l0c1",".form-l1c0",".form-l1c1"]

for form in forms:
    form_lc = driver.find_element_by_css_selector(form)

    input_name = form_lc.find_element_by_css_selector("[name='nome']")
    input_name.send_keys("Alison")

    input_password = form_lc.find_element_by_css_selector("[name='senha']")
    input_password.send_keys("1")

    # button_submit = form_lc.find_element_by_css_selector("[name='l1c1']")
    # button_submit.click()


sleep(2)