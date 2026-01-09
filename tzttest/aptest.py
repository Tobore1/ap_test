from playwright.sync_api import sync_playwright, Error  # Import Error to catch it
from bs4 import BeautifulSoup


class Aptest():
    def __init__(self):
        # Initialize variables as None or "-" so they exist if the code fails
        self.imsi = None
        self.imei = None
        self.plmn = None
        self.status_message = ""

        self.run_scrape()

    def run_scrape(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            try:
                # Set a short timeout (e.g., 5 seconds) so you don't wait forever
                page.goto("http://192.168.150.1", timeout=5000)

                # ... your login and scraping code here ...
                page.fill('input#username', 'admin')
                page.fill('input#password', 'admin')
                page.click('input[type=submit]')
                page.wait_for_load_state("networkidle")

                html = page.inner_html(".cbi-section:has-text('LTE Status')")
                soup = BeautifulSoup(html, "html.parser")

                self.imsi = soup.find(id="imsi").text
                self.imei = soup.find(id="imei").text
                self.plmn = soup.find(id="plmn").text

            except Error:
                # This catches the ERR_CONNECTION_TIMED_OUT
                self.status_message = "Radio is not Up"
            finally:
                browser.close()

    def imsi_test(self):
        if self.status_message == "Radio is not Up":
            return "Radio is not Up"

        if self.imsi and self.imsi != "-":
            return "imsi test passed"
        else:
            return "call someone, imsi issue"

    def plmn_test(self):
        if self.status_message == "Radio is not Up":
            return " "

        if self.plmn and self.plmn != "-":
            return " plmn test passed       "
        else:
            return "call someone or check sub, plmn issue"

test = Aptest()
test_imsi = test.imsi_test()
test_plmn = test.plmn_test()
if __name__ == "__main__":
    pass