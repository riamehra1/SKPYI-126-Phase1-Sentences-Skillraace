import pyaudio
import wave
import threading
import time
import os

class VoiceRecorder:
    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
        self.RECORD_SECONDS = 0
        self.WAVE_OUTPUT_FILENAME = "output.wav"
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.recording = False
        self.paused = False

    def start_recording(self):
        self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                                      rate=self.RATE, input=True,
                                      frames_per_buffer=self.CHUNK)
        self.recording = True
        self.paused = False
        print("recording started")
        self.record_thread = threading.Thread(target=self.record_audio)
        self.record_thread.start()

    def pause_recording(self):
        self.paused = True
        print("recording paused")

    def resume_recording(self):
        self.paused = False
        print("recording resumed")

    def stop_recording(self):
        self.recording = False
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        print("recording stopped")
        self.save_recording()

    def record_audio(self):
        while self.recording:
            if not self.paused:
                data = self.stream.read(self.CHUNK)
                self.frames.append(data)
            time.sleep(0.01)

    def save_recording(self):
        waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(self.frames))
        waveFile.close()
        print("recording saved")

    def get_recording_time(self):
        return len(self.frames) / (self.RATE / self.CHUNK)

    def get_recording_status(self):
        if self.recording:
            if self.paused:
                return "paused"
            else:
                return "recording"
        else:
            return "stopped"

def main():
    recorder = VoiceRecorder()
    while True:
        print("1. Start recording")
        print("2. Pause recording")
        print("3. Resume recording")
        print("4. Stop recording")
        print("5. Get recording time")
        print("6. Get recording status")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            recorder.start_recording()
        elif choice == "2":
            recorder.pause_recording()
        elif choice == "3":
            recorder.resume_recording()
        elif choice == "4":
            recorder.stop_recording()
        elif choice == "5":
            print("Recording time: {:.2f} seconds".format(recorder.get_recording_time()))
        elif choice == "6":
            print("Recording status: {}".format(recorder.get_recording_status()))
        elif choice == "7":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()