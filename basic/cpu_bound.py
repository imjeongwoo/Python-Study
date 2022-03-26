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