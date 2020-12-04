from selenium import webdriver  # WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep


class Distancy:
    def __init__(self):
        # Chrome Settings
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.driver = webdriver.Chrome(options=chrome_options)

    def open(self):
        """
        This functions opens up google search
        """
        self.driver.get(
            'https://www.google.com/search?source=hp&ei=N-_EX7qiFo'
            'vB3LUPoMSZ6Ag&q=Singapore+560578+to+Singapore+'
            '319773&oq=Singapore+560578+to+Singapore+319773&gs_lcp='
            'CgZwc3ktYWIQAzoLCAAQsQMQgwEQyQM6BQgAELEDOgIIADoLCC4QsQMQxwE'
            'QrwE6BQguELEDOggILhDHARCvAToICAAQsQMQgwE6BQgAEMkDOgIIJj'
            'oLCC4QsQMQxwEQowI6DgguELEDEIMBEMcBEKMCOgIILjoRCC4QsQMQxwEQrwEQyQMQkw'
            'I6CAguELEDEIMBOg4ILhCxAxCDARDHARCvAToRCC4QsQMQxwEQowIQy'
            'QMQkwI6BggAEBYQHjoICAAQFhAKEB46BAghEBVQ-g9YyJIBYKyTAWgOcAB4AIABdIgBxBmSAQQ0N'
            'i40mAEAoAEBqgEHZ3dzLXdperABAA&sclient=psy'
            '-ab&ved=0ahUKEwj6mZrZq6rtAhWLILcAHSBiBo0Q4dUDCAc&uact=5')

    def inputs(self, start, end):
        """
        This function searches from start to end.
        :param start: Postal Code of Starting Destination
        :param end: Postal Code of Ending Destination
        :return: Distance (str)
        """
        # Predefined Variables
        delay = 10
        wait = WebDriverWait(self.driver, delay)

        sleep(1)  # Waits for HTML page to render

        # Clears existing texts in the Google Search bar
        wait.until(
            ec.element_to_be_clickable((By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input'))).clear()

        # Inputs the start and end destination into the Google Search bar
        wait.until(
            ec.element_to_be_clickable((By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input'))).send_keys(
            "Singapore " + str(start) + " to Singapore " + str(end))

        # Initiate search
        wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[2]/button'))).click()

        # Retrieve distance from HTML source
        distance = self.driver.find_element_by_xpath('//*[@id="exp0"]/div[1]/div/div/span[1]/span[2]').text[:-2].trim()

        return distance

    # TODO: Optional, you can use abstraction to make your codes look nicer :D


# Instantiate Distancy
dist = Distancy()

dist.open()

# Input your postal codes here (int)
d = dist.inputs(560578, 808796)

# Print distance
print(d)


# This script helps you script the distance from one point to another point in Singapore.
# I haven't done any rigorous testings on the script. You can search for bugs for me.
# Moving forward you can add in your own loop to iterate through the postal codes (Need function for this)
