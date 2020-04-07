import imgkit
import os

path = os.getcwd()
LOCAL_URLs_PATH = 'downloaded_pages'
RENDERED_IMGS_PATH = 'rendered_images'

def render_images():
    filenames_PATH = os.path.join(path,LOCAL_URLs_PATH)
    filenames = os.listdir(filenames_PATH)
    
    for filename in filenames:
        local_URL = os.path.join(filenames_PATH, filename)
        render_PATH = os.path.join(path, RENDERED_IMGS_PATH)
        imgkit.from_file(local_URL, os.path.join(render_PATH, filename[:-6]+'.jpg'))


render_images()

#URL = "cdc.gov/coronavirus/2019-ncov/faq.html"

#imgkit.from_url(URL, 'out.jpg')
#imgkit.from_file(URL, URL[:-6]+'.jpg')
#imgkit.from_string('Hello!', 'out.jpg')

