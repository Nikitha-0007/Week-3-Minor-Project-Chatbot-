import time
from threading import Timer

def notify(task):
    print(f"\n🔔 Reminder: {task}")

def set_reminder(task, delay=10):
    Timer(delay, notify, args=[task]).start()
    return f"Reminder set for '{task}' in {delay} seconds."
