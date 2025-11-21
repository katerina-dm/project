from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# драйвер
driver = webdriver.Firefox()

def search_with_selenium():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

# На закупки
driver.get('https://zakupki.gov.ru/epz/order/extendedsearch/results.html')

# Загрузка страницы
wait = WebDriverWait(driver, 10)

  # Ищем
search_box = wait.until(EC.visibility_of_element_located((By.ID, 'searchString')))
search_box.clear()
search_box.send_keys('животные')

# Взаимодействие с кнопкой
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary')))
button.click()

 # Пауза для полной загрузки результатов
sleep(5)

# Получаем результаты поиска
results = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'search-result__item-title')))
for res in results[:5]:
    print(res.text.strip())
# Закрываем
#driver.quit()


  