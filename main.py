from turtle import position
import pyautogui as pt
from time import sleep
import random
import pyperclip

sleep(3)

position1 = pt.locateOnScreen("smiley.png" , confidence=.6)
x = position1[0]
y = position1[1]

#Gets Message
def get_message():
    global x, y

    position = pt.locateOnScreen("smiley.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y,duration=.5)
    pt.moveTo(x + 70,y - 40, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message Received: "+ whatsapp_message)

    return whatsapp_message

#Post
def post_response(message):
    global x, y

    position = pt.locateOnScreen("smiley.png", confidence=.6)
    x = position[0]
    y = position[1]

    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)


    pt.typewrite("\n", interval=.01)

#Process Response
def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me any questions!"
    if "Hey" in str(message).lower():
        return "Hey, What's up."
    if "nitaibeba" in str(message).lower():
        return "Fiti Usiisahau."
    if "mnaeza fanya hivo epl" in str(message):
        return "We tulia utaona. Man Utd inarebuild fiti."
    if "birthday" in str(message).lower():
        return "Thanks"
    if "I want to eat" in str(message):
        return "Come Over"
    else:
        if random_no == 0:
            return "That's Cool!"
        elif random_no == 1:
            return "Nice Day"
        else:
            return "I want to eat something."   


processed_message = process_response(get_message())
post_response(processed_message)