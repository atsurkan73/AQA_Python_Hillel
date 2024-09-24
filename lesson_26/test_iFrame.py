import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

class TestIFrametest1():
  def setup_method(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
    self.driver.maximize_window()
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_iFrametest1(self):
    self.driver.get("http://localhost:8000/dz.html")

    # Прокрутка вниз
    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  # Зачекайте трохи після прокрутки вниз

    # Прокрутка вгору
    self.driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)  # Зачекайте трохи після прокрутки вгору

    self.driver.switch_to.frame(0)
    self.driver.find_element(By.ID, "input1").click()
    self.driver.find_element(By.ID, "input1").send_keys("Frame1_Secret")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(3)
    assert self.driver.switch_to.alert.text == "Верифікація пройшла успішно!"

    alert = Alert(self.driver)
    print("\nТекст Alert iFrame1:", alert.text)
    alert.accept()

    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(1)
    self.driver.find_element(By.ID, "input2").click()
    self.driver.find_element(By.ID, "input2").send_keys("Frame2_Secret")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(2)
    assert self.driver.switch_to.alert.text == "Верифікація пройшла успішно!"

    alert = Alert(self.driver)
    print("Текст Alert iFrame2:", alert.text)
    alert.accept()
    time.sleep(2)
  
