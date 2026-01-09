helper_style = """
MDScreen:
    MDLabel:
        text: "Run Radio Test, it will help if your mobile data is off"
        halign: "center"
        valign: "center"
        theme_text_color: "Primary"
        font_style: "H6"
    MDRaisedButton:
        text: "click to start test"
        theme_text_color: "Primary"
        pos_hint: {"center_x": 0.4, "center_y": 0.4}
        on_release: app.ap_test()
        
    MDRaisedButton:
        text: "click to start full test"
        theme_text_color: "Primary"
        pos_hint: {"center_x": 0.6, "center_y": 0.4}    
        on_release: app.ap_test2()

"""
