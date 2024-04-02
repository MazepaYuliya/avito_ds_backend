import requests


class ImageReaderClient:
    def __init__(self, host: str):
        self.host = host

    def get_image(self, image_id):
        response = requests.get(
            f'{self.host}/images/{image_id}',
            timeout=10
        )
        response.raise_for_status()
        return response.content

    def get_images(self, image_ids):
        images = []
        for image_id in image_ids:
            images.append(self.get_image(image_id))
        return images


if __name__ == '__main__':
    client = ImageReaderClient(host='http://178.154.220.122:7777')
    res = client.get_image(9965)
    print(res)
