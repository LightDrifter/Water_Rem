import pickle
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from Popups.SetAlarm import *


class Manager(ScreenManager):
	pass

class MainScreen(Screen):
	goal = ObjectProperty(None)
	quantity = ObjectProperty(None)
	progress = ObjectProperty(None)
	
	def pressed(self):
		self.goal.value+= int(self.quantity.value)
		self.quantity.value = 0
		self.progress.text = str(self.goal.value*100//7000)+'%'
		print(self.progress.text)
		print(self.goal.value)

class SetScreen(Screen):
	#alarm_time = ObjectProperty(None)
	def alarm_btn(self):
		return set_alarm_popup()


class Drink(App):
    def build(self):
        return


if __name__ == '__main__':
    Drink().run()
