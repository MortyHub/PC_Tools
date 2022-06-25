from plyer import notification
import psutil, time

notification.notify(
    title = 'Watcher',
    message = 'Watching For Spikes',
    app_icon = None,
    timeout = 3,
)

while True:
    l1 = psutil.cpu_percent()
    notification.notify(
            title = "Watcher",
            message = f"Your PC Is Overloading With CPU Takeup {l1}%, close some apps"
    )
    time.sleep(.01)