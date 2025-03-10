from selenium import webdriver

# Class to represent the driver to scrape a website for information
class Scrapper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        #Prevent Chrome from automatically closing at the end of the script
        options.add_experimental_option('detach', True)

        # Create the driver for chrome
        self.browser = webdriver.Chrome(options=options)
        #Option the intial page to start to scraping
        self.browser.get('https://monsterhunterwilds.wiki.fextralife.com/Monster+Hunter+Wilds+Wiki')

    # Close the running instance of the driver
    def exit(self):
        self.browser.quit()
