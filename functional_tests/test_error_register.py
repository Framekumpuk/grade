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
        
        # มีนักศึกษาคนหนึ่งชื่อของเขาคือธิติ เขาได้ทราบผลสอบกลางภาคของเขาในรายวิชา Mathematics ว่า เขาได้คะแนน 58 คะแนน จากคะแนนเต็ม 90 คะแนน
        # เขาจึงได้เข้าโปรแกรมคำนวณเกรดว่าเขาจะได้เกรดอะไรในเทอมนี้ โดยเขาคาดคะเนไว้ว่า ปลายภาคเขาน่าจะได้ประมาณ 64 คะแนนเต็ม 90 
        self.browser.get(self.live_server_url)
        time.sleep(1)
        self.assertIn('Grade', self.browser.title)
        
        # เมื่อเขาเปิดหน้าเว็บขึ้นมา เขาพบกับคำว่า Grade Simulation และช่องให้ผู้ใช้กรอก Username กับ Password แต่เขายังไม่เคยใช้แอพนี้มาก่อน เขาเลยกดปุ่ม sign up เพื่อสมัครสมาชิก
        self.browser.find_element_by_name('signup').click()

        # เขาได้ใส่ Username ไปว่า titi แต่เขาไม่ได้กรอกรหัสผ่าน และกดส่งไป จึงไปยังหน้าข้อความแจ้งเตือน
        username_box = self.browser.find_element_by_name('name')
        username_box.send_keys('titi')
        password_box = self.browser.find_element_by_name('password')
        password_box.send_keys('')
        password_box.send_keys(Keys.ENTER)
        time.sleep(3)
