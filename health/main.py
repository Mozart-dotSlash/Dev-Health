import vscode
import datetime
import time

ext = vscode.Extension(name = "eye-care", display_name = "Eye Care", version = "4.3.1")

@ext.event
def on_activate():
    return f"The Extension '{ext.name}' has started"



@ext.command(keybind="ALT+5")
def Start_Eye_Care():
    res = vscode.window.show_quick_pick(['Enable', 'Nope! Had a change of mind :()'],)
    if res == "Enable":
        global time_set = 0
        time = vscode.window.show_quick_pick(['20 Mins','25 Mins','30 Mins','10 Sec(demo)','None'])
        if time == "20 Mins":
            vscode.window.show_info_message("Confirm 20 mins Eye relax session ", "okay")
            time_set = "20"
            call(20*60)
        elif time == "25 Mins":
            vscode.window.show_info_message("Confirm 25 mins Eye relax session ", "okay")
            time_set = "25"
            call(25*60)
        elif time == "30 Mins":
            vscode.window.show_info_message("Confirm 30 mins Eye relax session ", "okay")
            time_set = "30"
            call(30*60) 
        elif time == "10 Sec(demo)":
            vscode.window.show_info_message("Confirm 10 sec(demo) Eye relax session ", "okay")
            time_set = "10"
            call(10)
        else:
            vscode.window.show_info_message("Eye care Disabled")


    elif res == "Nope! Had a change of mind :()":
        vscode.window.show_info_message('Okay!')

def call(t):
    time.sleep(t)
    global time_set
    vscode.window.show_warn_message("its been "+time_set+ " minutes since you've been working, please take rest by closing your eyes for 20 secs :)","okay")
    call(t)

vscode.build(ext)
