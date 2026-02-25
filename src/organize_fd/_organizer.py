from collections.abc import Generator
from pathlib import Path

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
        self._target_extensions = set(
            ext for extensions in settings.values() for ext in extensions
        )
        self._cwd = Path.cwd()

    def affected_paths(self) -> Generator[Path, None, None]:
        """Returns the affected files as Path objects.

        Note: The result is evaluated at invocation

        Returns:
            Generator[Path, None, None]: Generator of all files that will be affected by
            the organizer
        """
        return (
            file_item
            for file_item in self._cwd.iterdir()
            if file_item.suffix in self._target_extensions
        )
