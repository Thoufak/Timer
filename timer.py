import time
import asyncio
from typing import Callable


class Timer:
    def __init__(self, timeout_secs: int, callback: Callable=None):
        assert timeout_secs > 0
        if not callback:
            self.callback = Timer.__raise_timeout_error

        self.timeout_secs = timeout_secs
        self.start_time = None

    @staticmethod
    def __raise_timeout_error():
        raise TimeoutError()

    def start(self):
        self.start_time = time.time()

    def validate(self):
        if not self.start_time:
            print("Timer error: validate() called before calling start()")
            return
        now = time.time()
        if now - self.start_time > self.timeout_secs:
            self.callback()


class AsyncTimer(Timer):
    def start(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.__start())
        if not loop.is_running():
            print("Timer error: no running asyncio loop found")
            loop.run_forever()

    async def __start(self):
        await asyncio.sleep(self.timeout_secs)
        self.callback()
