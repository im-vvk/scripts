"""
calculates total video length of files having video extension(.mp4 extension name to be changed
for different video format) including files in current as well as all sub-directories.
"""

import moviepy.editor
import os


extension_name = '.mp4'


# Converts into more readable format
def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600

    mins = seconds // 60
    seconds %= 60

    return hours, mins, seconds


# return duration of the video in seconds
def get_videolen(path):
    video = moviepy.editor.VideoFileClip(path)

    # Contains the duration of the video in terms of seconds
    video_duration = int(video.duration)

    return video_duration


path = "."

total_len = 0
# dirs=directories
for (root, dirs, file) in os.walk(path):
    cdir_len = 0

    for f in sorted(file):
        if extension_name in f:
            cdir_len += get_videolen(root+'/'+f)

    if cdir_len > 0:
        hours, mins, secs = convert(cdir_len)
        print(root.split('/')[-1], f"{hours}:{mins}:{secs}")

    total_len += cdir_len


hours, mins, secs = convert(total_len)
print("Total Duration", f"{hours}:{mins}:{secs}")
