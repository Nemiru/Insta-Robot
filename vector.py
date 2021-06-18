from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
user =['chavare_22','clivesdoesmarketing']
message_ = ("Hi hope you're well,"
"I'm Clive from Matrix Epos."
""
"I believe We came across your business online and I noticed what service"
"you're promoting."
""
"We like to chat with members of a business & business directors looking"
"thinking about improving features in their brick and mortar & online"
"website presence. But that's down to you guys we can provide you a few"
"products & services for you to browse?"
""
"I attached a promotional product of our service options <pdf link>"
"We have managed a valuable network of clientele across different industries"
"like Retail & Hospitality, so our service is built on experience."
""
#"SOME QUESTIONS"
#"Now for the next step,"
#"I would love to offer a 30-minute FREE"
#"call/video chat to talk about what kind of deals you're looking for with"
#"your requirements, then just send me your availability for the next few"
#"days so we can jump on a call."
#"You’re in good hands friend."
#"- Clive"
"www.matrixepos.co.uk"
"I look forward to hearing from you!")
username = ('matrixepos@gmail.com')
password = ('Birmingham@2020')

class bot:
	def __init__(self, username, password, user, message_):
		self.username = username
	    self.password = password
	    self.user = user
	    self.message = message
	    self.base_url = 'https://www.instagram.com/'
	    self.bot = driver
        self.login()
#entering the login details from above
def login(self):
	self.bot.get(self.base_url)	
enter_username = WebdriverWait(self.bot, 20).until(
    	expected_conditions.presence_of_element_located)((By.NAME,'username'))
enter_username.send_keys(self.username)
      
    
enter_password = WebDriverWait(self.bot, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'password')))
enter_password.send_keys(self.password)
  
   
enter_password.send_keys(Keys.RETURN)
time.sleep(5)

# first pop-up box
self.bot.find_element_by_xpath(
	'//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(3)

# 2nd pop-up box
self.bot.find_element_by_xpath(
	'/html/body/div[4]/div/div/div/div[3]/button[2]').click()

time.sleep(4)

# this will click on message(direct) option.
self.bot.find_element_by_xpath(
	'//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]').click()
time.sleep(3)

# This will click on the pencil icon as shown in the figure.
self.bot.find_element_by_xpath(
	'//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button').click()
time.sleep(2)


for i in user:

	# enter the username
	self.bot.find_element_by_xpath(
		'/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
	time.sleep(2)

	# click on the username
	self.bot.find_element_by_xpath(
		'/html/body/div[4]/div/div/div[2]/div[2]/div').click()
	time.sleep(2)

	# next button
	self.bot.find_element_by_xpath(
		'/html/body/div[4]/div/div/div[1]/div/div[2]/div/button').click()
	time.sleep(2)

	# click on message area
	send = self.bot.find_element_by_xpath(
		'/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

	# types message
	send.send_keys(self.message)
	time.sleep(1)

	# send message
	send.send_keys(Keys.RETURN)
	time.sleep(2)

	# clicks on pencil icon
	self.bot.find_element_by_xpath(
		'/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
	time.sleep(2)
	# here will take the next username from the user's list.

def init():
	bot('matrixepos@gmail.com', 'Birmingham@2020', user, message_)

	input("we is done bonny")

init()