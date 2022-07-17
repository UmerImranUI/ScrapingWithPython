from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  #opening browser with name headless=true if browser isn't to be opened
        page = browser.new_page()
        page.goto('https://quotes.toscrape.com/js')  #goto page

        heading = page.query_selector('//h1/a')   #selector for xpath/css

        login = page.query_selector('[href="/login"]')
        login.click()   #click

        user_input = page.query_selector('[id="username"]')
        user_input.type("user")   #supplying inp fields

        pass_input = page.query_selector('//*[text()="Password"]/following-sibling::*')
        pass_input.type('text')

        page.query_selector('[type="submit"]').click()

        selector = '//*[@href="/logout"]'
        try:
            logout = page.wait_for_selector(selector, timeout=5000)
        except:
            print('login failed')
            exit()
        quotes = page.query_selector_all('[class="quote"]')
        for quote in quotes:
            print(quote.query_selector('.text').inner_text())

        browser.close()


if __name__ == '__main__':
    main()