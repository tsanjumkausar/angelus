# THIS CODE USES pydub and noisereduce libraries to remove background noise and enhance the voice in an audio file on Windows:
# First, install the pydub and noisereduce libraries using pip:
pip install noisereduce
# Create a new Python file and import necessary libraries:
pip install pydub noisereduce
# use the following code to load an audio file, remove the background noise, and save the enhanced audio to a new file:
from pydub import AudioSegment
import noisereduce as nr

# Open the audio file
audio = AudioSegment.from_file('path_to_your_audio_file.wav', format='wav')

# Extract the audio data as a NumPy array
audio_data = np.array(audio.get_array_of_samples())

# Remove background noise
reduced_noise = nr.reduce_noise(audio_data, noise_clip=audio_data[10000:20000])

# Enhance the voice using a low-cut filter
lowcut = 150
b, a = signal.butter(4, [lowcut / (sample_rate / 2), 1], btype='band')
enhanced_voice = signal.filtfilt(b, a, reduced_noise)

# Create a new AudioSegment object with the enhanced voice
enhanced_audio = AudioSegment(
    data=enhanced_voice.astype(np.int16),
    sample_width=audio.sample_width,
    frame_rate=audio.frame_rate,
    channels=audio.channels
)

# Save the enhanced audio to a new file
enhanced_audio.export('path_to_your_output_file.wav', format='wav')
