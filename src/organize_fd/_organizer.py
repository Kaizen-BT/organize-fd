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

    def get_target_directory(self, source_path: Path) -> str | None:
        """Find the directory in which the supplied file will be moved.

        This function is unpredictable if the file-extension of the file
        is repeated in multiple directories.
        This function does not do any existence checks. It simply resolves
        the expected directory based on the Path objects suffix attribute

        Args:
            source_path (Path): Path object representation of any file/folder

        Returns:
            str | None: The name of the directory the file will be moved
            to or None if no directory handles the file's file-extensions
        """
        for directory, extensions in self.settings.items():
            if source_path.is_file() and source_path.suffix in extensions:
                return directory
        return None

    def dry_run(self) -> None:
        """Displays affected files and where they will be moved.

        This method does not touch the file system it is for
        a quick run to check what and where files will be moved

        Raises:
            RuntimeError: get_target_directory SHOULD return
            a valid directory string, if it does not then something
            spooky is going on
        """
        for source_path in self.affected_paths():
            destination = self.get_target_directory(source_path)

            if not destination:
                raise RuntimeError("Something is super not right")

            destination_path = self._cwd / destination

            print(f"{source_path.name} will be moved to {destination_path}")
