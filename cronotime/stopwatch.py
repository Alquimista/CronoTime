import time


class StopWatch:
    """
    A simple stopwatch class to measure elapsed time.

    Methods
    -------
    __init__() -> None
        Initializes the stopwatch and resets the timer.
    start() -> None
        Starts the stopwatch if it is not already running.
    stop() -> None
        Stops the stopwatch and updates the elapsed time.
    reset() -> None
        Resets the stopwatch to its initial state.
    _update() -> float | int
        Updates and returns the current elapsed time.
    get_time() -> str
        Returns the formatted elapsed time as a string in the format "H:MM:SS.mmm".
    """

    def __init__(self) -> None:
        self.reset()

    def start(self) -> None:
        """Starts the stopwatch if it is not already running."""
        if not self.start_time:
            self.start_time: float = time.perf_counter()

    def stop(self) -> None:
        """Stops the stopwatch and updates the elapsed time."""
        if self.start_time:
            self.elapsed += time.perf_counter() - self.start_time
            self.start_time = 0

    def reset(self) -> None:
        """Resets the stopwatch to its initial state."""
        self.start_time = 0
        self.elapsed = 0

    def _update(self) -> float | int:
        """Updates and returns the current elapsed time."""
        if self.start_time:
            return self.elapsed + time.perf_counter() - self.start_time
        return self.elapsed

    def is_running(self) -> bool:
        """Returns True if the stopwatch is running, False otherwise."""
        return self.start_time != 0

    def get_time(self) -> str:
        """Returns the formatted elapsed time as a string in the format 'H:MM:SS.mmm'."""
        elapsed: float = float(self._update())
        hours: float
        rem: float
        minutes: float
        seconds: float
        hours, rem = divmod(elapsed, 3600)
        minutes, seconds = divmod(rem, 60)
        milliseconds: float = (seconds - int(seconds)) * 1000
        return (
            f"{int(hours):01}:"
            f"{int(minutes):02}:"
            f"{int(seconds):02}."
            f"{int(milliseconds):03}"
        )
