from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from essential_generators import DocumentGenerator

import random
import rewards.constants as constants
import time

class Rewards(webdriver.Edge):
  def __init__(self):
    self.pointsToRedeem = True
    self.tasksToClick = True

    options = Options()
    options.add_argument("headless")
    options.add_argument(f'user-data-dir={constants.PROFILE_PATH}')
    options.add_argument(f'profile-directory={constants.PROFILE_NAME}')

    service = Service(executable_path=constants.EXECUTABLE_PATH)
    super(Rewards, self).__init__(options = options, service = service)

  def find_available_tasks(self):
    try:
      while(self.tasksToClick):
        availableTask = self.find_element(By.XPATH, '//div[contains(@class, "rewards-card-container")]//span[contains(@class, "AddMedium")]')

        availableTask.click()

        time.sleep(5)

        self.switch_page_to_home()
    except NoSuchElementException:
      self.tasksToClick = False


  def get_current_rewards_points(self):
    return self.find_element(By.ID, 'id_rc').text

  def navigate_to_page(self, url):
    self.get(url)
    time.sleep(5)

  def search_on_bing(self):
    self.navigate_to_page("https://bing.com")

    try:
      while(self.pointsToRedeem):
        documentGenerator = DocumentGenerator()
        generatedSentence = documentGenerator.sentence()
        
        time.sleep(random.randint(0, 9))

        rewardsPointsBeforeSearch = self.get_current_rewards_points()
        self.type_in_search_bar(generatedSentence)

        time.sleep(3)

        if (rewardsPointsBeforeSearch == self.get_current_rewards_points()):
          self.pointsToRedeem = False
    except Exception:
      time.sleep(2)

  def switch_page_to_home(self):
    window_name = self.window_handles[0]

    self.switch_to.window(window_name=window_name)

    time.sleep(5)

  def type_in_search_bar(self, string):
    searchBar = self.find_element(By.ID, 'sb_form_q')
    searchBar.send_keys(Keys.SHIFT + Keys.HOME)
    searchBar.send_keys(string)
    searchBar.send_keys(Keys.ENTER)
