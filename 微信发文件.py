import datetime
import time
target_time = datetime.datetime(2023, 2, 13, 17, 18, 11)
current_time = datetime.datetime.now()
while current_time < target_time:
    time_delta = target_time-current_time
    minutes_delta = int(time_delta.seconds/60)
    seconds_delta = time_delta.seconds - int(time_delta.seconds/60)*60
    print("current time:{},   {}:{} left".format(current_time, minutes_delta, seconds_delta))
    if current_time < target_time:

        time.sleep(60)
    current_time = datetime.datetime.now()

import pyautogui
file_pos = pyautogui.locateCenterOnScreen('file.png')
wechat_pos = pyautogui.locateCenterOnScreen('wechat.png')

pyautogui.moveTo(file_pos)

pyautogui.dragTo(wechat_pos, duration=0.5)

pyautogui.click(wechat_pos)
pyautogui.press('enter')
Enter = pyautogui.locateCenterOnScreen('enter.png')
print(Enter)
pyautogui.click(Enter)
pyautogui.press('enter')

