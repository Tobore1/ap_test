from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRoundFlatButton

from helper_style import helper_style
from tzttest import work, aptest


class TestApp(MDApp):
    def build(self):
        screen = Builder.load_string(helper_style)
        return screen

    def ap_test(self):
        ap_ping = str(work.works)
        if ap_ping == "None":
            ap_ping = "check you p.o.e or wait, Radio is not Up "

        close_button = MDRoundFlatButton(text="Close", on_release=self.close_dialog)
        # Run_again = MDRoundFlatButton(text="Run again", on_release=self.Run_again)
        # hold on the run again feature.
        self.dialog = MDDialog(title="AP check", text=ap_ping,
                               size_hint=(0.7, 1), buttons=[close_button])
        self.dialog.open()

    def ap_test2(self):
        ap_ping2 = str(aptest.test_imsi)
        ap_ping3 = str(aptest.test_plmn)
        all_test = (ap_ping2 +  ap_ping3)

        # if all_test  == "Radio is not working":
        #     all_test = "Radio is working"

        close_button = MDRoundFlatButton(text="Close", on_release=self.close_dialog)
        self.dialog = MDDialog(title=" Full AP check", text=all_test,
                               size_hint=(0.7, 1), buttons=[close_button])

        self.dialog.open()


    def close_dialog(self, obj):
        self.dialog.dismiss()

    def Run_again(self, obj):
        pass

if __name__ == '__main__':
    TestApp().run()
