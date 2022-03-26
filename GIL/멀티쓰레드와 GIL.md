# Global Interpreter Lock, GIL
## 파이썬의 Multi-Threading
- 파이썬에서는 멀티쓰레딩을 사용해도 각 쓰레드가 동시에 병렬적으로 실행되지 않는다.
- 파이썬에서 멀티쓰레딩을 했을 때, 오히려 성능이 나빠질 수 있다.
- `Global Interpreter Lock (GIL)` 이라는 동기화 방식 때문이다.

<br>

## 동기화를 위한 GIL
파이썬에서 쓰레드를 여러 개 생성한다고 해서 여러 개의 쓰레드가 동시에 실행되는 것은 아니다.
두 개의 쓰레드가 동시에 실행되는 것처럼 보일 뿐이지, 특정 시점에서는 여러 개의 쓰레드 중 하나의 쓰레드만 실행된다. 별도의 동기화 설정을 하지 않았지만, 파이썬 언어가 그렇게 동작하도록 설계되었기 때문이다.
- 하나의 스레드에 모든 자원을 허락하고, 그 후에는 Lock을 걸어 다른 쓰레드 실행을 막는다.
- multi-thread 의 경우 thread context switch 비용으로 single-thread 보다 시간이 오래 걸리는 문제 발생 가능

### `multi-threading.py`
```python3
import random, datetime, threading, time
 
 
def calc():
    max([random.random() for i in range(5000000)])
    max([random.random() for i in range(5000000)])                                 
    max([random.random() for i in range(5000000)])
 
 
# 1 Thread : 하나의 쓰레드에서 두 개의 함수를 연속적으로 실행
start_time = datetime.datetime.now()
calc()
calc()
end_time = datetime.datetime.now()
print(f'1 Thread : {end_time - start_time}')
 
 
# 2 Threads : 쓰레드 두 개를 생성해서 쓰레드에서 각각 하니씩 실행
start_time = datetime.datetime.now()
threads = []
for i in range(2):
    threads.append(threading.Thread(target=calc))
    threads[-1].start()
 
for t in threads:
    t.join()
 
end_time = datetime.datetime.now()
print(f'2 Threads : {end_time - start_time}')
```
- 1 Thread : 0:00:03.978802
- 2 Threads : 0:00:04.352987

<br>

## Why GIL?
파이썬은 `reference count` 방식으로 메모리를 관리한다. 객체를 참조하는 다른 객체 또는 위치가 증가하면 해당 객체의 reference count가 증가하고, reference count가 0이 되면 메모리에서 해제된다.

multi-thread 환경에서 각 쓰레드가 특정 객체를 사용한다면, 파이썬의 특성상 모든 객체에 일일이 Lock을 걸어야만 reference count가 가능할 것이다. 이러한 비효율성을 막기위해서 Global Interpreter Lock을 사용하게 되었다.


<br>

