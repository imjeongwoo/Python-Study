# 동기(Sync)와 비동기(Async) 코드 비교

동기(Sync)
```python
import time


def delivery(name, meal_time):
    print(f"{name}에게 배달 완료.")
    time.sleep(meal_time)
    print(f"{name} 식사 완료, {meal_time}시간 소요..")
    print(f"{name} 그릇 수거 완료")


def main():
    delivery("A", 3)
    delivery("B", 3)
    delivery("C", 4)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)

"""
A에게 배달 완료.
A 식사 완료, 5시간 소요..
A 그릇 수거 완료
B에게 배달 완료.
B 식사 완료, 3시간 소요..
B 그릇 수거 완료
C에게 배달 완료.
C 식사 완료, 4시간 소요..
C 그릇 수거 완료
12.006293058395386
"""
```
- A, B, C 식사 완료를 차례대로 기다리며 실행

<br>

비동기(Async)
```python
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
        delivery("A", 10),
        delivery("B", 3),
        delivery("C", 4),
    )


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)

"""
A에게 배달 완료.
B에게 배달 완료.
C에게 배달 완료.
B 식사 완료, 3시간 소요..
B 그릇 수거 완료
C 식사 완료, 4시간 소요..
C 그릇 수거 완료
A 식사 완료, 5시간 소요..
A 그릇 수거 완료
5.003593921661377
"""
```
- 배달하고 식사 완료를 기다리지 않음
- 코드가 반드시 **작성된 순서 그대로 실행되는 것이 아님**
- `asyncio.gather()` : 어웨이터블 객체를 동시에 실행
    - 동시에 태스크를 실행
    - 각각의 결과값이 `list`로 반환

<br><br>

## 알반적인 함수를 코루틴으로 (async/await 키워드 사용)
<br>

일반적인 함수
```python
def hello():
    print("hello")
    return 123

if __name__ == "main":
    print(hello())
```
<br>

async/await 키워드 사용 (Error)
```python
async def hello():
    print("hello")
    return 123

if __name__ == "main":
    await hello()

"""
  File "main.py", line 24
    await hello()
    ^
SyntaxError: 'await' outside function
"""
```
- `await` 키워드는 코루틴(`async`) 안에서 사용 !!

<br>

`asycio.run()` 으로 실행
```python
async def hello():
    print("hello")
    return 123

if __name__ == "__main__":
    asyncio.run(hello())
```
- `asyncio.run()` : 코루틴을 실행하고 결과 반환
<br><br>

## awaitable 객체
- await 표현식에서 사용될 수 있는 객체
- 코루틴(Coroutine), 태스크(Task), 퓨처(Future)

<br>

## 태스크(Task)
- 코루틴을 동시에 예약하는 데 사용
```python
import asyncio

async def nested():
    return 42

async def main():
    task = asyncio.create_task(nested())
    # 변수에 예약된 작업을 담고
    
    await task
    # 나중에 실행 가능
    # await nested() 와 같음

asyncio.run(main())
```
<br>

## 퓨처(Future)
- 저수준 awaitable 객체
- 비동기 연산의 최종 결과를 나타냄
- 보통 멀티 쓰레딩/프로세싱에서 사용

<br><br>