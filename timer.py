import pygame

class Timer:
    def __init__(self, duration):
        """
        Initialize a timer with a given duration in milliseconds.

        Args:
            duration: Time in milliseconds between events
        """
        self.duration = duration
        self.start_time = pygame.time.get_ticks()

    def is_ready(self):
        """
        Check if the timer has elapsed.

        Returns:
            True if the duration has passed, False otherwise
        """
        current_time = pygame.time.get_ticks()
        return current_time - self.start_time >= self.duration

    def reset(self):
        """Reset the timer to the current time."""
        self.start_time = pygame.time.get_ticks()
