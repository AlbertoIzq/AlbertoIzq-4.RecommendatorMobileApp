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
			self.manager.transition.direction = 'left'
			self.manager.current = "main_screen"
		else:
			self.ids.login_wrong.text = "Wrong username or password!"

	def signUp(self):
		self.manager.transition.direction = 'right'
		self.manager.current = "sign_up_screen"

	def forgetPass(self):
		self.manager.transition.direction = 'right'
		self.manager.current = "forget_pass_screen"

class SignUpScreen(Screen):
	def add_user(self, uname, pword):
		with open("users.json") as file:
			users = json.load(file)

		users[uname] = {'username' : uname, 'password' : pword,
						'created' : datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

		# Overwrite previous file
		with open("users.json", 'w') as file:
			json.dump(users, file)

		self.manager.current = "sign_up_screen_success"

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