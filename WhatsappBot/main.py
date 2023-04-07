import pyautogui as py
import time

limit = input("limit: ")
message = "kral iyi ki varsın"
i = 0

time.sleep(5)

while i < int(limit):
    py.typewrite(message)
    py.press("enter")
    i+=1


