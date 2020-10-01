import psutil
from win10toast import ToastNotifier
import time

battery= psutil.sensors_battery()
plugged=battery.power_plugged
battery_percent=battery.percent

n=1
show=ToastNotifier()
scan_time=60 * 15

while(n==1):
    if plugged:
        n=1
        if battery_percent > 80 :
            show.show_toast("Unplug the Charger","Stop charging your battery to maintain a good battery life", duration=60)
    else:
        if battery_percent < 50 :
            show.show_toast("Battery percentage less than 50" , "Plug in now for a good battery life", duration=60 )

    time.sleep(scan_time)
