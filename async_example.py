from timer import AsyncTimer
import asyncio

async def test():
    timer = AsyncTimer(timeout_secs=5)
    timer.start()
    for i in range(100):
        print("ping")
        await asyncio.sleep(1)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(test())
    loop.run_forever()