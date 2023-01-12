from rewards.rewards import Rewards

import time

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
