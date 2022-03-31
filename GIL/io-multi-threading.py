import requests, time
import os, threading
from concurrent.futures import ThreadPoolExecutor

def fetcher(params):
    session, url = params 
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text

def main():
    urls = ["https://www.daum.net", "https://www.naver.com", "https://www.apple.kr"] * 50

    executor = ThreadPoolExecutor(max_workers=10)

    with requests.Session() as session:
        params = [(session, url) for url in urls]
        result = list(executor.map(fetcher, params))
        print(result)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"실행 시간 : {end - start}")

"""
max_worker = 1 -> 실행 시간 : 16.03657293319702
max_worker = 10 -> 실행 시간 : 4.8986496925354

멀티 스레딩이 병렬적으로 수행은 안되었지만, 동시적으로 작동은 해서 성능은 빨라졌다.
"""