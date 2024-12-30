import time
class SimpleTask:
    def run_task(self):
        for i in range(1, 11):
            print('Đã in lần thứ :',i)
time.sleep(2) # Dừng 2 giây giữa mỗi lần in
def main():
    task = SimpleTask()
    task.run_task()
if __name__ == "__main__":
    main()