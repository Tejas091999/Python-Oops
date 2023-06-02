import time
from plyer import notification
print("Welcome to water reminder")
def reminder():
  while True:
    notification.notify(
      title="Drink Water",
      message="It's time to drink water",
      timeout=10
    )
    time.sleep(1800)
reminder()