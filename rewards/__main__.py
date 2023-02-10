import logging
from rewards.rewards import Rewards
import time
import typer

app = typer.Typer()

@app.command()
def run():
  try:
    with Rewards() as bot:

      try:
        bot.navigate_to_page('https://rewards.bing.com/')
        bot.find_available_tasks()

        time.sleep(5)

        bot.search_on_bing()

        time.sleep(5)

        bot.play_a_game("Fortnite")

      except Exception as e:
        raise

      bot.close()

  except Exception as e:
    raise

@app.command()
def find_available_tasks():
  try:
    with Rewards() as bot:

      try:
        bot.navigate_to_page('https://rewards.bing.com/')
        bot.find_available_tasks()
      except Exception as e:
        raise

      bot.close()

  except Exception as e:
    raise

@app.command()
def play_a_game():
  try:
    with Rewards() as bot:

      try:
        bot.play_a_game("Fortnite")
      except Exception as e:
        raise

      bot.close()

  except Exception as e:
    raise

@app.command()
def search_on_bing():
  try:
    with Rewards() as bot:

      try:
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
  app()
  logging.info("Bot finished")