import moviepy
import moviepy.editor
# Replace the parameter with the location of your file
video = moviepy.editor.VideoFileClip("abcdefg.mp4")

audio = video.audio
# Replace the parameter with the location along with filename
audio.write_audiofile("abcdefg.wav")
