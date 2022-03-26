## 메인 루틴과 서브 루틴의 동작 (일반적인 함수)
```python
# subroutine.py
def 서브루틴(a, b):
    print('서브 루틴 시작')
    c = a + b
    print(f'c = {c}, 서브 루틴 종료')

def 메인루틴():
    print('메인 루틴 시작')
    서브루틴(1, 2)
    print('메인 루틴 다시 시작')

메인루틴()   

'''
메인 루틴 시작
서브 루틴 시작
c = 3, 서브 루틴 종료
메인 루틴 다시 시작
'''
```

![image](https://user-images.githubusercontent.com/57474572/158195880-45ec9ba4-d905-40b2-9d93-44999e934158.png)

    1. 메인 루틴에서 서브 루틴 호출
    2. 서브 루틴 실행
    3. 서브 루틴이 끝나고 메인 루틴 복귀

    - 서브 루틴이 끝나면 서브 루틴의 내용은 모두 사라짐
    - 서브 루틴은 메인 루틴에 종속된 관계

<br>

## 메인 루틴과 코루틴의 동작
![image](https://user-images.githubusercontent.com/57474572/158199387-81918d3b-2bcc-441a-86f9-a54a699fe308.png)

    코루틴은 함수가 종료되지 않은 상태에서 메인 루틴의 코드를 실행한 뒤 다시 돌아와서 코루틴의 코드를 실행함.
    -> 코루틴이 종료되지 않았으므로 코루틴의 내용도 계속 유지됨.

    일반적인 함수를 호출하면 코드를 한 번 실행할 수 있지만, 코루틴은 여러 번 실행 가능.
    -> 코루틴은 진입점이 여러개인 함수이다.

<br>

## 코루틴에 값 보내기
> 코루틴은 제너레이터(Generator)의 특별한 형태이다.

- 제너레이터는 `yield`로 값을 발생시켰지만 **코루틴은 `yield`로 값을 받아올 수 있다.**<br>
- 코루틴에 값을 보내면서 코드를 실행할 때는 `send()` 메서드를 사용한다.<br>
- `send()`가 보낸 값을 받아오려면 `(yield)`로 변수에 저장한다.
```python
# coroutine_consumer.py
def number_coroutine():
    while True:        # 코루틴을 유지하기 위해 무한 루프 사용
        x = (yield)    # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶기
        print(x)
 
co = number_coroutine()
next(co)      # 코루틴 안의 yield까지 코드 실행(최초 실행)
 
co.send(1)    # 코루틴에 숫자 1을 보냄
co.send(2)    # 코루틴에 숫자 2을 보냄
co.send(3)    # 코루틴에 숫자 3을 보냄

'''
1
2
3
'''
```
![image](https://user-images.githubusercontent.com/57474572/158216937-d65491f1-9138-4ea0-8f2e-5c346878ad5f.png)
1. `next()`로 코루틴의 코드를 최초로 실행
2. `yield`에서 대기
3. 메인 루틴에서 `send()`로 값을 보내면, 코루틴에서 값을 받아 `x`에 저장후 `x` 출력
4. **2, 3번 과정**을 반복

<br>

## 코루틴 밖으로 값 전달하기
- `(yield 변수)` : 값을 받아오면서 밖으로 값을 전달
- 외부로 전달된 값은 `next()`와 `send()` 메서드의 반환값으로 나옴
```python
# coroutine_producer_consumer.py
def sum_coroutine():
    total = 0
    while True:
        x = (yield total)    # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        total += x
 
co = sum_coroutine()
print(next(co))      # 0: 코루틴 안의 yield까지 코드를 실행하고 코루틴에서 나온 값 출력
 
print(co.send(1))    # 1: 코루틴에 숫자 1을 보내고 코루틴에서 나온 값 출력
print(co.send(2))    # 3: 코루틴에 숫자 2를 보내고 코루틴에서 나온 값 출력
print(co.send(3))    # 6: 코루틴에 숫자 3을 보내고 코루틴에서 나온 값 출력

'''
0
1
3
6
'''
```
1. `next(co)`로 코루틴 최초 실행
2. 코루틴에서 `total`을 메인 루틴으로 전달 후 `yield`에서 대기
3. 메인 루틴에서 최초로 전달 받은 `total` 값 **0 출력**
4. `send(1)`로 1을 보냄
5. 코루틴은 대기 상태에서 풀리고 `x = (yield total)`의 `x`에 전달 받은 1을 저장
6. `total += x` 코드 실행, `total`은 1
7. 코루틴은 `total`을 메인 루틴으로 전달 후 `yield`에서 대기
8. 메인 루틴에서 전달 받은 `total` 값 **1 출력**
9. `send(2)`로 2을 보냄
10. 코루틴은 대기 상태에서 풀리고 `x = (yield total)`의 `x`에 전달 받은 2을 저장
11. `total += x` 코드 실행, `total`은 3
12. 코루틴은 `total`을 메인 루틴으로 전달 후 `yield`에서 대기
13. 메인 루틴에서 전달 받은 `total` 값 **3 출력**
14. `send(3)`로 3을 보냄
15. 코루틴은 대기 상태에서 풀리고 `x = (yield total)`의 `x`에 전달 받은 3을 저장
16. `total += x` 코드 실행, `total`은 6
17. 코루틴은 `total`을 메인 루틴으로 전달 후 `yield`에서 대기
18. 메인 루틴에서 전달 받은 `total` 값 **6 출력**

> `yield`를 사용하여 코루틴 밖으로 값을 전달하면 `next`와 `send`의 반환값으로 받는다!!

<br>

## 코루틴 종료

    보통 코루틴은 실행 상태를 유지하기 위해 무한 루프로 동작.
    만약 코루틴을 강제로 종료하고 싶으면?
    -> close() 메서드를 사용.
```python
# coroutine_close.py
def number_coroutine():
    while True:
        x = (yield)
        print(x, end=' ')
 
co = number_coroutine()
next(co)
 
for i in range(20):
    co.send(i)
 
co.close()    # 코루틴 종료

'''
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
'''
```
- 사실 스크립트가 끝나면 코루틴도 같이 끝나기 때문에 `close()`를 사용하지 않는 것과 별 차이가 없음
- 그렇다면 `close()`가 발생하면 어떤 일이 벌어질까?

<br>

## GeneratorExit 예외 처리

    코루틴 객체에서 close() 메서드를 호출하면 코루틴이 종료될 때 GeneratorExit 예외가 발생.
    이 예외를 처리하면 코루틴의 종료 시점을 알 수 있음.
```python
# coroutine_generator_exit.py
def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x, end=' ')
    except GeneratorExit:    # 코루틴이 종료 될 때 GeneratorExit 예외 발생
        print('\n코루틴 종료')
 
co = number_coroutine()
next(co)
 
for i in range(20):
    co.send(i)
 
co.close()

'''
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 
코루틴 종료
'''
```
- `close()` 메서드로 코루틴을 종료할 때 원하는 코드를 실행 가능

<br>

## 코루틴 안에서 특정 예외 발생시키기

    코루틴 안에 예외를 발생시킬 때는 throw 메서드를 사용함.
    throw 메서드에 지정한 에러 메시지는 except as의 변수에 들어감.
```python
# coroutine_throw.py
def sum_coroutine():
    try:
        total = 0
        while True:
            x = (yield)
            total += x
    except RuntimeError as e:
        print(e)       # 에러 메시지 출력
        yield total    # 코루틴 바깥으로 값 전달
 
co = sum_coroutine()
next(co)
 
for i in range(20):
    co.send(i)
 
print(co.throw(RuntimeError, '예외로 코루틴 끝내기')) # 190 (누적된 코루틴 값)

'''
예외로 코루틴 끝내기
190
'''
```
- 코루틴에서 숫자를 보내서 누적하다가 `RuntimeError` 예외가 발생
- 에러 메시지를 출력하고 누적된 값을 코루틴 바깥으로 전달

<br>

## 하위 코루틴의 반환값 가져오기

    제너레이터에서 yield from을 사용하면 값을 바깥으로 여러 번 전달한다.
    하지만 코루틴에서 yield from에 코루틴을 지정하면 해당 코루틴에서 return 값을 가져온다.
```python
# coroutine_yield_from.py
def accumulate():
    total = 0
    while True:
        x = (yield)         # 코루틴 바깥에서 값을 받아옴
        if x is None:       # 받아온 값이 None이면
            return total    # 합계 total을 반환
        total += x
 
def sum_coroutine():
    while True:
        total = yield from accumulate()    # accumulate의 반환값을 가져옴
        print(total)
 
co = sum_coroutine()
next(co)
 
for i in range(1, 11):    # 1부터 10까지 반복
    co.send(i)            # 코루틴 accumulate에 숫자를 보냄
co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄
 
for i in range(1, 101):   # 1부터 100까지 반복
    co.send(i)            # 코루틴 accumulate에 숫자를 보냄
co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄

'''
50
5050
'''
```
- 숫자를 받아서 누적할 코루틴 `accumulate()`은 밖에서 값을 받아온 뒤 `total`에 계속 누적
- 무한 루프로 동작하지만 조건문으로 `total`을 반환하고 코루틴을 종료
- 합을 출력할 코루틴 `sum_coroutine()`에서 `yield from`으로 `accumulate()`의 반환값을 가져옴
    - **코루틴에서 `yield from`을 사용하면 코루틴 바깥에서 `send()`로 하위 코루틴까지 값을 보낼 수 있음**
    - `co = sum_coroutine()`으로 코루틴 객체를 생성하고 `co.send()`로 값을 보내면 `accumulate()`에서 값을 받음
    - 값 누적을 끝내기 위해서 `co.send(None)`으로 `None`을 전달