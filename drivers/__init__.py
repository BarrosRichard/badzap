from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.options import Options as OptionsFox
from webdriver_manager.firefox import GeckoDriverManager


class ChromeDriver:
    def options(options=[]):
        chrome_options = Options()
        for opt in options:
            if type(opt) == list:
                chrome_options.add_experimental_option(opt[0], opt[1])
            else:
                chrome_options.add_argument(opt)

        return chrome_options

    def webdriver(self, options=[]):
        return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=self.options(options))


class FirefoxDriver:
    def options(options=[]):
        firefox_options = OptionsFox()
        for opt in options:
            if type(opt) == list:
                firefox_options.add_argument(opt[0], opt[1])
            else:
                firefox_options.add_argument(opt)

        return firefox_options

    def webdriver(options=[]):
        # return webdriver.Firefox(GeckoDriverManager().install(), firefox_options=FirefoxDriver.options(options))
        return webdriver.Firefox(GeckoDriverManager().install())
