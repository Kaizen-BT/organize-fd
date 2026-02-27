"""Test Script.

This assumes the library is installed in edit mode
"""

from organize_fd import Organizer

if __name__ == "__main__":
    organizer = Organizer(
        settings={"Documents": [".pdf", ".py"], "Music": [".mp3", ".py"]}
    )

    for aff_path in organizer.affected_paths():
        print(
            f"{aff_path.name} will be moved to \
            {organizer.get_target_directory(aff_path)}"
        )
