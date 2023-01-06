from rewards.rewards import Rewards
from essential_generators import DocumentGenerator

import random
import time

try:
  with Rewards() as bot:
    bot.navigate_to_page("https://bing.com")

    try:
      areTherePointsToRedeem = True

      while areTherePointsToRedeem:
        documentGenerator = DocumentGenerator()
        generatedSentence = documentGenerator.sentence()
        
        time.sleep(random.randint(0, 9))

        rewardsPointsBeforeSearch = bot.get_current_rewards_points()
        bot.type_in_search_bar(generatedSentence)

        time.sleep(3)

        if (rewardsPointsBeforeSearch == bot.get_current_rewards_points()):
          break

    except Exception as e:
      raise

    bot.close()

except Exception as e:
  raise