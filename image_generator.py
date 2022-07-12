import os.path
import zipfile
import random

def _get_image(extension) -> str:
    """Get random image from template desire extension (jpg, png)"""
    images: list = []
    for root, dirs, files in os.walk('images/'):
        for f in files:
            if f[-4:] == f'.{extension}':
                images.append(f)
    if images:
        return(f'images/{random.choice(images)}')
    else:
        print(f'No found template images')


def generate_image(size: int, image_type: str = 'jpg') -> None:
    """ Generate binary file and create zip archive """
    if os.path.exists(f"generated/{size}.{image_type}"):
       return
    size_byte: int = size*1024*1024
    filename: str = 'workload.dat'
    generated_zip: str  = 'generated.zip'
    with open('%s'%filename, 'wb') as fout:
        fout.write(os.urandom(size_byte)) #1
    with zipfile.ZipFile(generated_zip, mode="w") as archive:
        archive.write(filename)
    os.remove(filename)
    """ Merge zip and jpg file """
    jpg_file = open(_get_image(image_type), 'rb')
    jpg_data = jpg_file.read()
    jpg_file.close()
    zip_file = open(generated_zip, 'rb')
    zip_data = zip_file.read()
    zip_file.close()
    # merge zip-jpg
    new_file = open(f'generated/{size}.{image_type}', 'wb')
    new_file.write(jpg_data)
    new_file.write(zip_data)
    new_file.close()
    # Remove generated zip
    os.remove(generated_zip)


if __name__ == '__main__':
    input_size = input ("Enter the desired image size (Mb): ")
    try:
        image_size = int(input_size)
    except ValueError:
        print("Not interesting value, need number(int)")
    if image_size < 1000:
        generate_image(image_size)
    else:
        print('Sorry, dont want to do this')

