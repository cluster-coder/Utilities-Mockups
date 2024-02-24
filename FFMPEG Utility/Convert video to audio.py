import os

a=input('path \n')
b=[]

os.chdir(a)

for path, subfolders, files in os.walk(a):
    for file in files:
        if file.endswith('.mp4'):
            b.append(file)

for video in b:
    os.system(f"ffmpeg -i \"{video}\" -vn \"{video[:-1]+'3'}\"")
