"""Test Script.

This assumes the library is installed in edit mode
"""

from organize_fd import Organizer

if __name__ == "__main__":
    organizer = Organizer(settings={"Documents": [".pdf"], "Music": [".mp3", ".py"]})
    print(list(files.name for files in organizer.affected_paths()))
