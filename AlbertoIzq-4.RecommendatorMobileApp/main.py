from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import json
from datetime import datetime

Builder.load_file('design.kv')
Builder.load_file('kivy/login.kv')
Builder.load_file('kivy/sign_up.kv')
Builder.load_file('kivy/sign_up_success.kv')
Builder.load_file('kivy/forget_pass.kv')
Builder.load_file('kivy/forget_pass_success.kv')
Builder.load_file('kivy/main.kv')
Builder.load_file('kivy/music.kv')
Builder.load_file('kivy/movies.kv')
Builder.load_file('kivy/series.kv')
Builder.load_file('kivy/books.kv')
Builder.load_file('kivy/places.kv')
Builder.load_file('kivy/other.kv')

class LoginScreen(Screen):
	def login(self, uname, pword):
		with open("users.json") as file:
			users = json.load(file)
		if uname in users and users[uname]['password'] == pword:
			self.setMessage()
			self.resetInputs()
			self.manager.transition.direction = 'left'
			self.manager.current = "main_screen"
		else:
			self.setMessage("Wrong username or password!")

	def signUp(self):
		self.setMessage()
		self.resetInputs()
		self.manager.transition.direction = 'right'
		self.manager.current = "sign_up_screen"

	def forgetPass(self):
		self.setMessage()
		self.resetInputs()
		self.manager.transition.direction = 'right'
		self.manager.current = "forget_pass_screen"

	def setMessage(self, text = ""):
		self.ids.login_wrong.text = text

	def resetInputs(self):
		self.ids.username.text = ""
		self.ids.password.text = ""

class SignUpScreen(Screen):
	def add_user(self, uname, pword):
		has_capital_letter = False
		has_number = False
		len_ok = len(pword) >= 8
		for letter in pword:
			if letter.isupper():
				has_capital_letter = True
			if letter.isdigit():
				has_number = True

		if len_ok and has_capital_letter and has_number:
			with open("users.json") as file:
				users = json.load(file)

			users[uname] = {'username' : uname, 'password' : pword,
							'created' : datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

			# Overwrite previous file
			with open("users.json", 'w') as file:
				json.dump(users, file)

			self.setMessage()
			self.resetInputs()
			self.manager.current = "sign_up_screen_success"
		else:
			self.setMessage("Invalid Password!")

	def setMessage(self, text = ""):
		self.ids.sign_up_wrong.text = text

	def resetInputs(self):
		self.ids.username.text = ""
		self.ids.password.text = ""

class SignUpScreenSuccess(Screen):
	def goToLogin(self):
		self.manager.transition.direction = 'left'
		self.manager.current = "login_screen"

class ForgetPassScreen(Screen):
	pass

class ForgetPassScreenSuccess(Screen):
	def goToLogin(self):
		self.manager.transition.direction = 'left'
		self.manager.current = "login_screen"


class Main(Screen):
	def logOut(self):
		self.manager.transition.direction = 'right'
		self.manager.current = "login_screen"
	pass

class Music(Screen):
	def goToMain(self):
		self.manager.transition.direction = 'right'
		self.manager.current = "main_screen"

class Movies(Screen):
	def goToMain(self):
		self.manager.transition.direction = 'right'
		self.manager.current = "main_screen"

class Series(Screen):
	def goToMain(self):
		self.manager.transition.direction = 'right'
		self.manager.current = "main_screen"

class Books(Screen):
	def goToMain(self):
		self.manager.transition.direction = 'right'
		self.manager.current = "main_screen"

class Places(Screen):
	def goToMain(self):
		self.manager.transition.direction = 'right'
		self.manager.current = "main_screen"

class Other(Screen):
	def goToMain(self):
		self.manager.transition.direction = 'right'
		self.manager.current = "main_screen"

class RootWidget(ScreenManager):
	pass

class MainApp(App):
	def build(self):
		return RootWidget()

if __name__ == '__main__':
	MainApp().run()