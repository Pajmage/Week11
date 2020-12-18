# Generated by Selenium IDE
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import unittest



class Test_Add_Rivers_Page(unittest.TestCase):
  def setUp(self):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.vars = {}
  
  def tearDown(self):
    self.driver.quit()
  
  # User A wants to access the river page
  def test_Add_Page_Rendered(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.assertIn("River", self.driver.title)

  # User A can click the Add River link
  def test_Add_Page_Link_Works(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.find_element(By.LINK_TEXT, "Add River").click()
    self.assertEqual(self.driver.title, "Add River Details")

  # User A can click the Results link
  def test_Results_Page_Link_Works(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.find_element(By.LINK_TEXT, "Results").click()
    self.assertTrue(self.driver.title =="See River Details")
  
  # User A can enter data into the webform, returning the default form when they press the submit button
  def test_Form_Entry(self):
    self.driver.get("http://127.0.0.1:8000/")    
    self.driver.find_element(By.ID, "rivername").click()
    self.driver.find_element(By.ID, "rivername").send_keys("TestRiver")
    self.driver.find_element(By.ID, "length").click()
    self.driver.find_element(By.ID, "length").send_keys("46")
    self.driver.find_element(By.ID, "rapids").click()
    self.driver.find_element(By.ID, "rapids").send_keys("2")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    
    inputbox = self.driver.find_element_by_id('rivername')
    self.assertEqual(inputbox.get_attribute('placeholder'),'Enter the name of the river')
    inputbox = self.driver.find_element_by_id('length')
    self.assertEqual(inputbox.get_attribute('placeholder'),'Enter river length in km')
    inputbox = self.driver.find_element_by_id('rapids')
    self.assertEqual(inputbox.get_attribute('placeholder'),'Enter the grade of rapids')


class Test_View_Rivers_Page(unittest.TestCase):
  def setUp(self):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.vars = {}
  
  def tearDown(self):
    self.driver.quit()
  
  # User A wants to access the results page
  def test_View_Page_Rendered(self):
    self.driver.get("http://127.0.0.1:8000/results")
    self.assertIn("River", self.driver.title)

  # User A can click the View Results link from the results page
  def test_View_Page_Hyperlink_Works(self):
    self.driver.get("http://127.0.0.1:8000/results")
    self.driver.find_element(By.LINK_TEXT, "Results").click()
    self.assertEqual(self.driver.title, "See River Details")

  # User A can click the View Results link from the results page
  def test_Add_River_Page_Link_Works(self):
    self.driver.get("http://127.0.0.1:8000/results")
    self.driver.find_element(By.LINK_TEXT, "Add River").click()
    self.assertTrue(self.driver.title =="Add River Details")
  
  # User A can view all data in the table when the View Rivers button is pressed, including the data entered for testing the form works
  def test_Form_View(self):
    self.driver.get("http://127.0.0.1:8000/results")
    self.driver.find_element(By.NAME, "Display").click()
    time.sleep(2)
    table = self.driver.find_element_by_id('Tab_Results')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn("13 TestRiver 46.0 28.75 Medium", [row.text for row in rows])

if __name__ == "__main__":
    unittest.main()