from datetime import datetime
from threading import Timer

MIN_GYM_TIME_MIN = 30
MAX_GYM_TIME_MIN = 180
last_trigger_time = None

def trigger_gym_geofence():
    trigger_time = datetime.now()

    if last_trigger_time is None:
        last_trigger_time = trigger_time
        return "Entrance has been recorded"

    delta = trigger_time - last_trigger_time

    if delta.total_seconds() > MAX_GYM_TIME_MIN * 60:
        last_trigger_time = trigger_time
        return "Time difference is too large"
    elif delta.total_seconds() > MIN_GYM_TIME_MIN * 60:
        open_box()
        last_trigger_time = trigger_time
        return "The box has been opened"
    else:
        return "Work out more"

def reset_box():
    close_box()
    last_trigger_time = None

    return "Box has been reset"

def open_box():
    print("Opening the box!")

def close_box():
    print("Closing the box!")

