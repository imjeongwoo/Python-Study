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