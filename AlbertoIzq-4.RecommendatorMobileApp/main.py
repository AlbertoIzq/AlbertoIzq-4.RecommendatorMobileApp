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
	pass

class SignUpScreen(Screen):
	pass

class SignUpScreenSuccess(Screen):
	pass

class ForgetPassScreen(Screen):
	pass

class ForgetPassScreenSuccess(Screen):
	pass


class Main(Screen):
	pass

class Music(Screen):
	pass

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