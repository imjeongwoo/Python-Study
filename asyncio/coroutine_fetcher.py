import aiohttp, asyncio, time

async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ["https://www.daum.net", "https://www.naver.com", "https://www.google.com"] * 20

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"실행 시간 : {end - start}")

# 실행 시간 : 1.8221161365509033