from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):  #2
        self.browser = webdriver.Firefox()

    def tearDown(self):  #3
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('Grade', self.browser.title)  #5

        button = self.browser.find_element_by_id('0')

        button.send_keys(Keys.ENTER)

        time.sleep(1)
        
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('1')

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Math')
        time.sleep(1)
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('2')

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('58')
        time.sleep(1)
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('3')

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('90')
        time.sleep(1)
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('4')

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('3')
        time.sleep(1)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)

         #6
        time.sleep(1)

        button = self.browser.find_element_by_id('5')
        button.send_keys(Keys.ENTER)

        button = self.browser.find_element_by_id('6')
        button.send_keys(Keys.ENTER)
        time.sleep(3)
        
        self.fail('Finish the test!')         

if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8
