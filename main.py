import time
import threading
from plyer import notification
from playsound import playsound
from datetime import datetime

# Example task list
tasks = [
    {"task": "Study DSA", "time": "20:22", "status": "pending"},
    {"task": "Gym", "time": "16:00", "status": "pending"},
]


def check_tasks():
    while True:
        now = datetime.now().strftime("%H:%M")
        for task in tasks:
            if task['time'] == now and task['status'] == "pending":
                notify_user(task)
        time.sleep(60)  # Check every 60 seconds


def notify_user(task):
    # Show notification
    notification.notify(
        title=f"Task Reminder: {task['task']}",
        message="Time's up! Have you completed it?",
        timeout=10
    )

    # Play notification sound
    playsound("alert.mp3")  # You can use any .mp3 or .wav sound

    # Ask user via terminal (you can later do GUI)
    answer = input(f"\n{task['task']} - Have you completed it? (yes/no/snooze): ").strip().lower()
    if answer == "yes":
        task["status"] = "done"
        print(f"✅ Marked '{task['task']}' as done.")
    elif answer == "snooze":
        # You can implement delay logic
        new_time = (datetime.now() + timedelta(minutes=5)).strftime("%H:%M")
        task["time"] = new_time
        print(f"🔁 Snoozed '{task['task']}' for 5 minutes.")


# Start background thread
threading.Thread(target=check_tasks, daemon=True).start()

# Simulate main app
print("⏳ Task scheduler started. Waiting for reminders...\n")
while True:
    time.sleep(3600)
