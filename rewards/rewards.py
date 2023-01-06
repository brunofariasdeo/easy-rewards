from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import rewards.constants as constants
import os
import time

class Rewards(webdriver.Edge):
  def __init__(self):
    self.pointsToRedeem = True

    options = Options()
    options.add_argument("headless")
    options.add_argument(f'user-data-dir={constants.PROFILE_PATH}')
    options.add_argument(f'profile-directory={constants.PROFILE_NAME}')

    service = Service(executable_path=constants.EXECUTABLE_PATH)
    super(Rewards, self).__init__(options = options, service = service)

  def get_current_rewards_points(self):
    return self.find_element(By.ID, 'id_rc').text

  def navigate_to_page(self, url):
    self.get(url)
    time.sleep(5)

  def type_in_search_bar(self, string):
    searchBar = self.find_element(By.ID, 'sb_form_q')
    searchBar.send_keys(Keys.SHIFT + Keys.HOME)
    searchBar.send_keys(string)
    searchBar.send_keys(Keys.ENTER)
