from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class Home:

    def test(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        baseUrl = "https://rahulshettyacademy.com/angularpractice"
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]").click()

        products = driver.find_elements(By.XPATH, "//div[@class='card h-100']//div/h4/a")
        for product in products:
            if product.text == "Blackberry":
                product.find_element(By.XPATH, "//div/div/div[2]/app-card-list/app-card[4]/div/div[2]/button").click()


        cart = driver.find_element(By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']" )
        cart.click()

        checkOut = driver.find_element(By.CSS_SELECTOR, "button[class*='btn btn-success']")
        checkOut.click()


        driver.find_element(By.ID, "country").send_keys("ger")

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                                                ignored_exceptions=[NoSuchElementException,
                                                                     ElementNotVisibleException,
                                                                     ElementNotSelectableException])
        element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Germany")))
        element.click()

        driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

        purchaseBtn = driver.find_element(By.CSS_SELECTOR, "input[class='btn btn-success btn-lg']")
        purchaseBtn.click()


        print(driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']").text)


cc = Home()
cc.test()