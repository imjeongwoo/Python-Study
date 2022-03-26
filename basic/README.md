# 바운드와 블록킹
    블록킹 : 바운드에 의해 코드가 멈추게 되는 현상
## CPU 바운드
- 프로그램이 실행될 때 실행 속도가 **CPU 속도에 의해 제한됨**
- 보통 매우 복잡한 수학 계산식을 수행할 때 실행 속도가 느려짐
```python
def cpu_bound_function(num: int):
    result = 1
    arrange = range(1, num + 1)
    for i in arrange:
        for j in arrange:
            for k in arrange:
                result *= i * j * k
    return result


if __name__ == "__main__":
    result = cpu_bound_function(100)
    print(result)

# CPU가 실행을 막는다
```
<br>

## IO 바운드
- 프로그램이 실행될 때 실행 속도가 **I/O에 의해 제한됨**
- 키보드 입력 뿐만 아니라, 컴퓨터끼리 통신 시에도 I/O 바운드 발생 (ex. Network I/O)
```python
def io_bound_function():
    input_val = input("값 입력: ")
    return int(input_val) + 100


if __name__ == "__main__":
    result = io_bound_function()
    print(result)

# 사용자 응답을 기다림
```
