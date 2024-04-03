"""Module for schemas for validating views input"""
from marshmallow import Schema, fields, ValidationError


class ReadPlateNumberSchema(Schema):
    """Schema for validating input of view read_plate_numbers"""
    image_ids = fields.List(fields.Integer(), required=True)


    @staticmethod
    def validate_image_ids(data):
        """Additional validation of images ids"""
        if not data:
            raise ValidationError('No image IDs provided.')
        for image_id in data:
            if not isinstance(image_id, int):
                raise ValidationError('Image IDs must be integers.')

read_plate_number_schema = ReadPlateNumberSchema()
