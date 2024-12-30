import threading
import time
counter = 0
counter_lock = threading.Lock()
class SimpleTask:
    def run_task(self):
        global counter
        for _ in range(3):
            time.sleep(2)
        with counter_lock:
            counter += 1
        print(f"Counter đã tăng lên: {counter}")
def main():
    tasks = [threading.Thread(target=SimpleTask().run_task) for _ in range(4)]
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()
if __name__ == "__main__":
    main()