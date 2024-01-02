from moviepy.editor import VideoFileClip
import speech_recognition as sr


def transcribe_mp4_audio(mp4_file_path):
    # Convert MP4 to WAV
    video_clip = VideoFileClip(mp4_file_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile("audio.wav", codec='pcm_s16le')

    # Transcribe the converted audio
    recognizer = sr.Recognizer()
    with sr.AudioFile("audio.wav") as source:
        audio_data = recognizer.record(source)

    try:
        transcription = recognizer.recognize_google(audio_data, language="en-US")
        return transcription
    except sr.UnknownValueError:
        return "Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"
    
    

# Example usage
#mp4_file_path = "/Users/kingyhrash/Downloads/l4.mp4"
#transcription = transcribe_mp4_audio(mp4_file_path)
#print("Transcription:")




