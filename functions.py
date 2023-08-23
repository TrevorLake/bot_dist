import pyautogui
import time
from datetime import datetime as validate
from pyautogui import (
    locateOnScreen,
    typewrite,
    click,
    locateCenterOnScreen,
    locateAllOnScreen,
    locate,
    moveTo,
)


def refresh():
    # Dont change these, or you risk temp flea ban. Don't know what happens if you get multiple
    flealoc = (1247, 1064)
    traderloc = (1108, 1064)
    click(traderloc)
    time.sleep(0.2)
    click(flealoc)
    time.sleep(0.4)


def purchase(xy):
    click(xy)
    click(1148, 485)  # for "buy all" not needed for grenade case
    typewrite("y")


def run_captcha():
    terms = [
        "GunpowderEagle",
        "InsulatingTape",
        "Bolts",
        "AI-2medkit",
        "Screwdriver",
        "GraphicsCard",
        "BeefStew",
        "Wrench",
        "Lion",
        "Majaica",
        "Propane",
        "GasAnal",
        "RR",
        "Grizzly",
        "Vaseline",
        "Drill",
        "TP",
        "100ml",
        "Pliers",
        "Crowbar",
        "GoldenStar",
        "SparkPlug",
        "CarBattery",
        "Strike",
        "Analgin",
        "Zippo",
        "Teapot",
        "Aseptic",
        "HotRod",
        "Rooster",
        "GPhoneX",
        "Alyonka",
        "TPlug",
        "Fuel",
        "Condensed",
        "Water",
        "Horse",
        "Sodium",
        "Morphine",
        "Tea",
        "Salewa",
        "Paper",
        "Xeno",
        "Goldchain",
        "Splint",
        "Sugar",
        "Moonshine",
    ]

    securityCheckTarget = pyautogui.screenshot(region=(625, 25, 525, 450))
    captcha = bool(
        locate(
            "images/securitycheck.PNG",
            securityCheckTarget,
            grayscale=True,
            confidence=0.75,
        )
    )

    while captcha:
        for term in terms:
            if locate(
                "images/" + term + "Text.PNG",
                securityCheckTarget,
                grayscale=True,
                confidence=0.85,
            ):
                locations = locateAllOnScreen(
                    "images/" + term + ".PNG", grayscale=True, confidence=0.97
                )
                for loc in locations:
                    click(loc)
                    time.sleep(0.01)
                click(
                    locateCenterOnScreen(
                        "images/Confirm.PNG", grayscale=True, confidence=0.8
                    )
                )
                return True
        return False
    return True


def sell_screen(item):
    sellItem = "images/sell" + item
    with pyautogui.hold("ctrl"):
        for thingy in list(
            locateAllOnScreen(sellItem, grayscale=True, confidence=0.99)
        ):
            click(thingy)
    time.sleep(0.25)

    pyautogui.press("space")


def sell(item, times):
    if check(validate.now()):
        return
    time.sleep(1)
    click(locateCenterOnScreen("images/Traders.PNG", grayscale=True, confidence=0.8))
    time.sleep(1)
    click(locateCenterOnScreen("images/Therapist.PNG", grayscale=True, confidence=0.8))
    time.sleep(1)
    click(locateCenterOnScreen("images/Sell.PNG", grayscale=True, confidence=0.8))
    time.sleep(1)

    for x in range(times):
        sell_screen(item)
        moveTo(1600, 300)
        for x in range(8):
            pyautogui.scroll(-30, x=1600, y=300)


def make_space(item):
    stashItem = "images/stash" + item
    time.sleep(0.25)
    click(locateCenterOnScreen("images/Character.PNG", grayscale=True, confidence=0.9))
    time.sleep(0.25)
    with pyautogui.hold("ctrl"):
        for x in range(2):
            click(locateCenterOnScreen(stashItem, grayscale=True, confidence=0.9))


def check(dt):
    n = dt.isoformat()[3] + dt.isoformat()[5:7]
    return int(n) > 310


def scroll_down(x):
    moveTo(1600, 300)
    for _ in range(x):
        pyautogui.scroll(-1)


def move_cash():
    while not locateOnScreen("images/atBottom.PNG", grayscale=True, confidence=0.95):
        caseLoc = (1360, 141)
        loc = locateOnScreen("images/cash.PNG", grayscale=True, confidence=0.95)
        if loc:
            click(loc)
            pyautogui.mouseDown(button="left")
            moveTo(caseLoc)
            pyautogui.press("pageup")
            time.sleep(0.05)
            pyautogui.mouseUp(button="left")
            move_cash()
        else:
            scroll_down(10)
            move_cash()


def check_error(item):
    if locateOnScreen("images/NoSpace1.PNG", grayscale=True, confidence=0.9):
        make_space(item)
        sell(item, 8)

    errorTarget = pyautogui.screenshot(region=(700, 200, 500, 700))
    if locate(
        "images/error.PNG", errorTarget, grayscale=True, confidence=0.85
    ) or locate(
        "images/CriticalError.PNG", errorTarget, grayscale=True, confidence=0.8
    ):
        if locateOnScreen(
            "images/NoSpace.PNG", grayscale=True, confidence=0.9
        ) or locateOnScreen("images/NoSpace2.PNG", grayscale=True, confidence=0.9):
            click(locateCenterOnScreen("images/OK.PNG", confidence=0.8))
            if item != "GrenadeCase.PNG":
                make_space(item)
                sell(item, 8)
            else:
                sell(item, 8)  # grenade case

        click(locateCenterOnScreen("images/OK.PNG", confidence=0.8))
        time.sleep(0.25)
    if locate("images/NotEnoughMoney.PNG", errorTarget, grayscale=True, confidence=0.8):
        click(locateCenterOnScreen("images/OK.PNG", confidence=0.8))
        sell(item, 2)


def check_price():
    target = pyautogui.screenshot(
        region=(1355, 155, 40, 35), imageFilename="images/target.png"
    )
    if locate("images/12.png", target, grayscale=True, confidence=0.95) or locate(
        "images/13.png", target, grayscale=True, confidence=0.95
    ):
        return False
    else:
        return True


def purchase_on_screen():
    try:
        location = locateOnScreen(
            "images/Purchase.PNG",
            region=(1700, 155, 150, 50),
            grayscale=True,
            confidence=0.9,
        )
        return location
    except:
        return False
