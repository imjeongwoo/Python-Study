from time import time


import time
import asyncio


async def delivery(name, meal_time):
    print(f"{name}에게 배달 완료.")
    await asyncio.sleep(meal_time)
    print(f"{name} 식사 완료, {meal_time}시간 소요..")
    print(f"{name} 그릇 수거 완료")


async def main():
    await asyncio.gather(
        delivery("A", 5),
        delivery("B", 3),
        delivery("C", 4),
    )


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)