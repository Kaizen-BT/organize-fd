"""Test Script.

This assumes the library is installed in edit mode
"""

from organize_fd import Organizer

if __name__ == "__main__":
    organizer = Organizer(settings={"Documents": [".pdf"]})
    organizer.print_settings()
