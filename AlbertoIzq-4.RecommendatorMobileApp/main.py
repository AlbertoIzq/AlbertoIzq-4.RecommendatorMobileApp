from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

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
	def login(self):
		self.manager.current = "main_screen"

	def signUp(self):
		self.manager.transition.direction = 'right'
		self.manager.current = "sign_up_screen"

	def forgetPass(self):
		self.manager.transition.direction = 'right'
		self.manager.current = "forget_pass_screen"

class SignUpScreen(Screen):
	def add_user(self, name, password):
		print(name, password)

class SignUpScreenSuccess(Screen):
	def goToLogin(self):
		self.manager.current = "login_screen"

class ForgetPassScreen(Screen):
	pass

class ForgetPassScreenSuccess(Screen):
	def goToLogin(self):
		self.manager.current = "login_screen"


class Main(Screen):
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