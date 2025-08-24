import pyautogui
import time
import threading
import keyboard
import gui
import ctypes
import win32api
import win32con

avtoclicker = False
clicks = None

def auto_clicker():
    global avtoclicker
    global clicks
    #тута получение кол кликов
    try:
        if gui.radio2.isChecked():
            colicestva = max(int(gui.stopcik1.text()), 1)
        else:
            colicestva = -1
    except:
        colicestva = -1
    #тута получение интервала
    try:
        ms = int(gui.muzic_ms.text()) if gui.muzic_ms.text() != "" else 0
    except:
        ms = 0
    try:
        sec = int(gui.muzic_sec.text()) if gui.muzic_sec.text() != "" else 0
    except:
        sec = 0
    try:
        min_ = int(gui.muzic_min.text()) if gui.muzic_min.text() != "" else 0
    except:
        min_ = 0
    try:
        hour = int(gui.muzic_hour.text()) if gui.muzic_hour.text() != "" else 0
    except:
        hour = 0
    interval = ms/1000 + sec + min_*60 + hour*3600

    try:
        kps = max(int(gui.kps_input.text()), 1)
    except:
        kps = 10
        print("Log 10cps")

    kps_interval = 1/kps  

    clicks = 0
    #тута  кароче получение кнопки мыши
    try:
        button = "right" if gui.knopka1.currentText() == "Правая" else "left"
    except:
        button = "right"
    # тут думаю понтно
    while avtoclicker and (clicks < colicestva or colicestva == -1):
        click_type = gui.knopka2.currentText()

        print(interval, clicks)

        if click_type == "Одиночный":
            pyautogui.click(button=button)
            clicks +=1
            time.sleep(interval)
        elif click_type == "Двойной":
            pyautogui.doubleClick(button=button)
            clicks +=1
            time.sleep(interval)
        else:
            if button == "left":
                najat = win32con.MOUSEEVENTF_LEFTDOWN
                najat2 = win32con.MOUSEEVENTF_LEFTUP
                win32api.mouse_event(najat, 0, 0, 0, 0)
                win32api.mouse_event(najat2, 0, 0, 0, 0)
                clicks += 1
                time.sleep(kps_interval)  

            else:
                najat = win32con.MOUSEEVENTF_RIGHTDOWN
                najat2 = win32con.MOUSEEVENTF_RIGHTUP
                win32api.mouse_event(najat, 0, 0, 0, 0)
                win32api.mouse_event(najat2, 0, 0, 0, 0)
                clicks += 1
                time.sleep(kps_interval)  

    avtoclicker = False

def check():
    global avtoclicker, click_thread
    if avtoclicker:
        avtoclicker = False
    else:
        avtoclicker = True
        click_thread = threading.Thread(target=auto_clicker, daemon=True)
        click_thread.start()

def f6():
    keyboard.add_hotkey("f6", check)
    keyboard.wait("f6")

threading.Thread(target=f6, daemon=True).start()