#!/usr/bin/python3
import kivy

kivy.require("2.3.0")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.config import Config


from stopwatch import StopWatch

# Cargar el archivo .kv
Builder.load_file("ui/stopwatch.kv")


class StopWatchWidget(Widget):
    """
    A widget that functions as a stopwatch with lap functionality.

    Attributes:
        timer (StopWatch): The main stopwatch timer.
        lap_timer (StopWatch): The timer for individual laps.
        lap (int): The current lap number.
        stopwatch_started (bool): Indicates whether the stopwatch is running.

    Methods:
        update(dt): Updates the time label with the current time from the timer.
        on_start_stop_pressed(): Handles the start/stop button press event.
        on_reset_lap_pressed(): Handles the reset/lap button press event.
    """

    time_label = ObjectProperty(None)
    lap_label = ObjectProperty(None)
    start_stop_button = ObjectProperty(None)
    lap_reset_button = ObjectProperty(None)

    def __init__(self, **kwargs) -> None:
        super(StopWatchWidget, self).__init__(**kwargs)

        # Fonts made by Web Free Fonts is licensed by CC 4.0 BY
        self.timer = StopWatch()
        self.lap_timer = StopWatch()
        self.lap: int = 1
        self.stopwatch_started: bool = False
        self.clock_event = None

    def update(self, dt) -> None:
        lap_time = self.lap_timer.get_time()
        total_time = self.timer.get_time()
        self.time_label.text = total_time
        self.lap_label.text = f"Lap {self.lap}: {lap_time}    Total: {total_time}"

    def on_start_stop_pressed(self) -> None:
        if self.stopwatch_started:
            self.timer.stop()
            self.lap_timer.stop()
            self.start_stop_button.bgcolor = "#4aae71"
            self.lap_reset_button.bgcolor = "#fbad10"
            self.start_stop_button.text = "Start"
            self.lap_reset_button.text = "Reset"
            if self.clock_event:
                self.clock_event.cancel()
        else:
            self.timer.start()
            self.lap_timer.start()
            self.start_stop_button.bgcolor = "#ef6262"
            self.lap_reset_button.bgcolor = "#0090dd"
            self.start_stop_button.text = "Stop"
            self.lap_reset_button.text = "Lap"
            self.clock_event = Clock.schedule_interval(self.update, 0.01)
        self.stopwatch_started = not self.stopwatch_started

    def on_reset_lap_pressed(self) -> None:
        if self.stopwatch_started:
            self._lap()
        else:
            self._reset()

    def _lap(self) -> None:
        lap_time: str = self.lap_timer.get_time()
        total_time: str = self.timer.get_time()
        lap_label = Label(
            text=f"Lap {self.lap}: {lap_time}    Total: {total_time}",
            font_size="16sp",
            bold=True,
            color="#000000",
            size_hint_y=None,
            height=20,
        )
        self.lap_box.add_widget(lap_label)
        self.lap_timer.reset()
        self.lap_timer.start()
        self.lap += 1

    def _reset(self) -> None:
        self.timer.reset()
        self.lap_timer.reset()
        self.stopwatch_started = False
        self.lap = 1
        self.time_label.text = "0:00:00:000"
        self.lap_label.text = ""
        self.lap_box.clear_widgets()


class StopWatchApp(App):
    def build(self) -> StopWatchWidget:
        Config.set("input", "mouse", "mouse,multitouch_on_demand")
        Window.size = (1000, 750)
        return StopWatchWidget()


if __name__ == "__main__":
    StopWatchApp().run()
