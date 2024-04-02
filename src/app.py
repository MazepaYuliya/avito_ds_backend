import logging
from flask import Flask, jsonify, request
from models.plate_reader import PlateReader, InvalidImage
from image_provider_client import ImageReaderClient
import logging
import io
from schema import read_plate_number_schema
from requests import HTTPError
from marshmallow import ValidationError

app = Flask(__name__)
plate_reader = PlateReader.load_from_file('./model_weights/plate_reader_model.pth')
image_provider_client = ImageReaderClient(host='http://178.154.220.122:7777')


@app.route('/')
def hello():
    user = request.args['user']
    return f'<h1 style="color:red;"><center>Hello {user}!</center></h1>'


@app.route('/greeting', methods=['POST'])
def greeting():
    if 'user' not in request.json:
        return {'error': 'field "user" not found'}, 400

    user = request.json['user']
    return {
        'result': f'Hello {user}',
    }


def get_auto_numbers_by_ids(image_ids):
    try:
        images = image_provider_client.get_images(image_ids)
    except HTTPError as e:
        status = e.response.status_code
        if status == 404:
            return jsonify({'error': 'Wrong image id'}), 404
        else:
            return jsonify({'error': 'Getting images error'}), status
    except Exception as e:
        # return jsonify({'error': 'Getting images error'}), 500
        return jsonify({'error': str(e)}), 500
        
    result = {}
    for ind, im in enumerate(images):
        im = io.BytesIO(im)
        image_id = image_ids[ind]

        try:
            auto_number = plate_reader.read_text(im)
        except InvalidImage:
            error_text = f'invalid image {image_id}'
            logging.error(error_text)
            return jsonify({'error': error_text}), 400

        result[image_id] = auto_number

    return result


@app.route('/readPlateNumber/<image_id>', methods=['GET'])
def read_plate_number(image_id:int):
    image_ids = [image_id]

    result = get_auto_numbers_by_ids(image_ids)

    return result
    # if isinstance(result, tuple):
    #     return result

    # return {
    #     'plate_number': result.get(image_id),
    # }


@app.route('/readPlateNumber', methods=['POST'])
def read_plate_numbers():
    
    try:
        data = read_plate_number_schema.load(
            request.json,
        )
        image_ids = data['image_ids']
        read_plate_number_schema.validate_image_ids(image_ids)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400 

    return get_auto_numbers_by_ids(image_ids)


if __name__ == '__main__':
    logging.basicConfig(
        format='[%(levelname)s] [%(asctime)s] %(message)s',
        level=logging.INFO,
    )

    # app.config['JSON_AS_ASCII'] = False
    app.json.ensure_ascii = False
    app.run(host='0.0.0.0', port=8080, debug=True)