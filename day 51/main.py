from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

PROMISED_UP = 15
PROMISED_DOWN = 200

TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()

        wait = WebDriverWait(self.driver, 150)
        wait.until(ec.url_contains("result"))
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"Final Speeds - Down: {self.down}, Up: {self.up}")

    def tweet_provider(self):
        self.driver.get("https://twitter.com/login")
        wait = WebDriverWait(self.driver, 20)

        email = wait.until(ec.presence_of_element_located((By.NAME, "text")))
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        time.sleep(3)
        try:
            secondary_field = self.driver.find_element(By.NAME, "text")
            secondary_field.send_keys("HemanthBabu2006")
            secondary_field.send_keys(Keys.ENTER)
            print("Username verification step handled.")
        except:
            print("No secondary verification needed.")
        password = wait.until(ec.presence_of_element_located((By.NAME, "password")))
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        tweet_box = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='tweetTextarea_0']")))
        message = f"Hey ISP, why is my speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}/{PROMISED_UP}?"
        tweet_box.send_keys(message)
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='tweetButtonInline']")
        tweet_button.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_provider()
