import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
from kivy.adapters.listadapter import ListAdapter


class CanteenApp(App):
    def build(self):
        return CanteenLayout()

    def order_item(self, item_name):

        print(f"Ordered: {item_name}")

class CanteenLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(CanteenLayout, self).__init__(**kwargs)


CanteenApp().run()
