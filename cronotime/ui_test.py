#!/usr/bin/python3
import kivy

kivy.require("2.3.0")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.config import Config


from stopwatch import StopWatch

# Cargar el archivo .kv
Builder.load_file("ui/uitest.kv")


class UiTest(Widget):
    def __init__(self, **kwargs) -> None:
        super(UiTest, self).__init__(**kwargs)


class UiTestApp(App):

    def build(self) -> UiTest:
        Config.set("input", "mouse", "mouse,multitouch_on_demand")
        Window.size = (1000, 750)
        return UiTest()


if __name__ == "__main__":
    UiTestApp().run()
