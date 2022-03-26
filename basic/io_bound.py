def io_bound_function():
    input_val = input("값 입력: ")
    return int(input_val) + 100


if __name__ == "__main__":
    result = io_bound_function()
    print(result)