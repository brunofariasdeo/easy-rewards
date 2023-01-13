import logging
from rewards.rewards import Rewards
import time

def run_bot():
  try:
    with Rewards() as bot:

      try:
        bot.navigate_to_page('https://rewards.bing.com/')
        bot.find_available_tasks()

        time.sleep(5)

        bot.search_on_bing()

      except Exception as e:
        raise

      bot.close()

  except Exception as e:
    raise

def setup_logging():
  logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
  )

if __name__ == "__main__":
  setup_logging()

  logging.info("Bot started")
  run_bot()
  logging.info("Bot finished")
