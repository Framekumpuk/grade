from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        
        self.browser.get(self.live_server_url)
        time.sleep(1)
        self.assertIn('Grade', self.browser.title)

        self.browser.find_element_by_name('signup').click()

        # register
        username_box = self.browser.find_element_by_name('name')
        username_box.send_keys('titi')
        password_box = self.browser.find_element_by_name('password')
        password_box.send_keys('dontseemypass')
        password_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # back to login
        self.browser.find_element_by_name('backtologin').click()
        time.sleep(1)

        # login
        username_box = self.browser.find_element_by_name('name')
        username_box.send_keys('titi')
        password_box = self.browser.find_element_by_name('password')
        password_box.send_keys('dontseemypass')
        password_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # enter to program
        self.browser.find_element_by_name('enter_program').click()
        time.sleep(1)

        # put data of that subject
        inputbox = self.browser.find_element_by_id('1')
        inputbox.send_keys('Math')
        time.sleep(1)

        inputbox = self.browser.find_element_by_id('2')
        inputbox.send_keys('3')
        time.sleep(1)
        
        inputbox = self.browser.find_element_by_id('3')
        inputbox.send_keys('58')
        time.sleep(1)

        inputbox = self.browser.find_element_by_id('4')
        inputbox.send_keys('90')
        time.sleep(1)

        inputbox = self.browser.find_element_by_id('5')
        inputbox.send_keys('64')
        time.sleep(1)

        inputbox = self.browser.find_element_by_id('6')
        inputbox.send_keys('90')
        time.sleep(1)

        inputbox = self.browser.find_element_by_id('7')
        inputbox.send_keys('36')
        time.sleep(1)

        inputbox = self.browser.find_element_by_id('8')
        inputbox.send_keys('14')
        time.sleep(1)
        
        inputbox.send_keys(Keys.ENTER)

        self.browser.find_element_by_id('10').click() # see result
        time.sleep(3)
