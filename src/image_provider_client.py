import requests
from requests import HTTPError
from requests.exceptions import RequestException
# todo: wroong imports order
from constants import IMAGE_SERVICE_HOST

from exceptions import RequestsNotFoundException, RequestsUnavailableException

from multiprocessing.pool import ThreadPool

class ImageReaderClient:
    def __init__(self, host: str):
        self.host = host

    def get_image(self, image_id):
        try:
            response = requests.get(
                f'{self.host}/images/{image_id}',
                timeout=10
            )
            response.raise_for_status()
            return response.content
        except HTTPError as http_exception:
            if http_exception.response.status_code == 404:
                raise RequestsNotFoundException from http_exception
            if http_exception.response.status_code // 100 == 5:
                raise RequestsUnavailableException from http_exception
        except RequestException as requests_exception:
            raise RequestsUnavailableException

    def get_images(self, image_ids):
        images = []
        with ThreadPool() as pool:
            for image in pool.map(self.get_image, image_ids):
                images.append(image)
        return images


if __name__ == '__main__':
    # client = ImageReaderClient(host='http://178.154.220.122:7777')
    client = ImageReaderClient(host=IMAGE_SERVICE_HOST)
    res = client.get_image(9965)
    print(res)
