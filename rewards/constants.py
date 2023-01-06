from dotenv import load_dotenv
import os

load_dotenv()

EXECUTABLE_PATH = os.getenv('EXECUTABLE_PATH')
PROFILE_NAME = os.getenv('PROFILE_NAME')
PROFILE_PATH = os.getenv('PROFILE_PATH')
