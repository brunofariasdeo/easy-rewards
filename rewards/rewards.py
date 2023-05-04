import logging
import random
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from essential_generators import DocumentGenerator
import rewards.constants as constants


class Rewards(webdriver.Edge):
    def __init__(self, headless=False):
        self.points_to_redeem = True
        self.tasks_to_click = True
        options = Options()
        # The argument "--headless" is currently not working due to a Chrome Webdriver bug,
        # as per https://github.com/SeleniumHQ/selenium/issues/11634
        options.add_argument("headless=new" if headless else "None")
        options.add_argument("--mute-audio")
        options.add_argument(f"user-data-dir={constants.PROFILE_PATH}")
        options.add_argument(f"profile-directory={constants.PROFILE_NAME}")

        service = Service(executable_path=constants.EXECUTABLE_PATH)
        super(Rewards, self).__init__(options=options, service=service)

    def find_available_tasks(self):
        logging.info("Finding available tasks")
        try:
            while self.tasks_to_click:
                available_task = self.find_element(
                    By.XPATH, '//div[contains(@class, "rewards-card-container")]//span[contains(@class, "AddMedium")]'
                )
                available_task.click()
                logging.info("Element found. Clicked on it.")

                time.sleep(5)

                self.switch_page_to_home()
        except NoSuchElementException:
            logging.info("You've already completed all tasks. Moving on.")
            self.tasks_to_click = False

    def find_login_button(self):
        time.sleep(5)

        try:
            authenticate_button = self.find_element(By.XPATH, '//a[contains(text(), "Entrar")]')

            if len(authenticate_button) > 0:
                logging.info("Authenticating.")
                authenticate_button.click()
        except Exception:
            logging.info("Login button not found.")
            time.sleep(5)

    def get_current_rewards_points(self):
        try:
            return self.find_element(By.ID, "id_rc").text
        except Exception as exception:
            print(exception)

            logging.info("Could not retrieve rewards points.")
            self.take_a_screenshot()
            time.sleep(5)

    def navigate_to_page(self, url):
        logging.info("Navigating to page: %s", url)
        self.get(url)
        time.sleep(5)

    def play_a_game(self, game_name):
        self.navigate_to_page("https://www.xbox.com/pt-BR/play")
        logging.info("Opening Xbox Cloud.")

        xbox_cloud_logo_xpath = '//button[contains(@class, "XboxButton")]'
        self.wait_for_element(xbox_cloud_logo_xpath)

        self.find_login_button()

        try:
            game = self.find_element(
                By.XPATH, f'//button//div[contains(text(), "{game_name}")]/ancestor::div[contains(@class, "BaseItem")]'
            )
            game.click()
            logging.info("Game found. Clicked on it.")

            time.sleep(5)

            confirm_button = self.find_element(By.XPATH, '//button[contains(text(), "Continuar mesmo assim")]')
            confirm_button.click()
            logging.info("Confirm button found. Clicked on it.")
            logging.info("%s will be running for 10 minutes. This page will be closed once finished.", game_name)

            time.sleep(600)
        except Exception as exception:
            print(exception)

            self.take_a_screenshot()
            logging.info("Game not found. Moving on.")

    def search_on_bing(self):
        self.navigate_to_page("https://bing.com")

        logging.info("Starting Bing search.")
        document_generator = DocumentGenerator()

        try:
            number_of_attempts = 0

            while self.points_to_redeem:
                generated_sentence = document_generator.sentence()

                time.sleep(random.randint(0, 9))

                rewards_points_before_search = self.get_current_rewards_points()
                logging.info("You currently have %s points.", rewards_points_before_search)

                truncated_sentence = generated_sentence[:10]
                self.type_in_search_bar(truncated_sentence)
                time.sleep(5)

                if rewards_points_before_search == self.get_current_rewards_points():
                    number_of_attempts += 1

                if rewards_points_before_search == self.get_current_rewards_points() and number_of_attempts == 3:
                    logging.info("You've already completed all searches. Moving on.")
                    self.points_to_redeem = False
        except Exception as exception:
            print(exception)

            self.take_a_screenshot()
            logging.error("Error while trying to search on Bing.")
            time.sleep(2)

    def switch_page_to_home(self):
        logging.info("Going back to the previous page.")
        window_name = self.window_handles[0]

        self.switch_to.window(window_name=window_name)

        time.sleep(5)

    def take_a_screenshot(self):
        logging.info("Taking a browser screenshot...")
        self.save_screenshot("./logs/rewards" + time.strftime("%Y%m%d-%H%M%S") + ".png")

    def type_in_search_bar(self, string):
        logging.info("Searching for: %s", string)
        search_bar = self.find_element(By.ID, "sb_form_q")
        search_bar.send_keys(Keys.SHIFT + Keys.HOME)
        search_bar.send_keys(string)
        search_bar.send_keys(Keys.ENTER)

    def wait_for_element(self, element):
        logging.info("Waiting for page to be loaded")
        WebDriverWait(self, 10).until(EC.presence_of_element_located((By.XPATH, element)))
