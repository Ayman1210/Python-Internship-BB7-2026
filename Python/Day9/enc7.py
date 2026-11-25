import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()

        total_time = self.end - self.start

        print("Time taken:", total_time, "seconds")


with Timer():
    for i in range(1000000):
        pass