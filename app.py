import os
from flask import Flask, request, render_template, send_file
from image_generator import generate_image

app = Flask(__name__)

URL = '127.0.0.1'

@app.route('/', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        image_size = request.form.get('image_size')
        image_type = request.form.get('image_type')
        generate_image(int(image_size), str(image_type))
        download_url = f"http://{URL}/downloads/{image_size}.{image_type}"
        context = {'size' : image_size, 'format' : image_type, 'url' : download_url}
        return render_template('index.html', context=context)
    return render_template('index.html')


@app.route('/downloads/<path:filename>', methods=['GET'])
def download(filename):
    uploads = 'generated/' + filename
    return send_file(uploads, as_attachment=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
