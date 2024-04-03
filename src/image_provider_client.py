"""Client for getting images"""
import requests
from requests import HTTPError
from requests.exceptions import RequestException

from multiprocessing.pool import ThreadPool

from constants import IMAGE_SERVICE_HOST
from exceptions import RequestsNotFoundException, RequestsUnavailableException


class ImageReaderClient:
    """Class for getting images from external service"""
    def __init__(self, host: str):
        """Initialization of ImageReaderClient"""
        self.host = host

    def get_image(self, image_id):
        """Getting one image"""
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
        """Getting a list of images"""
        images = []
        with ThreadPool() as pool:
            for image in pool.map(self.get_image, image_ids):
                images.append(image)
        return images


if __name__ == '__main__':
    client = ImageReaderClient(host=IMAGE_SERVICE_HOST)
    res = client.get_image(9965)
    print(res)
