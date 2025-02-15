from audio_transcription import AudioTranscription
from file_lister import FileLister

class Manager:
  def __init__(self, input_path: str):
    self.input_path = input_path
    self.files = []

  def get_files(self):
    fl = FileLister(self.input_path)
    return fl.get_files()
  
  def transcribe_files(self):
    for file in self.files:
      audio_transcription = AudioTranscription(file)
      audio_transcription.start_transcription()

  def process(self):
    self.files = self.get_files()
    self.transcribe_files()

def main():
  # Specify the path to your audio file(s) here
  input_path = r''

  mgr = Manager(input_path)
  mgr.process()

if __name__ == "__main__":
  main()