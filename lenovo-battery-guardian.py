#!/usr/bin/python3
from systemd import journal
import os
from time import sleep

conservation_mode_file_1 = "/sys/module/legion_laptop/drivers/platform:legion/PNP0C09:00/VPC2004:00/conservation_mode"
conservation_mode_file_2 = "/sys/devices/pci0000:00/0000:00:14.3/PNP0C09:00/VPC2004:00/conservation_mode"

if os.path.exists("/sys/module/legion_laptop/"):
    conservation_mode_file = conservation_mode_file_1
else:
    conservation_mode_file = conservation_mode_file_2

journal.send("Conservation mode file selected"+conservation_mode_file)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def get_battery_capacity():
    return int(read_file('/sys/class/power_supply/BAT0/capacity'))

def is_battery_conservation_mode_on():
    return bool(int(read_file(conservation_mode_file)))

def is_AC_connected():
    return bool(int(read_file('/sys/class/power_supply/ADP0/online')))

def has_capacity_changed(info, prev_info):
    return prev_info != 'init' and prev_info.split('capacity: ')[1][5:] != info.split('capacity: ')[1][5:]

if __name__ == '__main__':
    try:
        journal.send("Battery conservation script started.")
        prev_info = "init"

        while True:
            capacity = get_battery_capacity()
            conservation = is_battery_conservation_mode_on()
            ac_connected = is_AC_connected()
            info = f"capacity: {capacity} | AC: {ac_connected} | conservation: {conservation}"

            if capacity >= 95 and not conservation:
                write_file(conservation_mode_file, '1')  # Stop charging
                journal.send(f"{info} | Battery charging stopped") if has_capacity_changed(info, prev_info) else None

            elif capacity < 95 and conservation:
                write_file(conservation_mode_file, '0')  # Start charging
                journal.send(f"{info} | Enable Battery charging") if has_capacity_changed(info, prev_info) else None

            else:
                journal.send(info) if has_capacity_changed(info, prev_info) else None

            sleep(7 * 60)  # 7 minutes
            prev_info = info

    except KeyboardInterrupt:
        journal.send("Battery conservation script terminated by the user.")
    except Exception as e:
        journal.send("An error occurred: %s", str(e))
