from playwright.async_api import async_playwright


class BrowserTool:
    """Use Playwright headless browser to fetch page contents."""

    async def fetch(self, url: str) -> str:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url)
            content = await page.content()
            await browser.close()
            return content