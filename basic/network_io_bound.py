import re
from unittest import result
import requests

def io_bound_function():
    result = requests.get("https://google.com")
    return result


if __name__ == "__main__":
    for _ in range(10):
        result = io_bound_function()
    print(result)