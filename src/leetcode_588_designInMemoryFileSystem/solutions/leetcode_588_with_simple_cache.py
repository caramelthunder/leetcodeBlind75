from typing import List, Union


class Directory:
    def __init__(self, name: str):
        self.name = name
        self.content = {}

    def list_content(self) -> List[str]:
        return sorted(list(self.content.keys()))


class File:
    def __init__(self, name: str, content=""):
        self.name = name
        self.content = content

    def read_content(self) -> str:
        return self.content

    def write_content(self, new_content: str):
        self.content += new_content


class FileSystem:
    def __init__(self):
        self.root = Directory("/")
        self.recent_paths = {}

    def ls(self, path: str) -> List[str]:
        """
        Time Complexity:
        O(m + n log n) where m is the depth of the directory in the file system hierarchy
        and n is the number of items in the directory.

        Space Complexity:
        O(m)
        """
        curr_dir = self._navigate_path(self._get_dir_names(path))
        if isinstance(curr_dir, File):
            return [curr_dir.name]
        elif isinstance(curr_dir, Directory):
            return curr_dir.list_content()
        return []

    def mkdir(self, path: str) -> None:
        """
        Time Complexity:
        O(m) where m is the depth of the directory in the file system hierarchy.

        Space Complexity:
        O(m)
        """
        self._navigate_path(
            self._get_dir_names(path), create_if_not_exist=True
        )

    def addContentToFile(self, filePath: str, content: str) -> None:
        """
        Time Complexity:
        O(m + len(content)) where m is the depth of the directory in the file system hierarchy.

        Space Complexity:
        O(m)
        """
        dir_names = self._get_dir_names(filePath)
        file_name = dir_names.pop()
        curr_dir = self._navigate_path(dir_names, create_if_not_exist=True)

        if isinstance(curr_dir, Directory):
            file = curr_dir.content.get(file_name, File(file_name))
            file.write_content(content)
            curr_dir.content[file_name] = file

    def readContentFromFile(self, filePath: str) -> str:
        """
        Time Complexity:
        O(m) where m is the depth of the directory in the file system hierarchy.

        Space Complexity:
        O(m)
        """
        curr_dir = self._navigate_path(self._get_dir_names(filePath))
        if isinstance(curr_dir, File):
            return curr_dir.read_content()
        return ""

    def _get_dir_names(self, path: str) -> List[str]:
        """
        Time Complexity:
        O(len(path))

        Space Complexity:
        O(len(path))
        """
        path = path.strip("/")
        return [] if path == "" else path.split("/")

    def _navigate_path(
        self, dir_names: List[str], create_if_not_exist=False
    ) -> Union[Directory, File, None]:
        """
        Time Complexity:
        O(m), where m is the length of dir_names.

        Space Complexity:
        O(m), where m is the length of dir_names.
        """
        path = "/".join(dir_names)
        if path in self.recent_paths:
            return self.recent_paths[path]

        curr_dir = self.root
        for name in dir_names:
            if isinstance(curr_dir, Directory):
                if name not in curr_dir.content:
                    if create_if_not_exist:
                        curr_dir.content[name] = Directory(name)
                    else:
                        return None
                curr_dir = curr_dir.content[name]
            else:
                return None  # Files cannot contain other directories or files

        self.recent_paths[path] = curr_dir
        return curr_dir
