from functions import *
import json

config = json.load(open("config.json"))


def main(item):
    time.sleep(1)
    bought = 0
    while True:
        purch_loc = purchase_on_screen()
        purch_loc = purchase_on_screen()
        if purch_loc:
            purchase(purch_loc)
            bought += 1
            if bought > 75:
                sell(item, 8)
                bought = 0
        check_error(item)  # sell() and make_room() handled here
        run_captcha()
        refresh()


if __name__ == "__main__":
    main(f"{config['item']}.PNG")
