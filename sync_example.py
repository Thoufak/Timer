from timer import Timer
import time

def test():
    timer = Timer(timeout_secs=5)
    timer.start()
    for i in range(100):
        print("ping")
        time.sleep(1)
        timer.validate()

if __name__ == '__main__':
    test()