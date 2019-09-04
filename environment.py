
"""		Pyautomator Framework de teste 

			saraivatestes"""

from Pyautomators import fixture
from Pyautomators.contrib.scenario_autoretry import scenario_retry
from selenium import webdriver
from pages.pages.CartPage import CartPage

def before_all(context):
	context.app=webdriver.Chrome('driver/chromedriver.exe')
	context.page=CartPage(context.app)

def before_feature(context,feature):
	pass

def before_scenario(context,scenario):
	pass

def before_step(context,step):
	pass

def after_step(context,step):
	pass

def after_scenario(context,scenario):
	pass

def after_feature(context,feature):
	pass

def after_all(context):
	context.app.quit()

