import os
from datetime import datetime

dir_path = './images'
html = ''

def get_age(birthdate):
    # YYYY-MM-DD
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    # convert 
    return age

def imgs():
    html = ''
    for filename in os.listdir(dir_path):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.png') or filename.lower().endswith('.jpeg') and not filename == 'backstage.png' and not filename == 'favicon.png':
            html += f'''
                <div class="image-container">
                    <a target="_blank" href="images/{filename}">
                        <img src="images/{filename}" alt="Gallery Image" loading="lazy">
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