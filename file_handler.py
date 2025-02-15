import os
import uuid

class FileHandler:
  @staticmethod
  def temp_file_name(extension: str) -> str:
    return f'{uuid.uuid4()}.{extension}'
  
  @staticmethod
  def output_file_name(input_file_path: str) -> str:
    base_name = os.path.splitext(os.path.basename(input_file_path))[0]
    dir_name = os.path.basename(os.path.dirname(input_file_path))
    filename = f"{dir_name}__{base_name}.txt"
    return 'output/' + filename