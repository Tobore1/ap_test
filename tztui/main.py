from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

from tzttest import work, aptest

class MyGrid(Widget):
    name= ObjectProperty(None)
    email= ObjectProperty(None)
    imsi = ObjectProperty(None)
    plmn = ObjectProperty(None)
    imei = ObjectProperty(None)
    def btn(self):
        ap_ping =  str(work.R_Ping1)
        imsi_test = str(aptest.imsi_test)
        plmn_test = str(aptest.plmn_test)
        imei_test = str(aptest.imei_test)
        self.name.text = ap_ping

        self.imsi.text = imsi_test
        self.plmn.text = plmn_test
        self.imei.text = imei_test

        self.email.text = " scan complete"

class MyApp(App):
    def build(self):
        return MyGrid()


MyApp().run()