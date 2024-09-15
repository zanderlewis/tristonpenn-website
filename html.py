import os
from datetime import datetime

dir_path = './images'
ignore_dir = './images/ignore'
html = ''

def get_age(birthdate):
    # YYYY-MM-DD
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def imgs():
    html = ''
    for root, dirs, files in os.walk(dir_path):
        # Skip the ignore directory
        if ignore_dir in root:
            continue
        for filename in files:
            if filename.lower().endswith(('.jpg', '.png', '.jpeg')):
                relative_path = os.path.relpath(os.path.join(root, filename), dir_path)
                html += f'''
                    <div class="image-container">
                        <a target="_blank" href="images/{relative_path}">
                            <img src="images/{relative_path}" alt="Gallery Image" loading="lazy">
                        </a>
                    </div>
                '''
            else:
                raise Exception(f"Incorrect file type for file `{filename}`")
    return html

def main():
    with open('gallery.html', 'w') as f:
        # Get code from template.html
        with open('template.html', 'r') as template:
            html = template.read()
        # Replace the placeholder with the images
        html = html.replace('{{images}}', imgs())
        html = html.replace('{{age}}', str(get_age('2008-06-06')))
        # Write the final code to gallery.html
        f.write(html)

if __name__ == '__main__':
    main()