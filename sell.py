from functions import sell
import json


config = json.load(open("config.json"))

sell(f"{config['item']}.PNG", 8)
