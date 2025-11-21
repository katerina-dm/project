from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def search_with_selenium():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    # Переход на страницу поиска
    driver.get('https://zakupki.gov.ru/epz/order/quicksearch/search.html')

    # Явное ожидание загрузки страницы
    wait = WebDriverWait(driver, 10)

    # Вводим запрос
    search_box = wait.until(EC.visibility_of_element_located((By.ID, 'searchString')))
    search_box.clear()
    search_box.send_keys('животные')

    # Нажимаем кнопку поиска
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary')))
    button.click()

    # Пауза для полной загрузки результатов
    sleep(5)

    # Получаем результаты поиска
    results = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'search-result__item-title')))
    for res in results[:5]:
        print(res.text.strip())

    # Завершаем
    driver.quit()

search_with_selenium()
