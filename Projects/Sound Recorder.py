import sounddevice
from scipy.io.wavfile import write

# Enter Frequency
Frequency = 44100

# Ask User for Duration
Duration = int(input('Enter duration in seconds: '))

# Record Voice
Rec = sounddevice.rec(int(Duration * Frequency), samplerate=Frequency, channels=2)
sounddevice.wait()

# Save to specified Folder
path = "C:/Users/pc/OneDrive/Desktop/Python With Mosh/Wav Files/Record.wav"

# Save as File in Folder
write(path, Frequency, Rec)