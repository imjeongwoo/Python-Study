import requests, time

def fetcher(session, url):
    with session.get(url) as response:
        return response.text

def main():
    urls = ["https://www.daum.net", "https://www.naver.com", "https://www.google.com"] * 20

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"실행 시간 : {end - start}")

# 실행 시간 : 4.675053119659424