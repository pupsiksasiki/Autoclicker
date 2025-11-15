import pyautogui
import time
import threading
import keyboard
import gui
import ctypes
import win32api
import win32con

avtoclicker = False
anti = False
clicks = None
chechszajim = False
zajim = False






# настроики включения авто кликеров
def auto_clicker():
    global avtoclicker
    global clicks
    try:
        if gui.radio2.isChecked():
            colicestva = max(int(gui.stopcik1.text()), 1)
        else:
            colicestva = -1
    except:
        colicestva = -1
 
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
    
    try:
        button = "right" if gui.knopka1.currentText() == "Правая" else "left"
    except:
        button = "right"
    
    while avtoclicker and (clicks < colicestva or colicestva == -1):
        click_type = gui.knopka2.currentText()

        print(interval, clicks)
        print(avtoclicker,zajim)

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


def antiafkdef():
    global anti
    print("LOg anti-afk succees enabled")
    print(anti)
    while anti:
        time.sleep(50) 
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 110, 10, 0, 0)
        
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -110, -10, 0, 0)



# Проверка включения авто кликера =========================================
def check():
    global avtoclicker, click_thread, anti, zajim
    if avtoclicker:
        avtoclicker = False
        anti = False
        print("[Log] Выключение кликов")
    else:
        zajim = False
        avtoclicker = True
        click_thread = threading.Thread(target=auto_clicker, daemon=True)
        click_thread.start()
        print("[Log] Включение кликов")
        #========================================================

        # anti afk ======================
        print("[Log] проверка включения анти афк")
        anti = gui.antiafk.isChecked()
        if anti:
            anti = True
            threading.Thread(target=antiafkdef, daemon=True).start()
            print("[Log] anti afk включен")
        else:
            anti = False
            print("[Log] anti-afk выключен")
        #anti-afk ==================================










# Режим авто-зажима ===========================================

def zajim_click():
    global zajim
    while zajim:
        pyautogui.mouseDown(button="left")
        
def check2():
    global avtoclicker, zajim
    print("[Log] Проверка для режима авто-зажима активирирована")

    
    if gui.sajim.isChecked():
        
        if not zajim:
            zajim = True
            avtoclicker = False
            pyautogui.mouseUp(button="left")
            threading.Thread(target=zajim_click, daemon=True).start()
            print("[Log] авто-зажим активирован")
        else:
            zajim = False
            pyautogui.mouseUp(button="left")
            print("[Log] Авто-зажим был выключен")
    else:
        zajim = False
        pyautogui.mouseUp(button='left')
        print("[Log] Авто зажим не был включен в настроиках")


# ==========================================================================




# горячие клавиши для запуска

def f6():
    keyboard.add_hotkey("f6", check)
    keyboard.wait("f6")
def f7():
    keyboard.add_hotkey("f7", check2)
    keyboard.wait("f7")


threading.Thread(target=f6, daemon=True).start()
threading.Thread(target=f7, daemon=True).start()
