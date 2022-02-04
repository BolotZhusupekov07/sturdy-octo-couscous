import random
import string
import sys
import threading
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

lock = threading.Lock()


def generate_random_password(
    length=8, chars=string.ascii_letters + string.digits + string.punctuation
):
    return "".join(random.choice(chars) for _ in range(length))


class DiscordAccountGenerator:
    def __init__(self, email, username, password, proxy=None):
        self.driver = webdriver.Chrome(
            executable_path="/home/bolot/Desktop/chromedriver"
        )

        self.email = email
        self.username = username
        self.password = password

    def register(self):
        self.driver.get("https://discord.com/register")

        WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@type='email']")
            )
        )

        self.driver.find_element_by_xpath("//input[@type='email']").send_keys(
            self.email
        )
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(
            self.username
        )
        self.driver.find_element_by_xpath(
            "//input[@type='password']"
        ).send_keys(self.password)

        dateWorking = False

        try:
            actions = ActionChains(self.driver)
            time.sleep(0.5)

            self.driver.find_elements_by_class_name("css-1hwfws3")[0].click()

            actions.send_keys(str(random.randint(1, 12)))
            actions.send_keys(Keys.ENTER)
            actions.send_keys(str(random.randint(1, 28)))
            actions.send_keys(Keys.ENTER)
            actions.send_keys(str(random.randint(1990, 2001)))
            actions.send_keys(Keys.ENTER)
            actions.send_keys(Keys.TAB)
            actions.send_keys(Keys.ENTER)
            actions.perform()
        except Exception:
            print(" Submit your form manually.")

        if dateWorking:
            actions = ActionChains(self.driver)

            actions.send_keys(str(random.randint(1, 12)))
            actions.send_keys(Keys.ENTER)
            actions.send_keys(str(random.randint(1, 28)))
            actions.send_keys(Keys.ENTER)

            random_year = [
                1989,
                1990,
                1991,
                1992,
                1993,
                1994,
                1995,
                1996,
                1997,
                1998,
                1999,
                2000,
            ]

            actions.send_keys(str(random.choice(random_year)))
            actions.perform()

            try:
                self.driver.find_element_by_class_name(
                    "inputDefault-3JxKJ2"
                ).click()
            except Exception:
                print("Submit manually")

            self.driver.find_element_by_class_name("button-3k0cO7").click()

        while True:
            lock.acquire()
            checker = input("Have you finished ? [y/n]")
            lock.release()
            if checker == "y":
                self.token = self.driver.execute_script(
                    "let popup; popup = window.open('', '', `width=1,height=1`); if(!popup || !popup.document || !popup.document.write) console.log('Please allow popups'); window.dispatchEvent(new Event('beforeunload')); token = popup.localStorage.token.slice(1, -1); popup.close(); return token"
                )
                break
                return True
            elif checker == "n":
                sys.exit()

        return False


def main():
    email = input("Enter an email: ")
    username = input("Enter an username: ")
    password = generate_random_password()

    discord_account = DiscordAccountGenerator(email, username, password)

    discord_account.register()
    print(str(discord_account.token))


if __name__ == "__main__":
    main()
