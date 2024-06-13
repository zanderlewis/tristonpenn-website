import os

dir_path = './images'
count = 1

for filename in os.listdir(dir_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        new_filename = f'image{count}{os.path.splitext(filename)[1]}'
        os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename))
        count += 1