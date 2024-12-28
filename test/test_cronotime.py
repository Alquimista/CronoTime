import unittest
import time

from cronotime.stopwatch import StopWatch


class TestStopWatch(unittest.TestCase):

    def setUp(self) -> None:
        self.stopwatch = StopWatch()

    def test_initial_state(self) -> None:
        self.assertEqual(self.stopwatch.get_time(), "0:00:00.000")

    def test_start(self) -> None:
        self.stopwatch.start()
        time.sleep(0.1)
        self.assertNotEqual(self.stopwatch.start_time, 0)

    def test_stop(self) -> None:
        self.stopwatch.start()
        time.sleep(0.1)
        self.stopwatch.stop()
        elapsed_time: int | float = self.stopwatch.elapsed
        self.assertGreater(elapsed_time, 0)
        self.assertEqual(self.stopwatch.start_time, 0)

    def test_reset(self) -> None:
        self.stopwatch.start()
        time.sleep(0.1)
        self.stopwatch.stop()
        self.stopwatch.reset()
        self.assertEqual(self.stopwatch.get_time(), "0:00:00.000")

    def test_get_time_format(self):
        self.stopwatch.start()
        time.sleep(0.1)
        self.stopwatch.stop()
        time_str: str = self.stopwatch.get_time()
        self.assertRegex(time_str, r"\d:\d{2}:\d{2}\.\d{3}")

    def test_get_time_format_seconds(self):
        self.stopwatch.start()
        time.sleep(0.349)
        self.stopwatch.stop()
        time_str: str = self.stopwatch.get_time()
        self.assertEqual(time_str, "0:00:00.349")

    def test_is_running(self) -> None:
        self.assertFalse(self.stopwatch.is_running())
        self.stopwatch.start()
        self.assertTrue(self.stopwatch.is_running())
        self.stopwatch.stop()
        self.assertFalse(self.stopwatch.is_running())


if __name__ == "__main__":
    unittest.main()
