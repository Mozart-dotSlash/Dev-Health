# Built using vscode-ext

import sys
import vscode
import time

ext = vscode.Extension(name = "movementreminder", display_name = "Movement Reminder", version = "4.3.1")

@ext.event
def on_activate():
    return f"The Extension '{ext.name}' has started"

@ext.command()
def hello_world():
    vscode.window.show_info_message(f'Hello World from {ext.name}')

@ext.command(keybind="ALT+4")
def Movement_Reminder():
    res = vscode.window.show_quick_pick(['Enable sit too long reminder', 'Nope'])
    if res == "Enable sit too long reminder":
        time = vscode.window.show_quick_pick(['30 Mins','10 Sec(demo)'])
        if time == "30 Mins":
            vscode.window.show_info_message("confirm 30 mins movement reminder ","okay")
            call(30*60)
        elif time == "10 Sec(demo)":
            vscode.window.show_info_message("confirm 10 sec Demo movement reminder ","okay")
            call(10)
        else:
            vscode.window.show_info_message("movement reminder Disabled")

    else:
         vscode.window.show_info_message("sit too long disabled")       


def call(t):
    time.sleep(t)
    vscode.window.show_warn_message("You've been sitting for "+ str(t)+"seconds straight, stay healthy while proogramming by taking a 1 minute walk/exercise",'okay!')
    call(t)




def ipc_main():
    globals()[sys.argv[1]]()

ipc_main()
