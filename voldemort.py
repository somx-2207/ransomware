import os
files = []


for file in os.listdir():
    if file == "voldemort.py":
        continue
    files.append(file)

print(files)
