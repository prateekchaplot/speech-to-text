import os

class FileLister:
  def __init__(self, input_path: str):
    self.extensions = ['.mp3', '.mp4']
    self.input_path = input_path

  def _get_all_files_in_directory(self) -> list[str]:
    file_list = []
    for root, _, files in os.walk(self.input_path):
      for file in files:
        if not file.endswith(tuple(reversed(self.extensions))):
          continue
        file_list.append(os.path.join(root, file))
    return file_list

  def get_files(self) -> list[str]:
    if os.path.isfile(self.input_path):
      return [self.input_path]
    elif os.path.isdir(self.input_path):
      return self._get_all_files_in_directory()
    else:
      return []