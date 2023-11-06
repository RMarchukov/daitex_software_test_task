import json
import os
from dotenv import load_dotenv

load_dotenv()

PROGRAM_NAME = os.environ.get("PROGRAM_NAME")
settings = {"PROGRAM_NAME": PROGRAM_NAME}

with open('../settings.json', 'w') as json_file:
    json.dump(settings, json_file, indent=4)
