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
	def add_user(self, uname, pword, fword):
		has_capital_letter = False
		has_number = False
		len_ok = len(pword) >= 8
		for letter in pword:
			if letter.isupper():
				has_capital_letter = True
			if letter.isdigit():
				has_number = True

		with open("users.json") as file:
			users = json.load(file)

		if len_ok and has_capital_letter and has_number and not (uname in users):
			users[uname] = {'username' : uname, 'password' : pword,
							'created' : datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
							'favourite_word' : fword}

			# Overwrite previous file
			with open("users.json", 'w') as file:
				json.dump(users, file)

			self.setMessage()
			self.resetInputs()
			self.manager.current = "sign_up_screen_success"
		elif (uname in users):
			self.setMessage("Username already exists!")
		else:
			self.setMessage("Invalid Password!")

	def setMessage(self, text = ""):
		self.ids.sign_up_wrong.text = text

	def resetInputs(self):
		self.ids.username.text = ""
		self.ids.password.text = ""
		self.ids.fav_word.text = ""

class SignUpScreenSuccess(Screen):
	def goToLogin(self):
		self.manager.transition.direction = 'left'
		self.manager.current = "login_screen"

class ForgetPassScreen(Screen):
	def getPassword(self, uname, fword):
		with open("users.json") as file:
			users = json.load(file)
		
		if uname in users and users[uname]['favourite_word'] == fword:
			password = users[uname]['password']
			self.setMessage(password)
		else:
			self.setMessage("Wrong username or favourite word!")

	def goToLogin(self):
		self.setMessage()
		self.resetInputs()
		self.manager.transition.direction = 'left'
		self.manager.current = "login_screen"

	def setMessage(self, text = ""):
		self.ids.retrieved_password.text = text

	def resetInputs(self):
		self.ids.username.text = ""
		self.ids.fav_word.text = ""

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
	pass

class Series(Screen):
	pass

class Books(Screen):
	pass

class Places(Screen):
	pass

class Other(Screen):
	pass

class RootWidget(ScreenManager):
	pass

class MainApp(App):
	def build(self):
		return RootWidget()

if __name__ == '__main__':
	MainApp().run()