#!/usr/bin/env python3
"""
 This is a basic code to deploy a simple Instagram messaging bot using selenium.
 you still can add enhanced feature to it.
"""
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


# Define the friends IDs
friends = ['list of friends']
# Define the messages
message = ("customized message")
# initiate the driver
browser_driver = webdriver.Chrome(ChromeDriverManager().install())

class InstagramMessageBot:
	def __init__(self, username, password, friends, message):

		self.username = username
		self.password = password
		self.friends = friends
		self.message = message
		self.url = 'https://www.instagram.com/'
		self.message_bot = browser_driver
		self.singin()

	def singin(self):
		"""
		 this function stimulates the user behavior (login/clicks/typing) using the xpath of the coponents
			NB: you can get xpath from the inspect section.

		   """
		self.message_bot.get(self.url)
		get_username = WebDriverWait(self.message_bot, 20).until(
			expected_conditions.presence_of_element_located((By.NAME, 'username')))
		get_username.send_keys(self.username)
		get_password = WebDriverWait(self.message_bot, 20).until(
			expected_conditions.presence_of_element_located((By.NAME, 'password')))
		get_password.send_keys(self.password)
		get_password.send_keys(Keys.RETURN)
		time.sleep(5)

		# first pop-up not now click
		self.message_bot.find_element_by_xpath(
			'//*[@id="react-root"]/section/main/div/div/div/div/button').click()
		time.sleep(5)

		# second pop-up not now click
		self.message_bot.find_element_by_xpath(
			'/html/body/div[6]/div/div/div/div[3]/button[2]').click()
		time.sleep(5)
		# direct button click
		self.message_bot.find_element_by_xpath(
			'//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]').click()
		time.sleep(3)

		# click on pencil icon
		self.message_bot.find_element_by_xpath(
			'//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
		time.sleep(2)
		for i in user:

			# enter the username
			self.message_bot.find_element_by_xpath(
				'/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
			time.sleep(2)

			# click on the username
			self.message_bot.find_element_by_xpath(
				'/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div').click()
			time.sleep(2)

			# next button
			self.message_bot.find_element_by_xpath(
				'/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()
			time.sleep(2)

			# click on message area
			send = self.message_bot.find_element_by_xpath(
				'/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

			# types message
			send.send_keys(self.message)
			time.sleep(1)

			# send message
			send.send_keys(Keys.RETURN)
			time.sleep(2)

			# clicks on direct option or pencl icon
			self.message_bot.find_element_by_xpath(
				'/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
			time.sleep(2)


def main():

	InstagramMessageBot('your_user_ID', 'your_password', friends, message)
	input("End of the task")


if __name__ == "__main__":
    main()
