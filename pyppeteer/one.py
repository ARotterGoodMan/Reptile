import asyncio
import pyppeteer


# from lxml import etree


async def text():
    drive = await pyppeteer.launch(headless=False)
    page = await drive.newPage()
    await page.goto("https://www.baidu.com")
    print(page)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(text())
