import os

dir_path = './images'
html = ''

for filename in os.listdir(dir_path):
    if filename.lower().endswith('.jpg') or filename.lower().endswith('.png'):
        html += f'<img src="images/{filename}" alt="Gallery Image">\n'
    else:
        raise Exception(f"Incorrect file type for file `{filename}`")

with open('gallery.html', 'w') as f:
    f.write(html)