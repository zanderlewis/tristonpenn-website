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
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.png') or filename.lower().endswith('.jpeg'):
            html += f'''
                <div class="image-container">
                    <a target="_blank" href="{filename}">
                        <img src="{filename}" alt="Gallery Image" loading="lazy">
                    </a>
                </div>
            '''
        else:
            raise Exception(f"Incorrect file type for file `{filename}`")
    return html

def main():
    with open('gallery.html', 'w') as f:
        # find the line with `{{gallery}}` and replace it with the generated html
        f.write(open('template.html').read().replace('{{gallery}}', html))
        # write age from birthday and replace `{{age}}` with the calculated age
        f.write(open('template.html').read().replace('{{age}}', str(get_age('2008-06-06'))))
                
if __name__ == '__main__':
    main()