import threading
import time


class Countdown(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter
        self.task_completed = False
        self.countdown_expired = False

    def run(self):
        time.sleep(1)
        print("\nDu hast", str(self.counter), "Sekunden um die Aufgabe zu lösen.")
        self.remaining_time(self.counter)
        print("\nCountdown ist vorbei!")
        print("Du bist gefeuert! Drücke beliebige Tast um Spiel zu beenden...")
        self.countdown_expired = True

    def stop_countdown(self):
        self.task_completed = True

    def remaining_time(self, counter):
        while counter:
            if self.task_completed:
                raise SystemExit
            time.sleep(1)
            counter -= 1
