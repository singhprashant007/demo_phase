from gtts import gTTS
import os

def text_to_audio(text, output_filename):
    tts = gTTS(text)
    tts.save(output_filename)

    # Play the generated audio file
    os.system(f"start {output_filename}")  # For Windows
    # For Linux or macOS, you can use: os.system(f"xdg-open {output_filename}")

# Input text
input_text = "Hello, this is a text-to-speech example."

# Output audio file name
output_file = "output_audio.mp3"

# Convert text to audio
text_to_audio(input_text, output_file)
