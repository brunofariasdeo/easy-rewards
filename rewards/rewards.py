from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from essential_generators import DocumentGenerator
import logging
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
    logging.info("Finding available tasks")
    try:
      while(self.tasksToClick):
        availableTask = self.find_element(By.XPATH, '//div[contains(@class, "rewards-card-container")]//span[contains(@class, "AddMedium")]')
        availableTask.click()
        logging.info("Element found. Clicked on it.")

        time.sleep(5)

        self.switch_page_to_home()
    except NoSuchElementException:
      logging.info("You've already completed all tasks. Moving on.")
      self.tasksToClick = False

  def find_login_button(self):
    time.sleep(5)

    try:
      authenticateButton = self.find_element(By.XPATH, '//a[contains(text(), "Entrar")]')

      if (len(authenticateButton) > 0):
        logging.info("Authenticating.")
        authenticateButton.click()
    except Exception as e:
      logging.info("Login button not found.")
      time.sleep(5)

  def get_current_rewards_points(self):
    return self.find_element(By.ID, 'id_rc').text

  def navigate_to_page(self, url):
    logging.info("Navigating to page: " + url)
    self.get(url)
    time.sleep(5)

  def play_a_game(self, gameName):
    self.navigate_to_page("https://www.xbox.com/pt-BR/play")
    logging.info("Opening Xbox Cloud.")

    self.find_login_button()

    try:
      game = self.find_element(By.XPATH, f'//div[contains(text(), "{gameName}")]/ancestor::div[contains(@class, "BaseItem")]')
      game.click()
      logging.info("Game found. Clicked on it.")

      time.sleep(5)

      confirmButton = self.find_element(By.XPATH, '//button[contains(text(), "Continuar mesmo assim")]')
      confirmButton.click()
      logging.info("Confirm button found. Clicked on it.")
      logging.info(f"{gameName} will be running for 10 minutes. This page will be closed once finished.")

      time.sleep(600)
    except Exception as e:
      logging.info("Game not found. Moving on.")


  def search_on_bing(self):
    self.navigate_to_page("https://bing.com")

    logging.info("Starting Bing search.")
    try:
      while(self.pointsToRedeem):
        documentGenerator = DocumentGenerator()
        generatedSentence = documentGenerator.sentence()
        
        time.sleep(random.randint(0, 9))

        rewardsPointsBeforeSearch = self.get_current_rewards_points()
        logging.info("You currently have " + rewardsPointsBeforeSearch + " points.")

        self.type_in_search_bar(generatedSentence)
        time.sleep(5)

        if (rewardsPointsBeforeSearch == self.get_current_rewards_points()):
          logging.info("You've already completed all searches. Moving on.")
          self.pointsToRedeem = False
    except Exception as e:
      logging.error("Error while trying to search on Bing.", e)
      time.sleep(2)

  def switch_page_to_home(self):
    logging.info("Going back to the previous page.")
    window_name = self.window_handles[0]

    self.switch_to.window(window_name=window_name)

    time.sleep(5)

  def type_in_search_bar(self, string):
    logging.info("Searching for: " + string)
    searchBar = self.find_element(By.ID, 'sb_form_q')
    searchBar.send_keys(Keys.SHIFT + Keys.HOME)
    searchBar.send_keys(string)
    searchBar.send_keys(Keys.ENTER)
