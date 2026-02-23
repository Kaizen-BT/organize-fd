Organizer_Settings = dict[str, list[str]]


class Organizer:
    """Used to create Organizer instances to organize a directory."""

    def __init__(self, settings: Organizer_Settings) -> None:
        """Instantiate the organizer with the given mapping.

        Args:
            settings (Organizer_Settings): A dictionary where the keys
            are the name of the directory and the values are lists of
            file extensions
        """
        self.settings = settings

    def print_settings(self) -> None:
        """Helper method to display what files will be moved to which directory."""
        for destination, extension_list in self.settings.items():
            print(f"{destination} will hold:\n{extension_list}")
