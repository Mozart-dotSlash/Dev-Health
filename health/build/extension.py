# Built using vscode-ext

import sys
import vscode
import datetime
import time

ext = vscode.Extension(name = "testpy", display_name = "Test Py", version = "0.0.1")

@ext.event
def on_activate():
    return f"The Extension '{ext.name}' has started"

@ext.command(keybind="ALT+5")
def Start_Eye_Care():
    res = vscode.window.show_quick_pick(['Yes', 'No'])
    if res == "Yes":
        vscode.window.show_info_message('Select reminder duration')
        time = vscode.window.show_quick_pick(['20 Mins','25 Mins','30 Mins','10 Sec(demo)','None'])
        if time == "20 Mins":
            vscode.window.show_info_message("20 mins Eye relax session enabled")
            call(20*60)
        elif time == "25 Mins":
            vscode.window.show_info_message("25 mins Eye relax session enabled")
            call(25*60)
        elif time == "30 Mins":
            vscode.window.show_info_message("30 mins Eye relax session enabled")
            call(30*60) 
        elif time == "10 Sec(demo)":
            vscode.window.show_info_message("10 sec Demo Eye relax session enabled")
            call(10)
        else:
            vscode.window.show_info_message("Eye care Disabled")


    elif res == "No":
        vscode.window.show_info_message('Okay!')

def call(t):
    time.sleep(t)
    vscode.window.show_warn_message("its been "+str(t)+ " minutes since you've been working, please take rest by closing your eyes for 20 secs :)")
    call(t)



def ipc_main():
    globals()[sys.argv[1]]()

ipc_main()
