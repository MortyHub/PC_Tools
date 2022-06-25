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
    if l1 > 90.0:
        with open("Watcher/data/past_causes.txt", "a+") as f:
            f.write(f'{l1}\n')
            f.close()
        notification.notify(
            title = "Watcher",
            message = f"Your PC Is Overloading With CPU Takeup {l1}%"
        )
    time.sleep(.01)