import requests, time
import os, threading

def fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text

def main():
    urls = ["https://www.daum.net", "https://www.naver.com", "https://www.apple.kr"] * 50

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"실행 시간 : {end - start}")

# 실행 시간 : 17.820591926574707