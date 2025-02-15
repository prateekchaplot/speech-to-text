# Import necessary libraries
import subprocess
import os
import speech_recognition as sr
import uuid
import time

class AudioTranscription:
  # Initialize the class with input file path
  def __init__(self, input_file_path):
    self.input_file_path = input_file_path
    self.temporary_wav_file = f"{uuid.uuid4()}.wav"
    self.output_file_name = 'output/' + os.path.splitext(os.path.basename(input_file_path))[0] + ".txt"

  # Convert MP3 to WAV using ffmpeg
  def convert_mp3_to_wav(self):
    command = ["ffmpeg", "-i", self.input_file_path, self.temporary_wav_file]
    subprocess.run(command)

  # Initialize a speech recognition object
  def initialize_recognizer(self):
    return sr.Recognizer()

  # Recognize speech in the temporary WAV file
  def recognize_speech(self):
    try:
      r = self.initialize_recognizer()
      with sr.AudioFile(self.temporary_wav_file) as source:
        audio_data = r.record(source)
        text = r.recognize_sphinx(audio_data)
        return text
    except sr.UnknownValueError:
      print("Sorry, could not understand the audio.")
    except sr.RequestError:
      print("Could not request results; check your internet connection.")

  # Save the recognized transcript to a file
  def save_transcript(self, text):
    with open(self.output_file_name, "w") as file:
      file.write(text)

  # Start the transcription process
  def start_transcription(self):
    self.start_time = self.get_time()
    self.convert_mp3_to_wav()
    text = self.recognize_speech()
    self.save_transcript(text)
    self.end_time = self.get_time()
    self.post_cleanup()
    self.calculate_elapsed_time()

  # Get the current time in seconds
  def get_time(self):
    return time.time()

  # Calculate the elapsed time since the start of transcription
  def calculate_elapsed_time(self):
    elapsed_time = self.end_time - self.start_time
    print(f'Time taken to execute: {elapsed_time:.2f} seconds')

  # Perform cleanup
  def post_cleanup(self):
    self.delete_wav_file()

  # Delete temporary WAV file
  def delete_wav_file(self):
    if os.path.exists(self.temporary_wav_file):
      os.remove(self.temporary_wav_file)
    print("Temporary WAV file deleted.")

def main():
  input_file_path = ''  # Specify the path to your audio file here
  audio_transcription = AudioTranscription(input_file_path)
  audio_transcription.start_transcription()

if __name__ == "__main__":
  main()