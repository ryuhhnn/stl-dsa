import sys
import os
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

opts = FirefoxOptions()
opts.add_argument("--headless")


class PrioritiesTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(options=opts)

    def tearDown(self):
        self.browser.quit()
