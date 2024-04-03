from marshmallow import Schema, fields, ValidationError


class ReadPlateNumberSchema(Schema):
    image_ids = fields.List(fields.Integer(), required=True)


    @staticmethod
    def validate_image_ids(data):
        if not data:
            raise ValidationError('No image IDs provided.')
        for image_id in data:
            if not isinstance(image_id, int):
                raise ValidationError('Image IDs must be integers.')

read_plate_number_schema = ReadPlateNumberSchema()
