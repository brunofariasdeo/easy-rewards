from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from essential_generators import DocumentGenerator
from dotenv import load_dotenv

import os
import random
import time

load_dotenv()

EXECUTABLE_PATH = os.getenv('EXECUTABLE_PATH')
PROFILE_NAME = os.getenv('PROFILE_NAME')
PROFILE_PATH = os.getenv('PROFILE_PATH')

options = Options()
# options.add_argument("headless")
options.add_argument(f'user-data-dir={PROFILE_PATH}')
options.add_argument(f'profile-directory={PROFILE_NAME}')

driver = webdriver.Edge(options = options, executable_path=EXECUTABLE_PATH)

driver.get('https://bing.com')
documentGenerator = DocumentGenerator()

while True:
  try:
    rewardsPoints = driver.find_element(By.ID, 'id_rc').text

    generatedSentence = documentGenerator.sentence()

    bingSearch = driver.find_element(By.ID, 'sb_form_q')
    bingSearch.send_keys(Keys.SHIFT + Keys.HOME)
    bingSearch.send_keys(generatedSentence)
    bingSearch.send_keys(Keys.ENTER)

    time.sleep(random.randint(0, 9))

    if (driver.find_element(By.ID, 'id_rc').text == rewardsPoints):
      break

  except NoSuchElementException:
    time.sleep(5)
  except StaleElementReferenceException:
    time.sleep(5)
