import logging
import time
import os
import typer
from rewards.rewards import Rewards

app = typer.Typer()


@app.command()
def run(headless: bool = typer.Option(False, "--headless")):
    try:
        with Rewards(headless) as bot:
            try:
                bot.navigate_to_page("https://rewards.bing.com/")
                bot.find_available_tasks()

                time.sleep(5)

                bot.search_on_bing()

                time.sleep(5)

                bot.play_a_game("Fortnite")

            except Exception as exception:
                print(exception)
                raise

            bot.close()

    except Exception as exception:
        print(exception)
        raise


@app.command()
def find_available_tasks(headless: bool = typer.Option(False, "--headless")):
    try:
        with Rewards(headless) as bot:
            try:
                bot.navigate_to_page("https://rewards.bing.com/")
                bot.find_available_tasks()
            except Exception as exception:
                print(exception)
                raise

            bot.close()

    except Exception as exception:
        print(exception)
        raise


@app.command()
def play_a_game(headless: bool = typer.Option(False, "--headless")):
    try:
        with Rewards(headless) as bot:
            try:
                bot.play_a_game("Fortnite")
            except Exception as exception:
                print(exception)
                raise

            bot.close()

    except Exception as exception:
        print(exception)
        raise


@app.command()
def search_on_bing(headless: bool = typer.Option(False, "--headless")):
    try:
        with Rewards(headless) as bot:
            try:
                bot.search_on_bing()
            except Exception as exception:
                print(exception)
                raise

            bot.close()

    except Exception as exception:
        print(exception)
        raise


def setup_logging():
    if not os.path.exists("./logs/"):
        os.makedirs("./logs/")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s:%(message)s",
        handlers=[logging.FileHandler("./logs/logs.txt"), logging.StreamHandler()],
    )


if __name__ == "__main__":
    setup_logging()
    logging.info("Bot started")
    app()
    logging.info("Bot finished")
