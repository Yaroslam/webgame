from rest_framework import serializers


def not_null(value):
    if value == None:
        raise serializers.ValidationError(f'value is null')
    else:
        return value


def must_be_int(value):
    if type(value) != int:
        raise serializers.ValidationError('value must be int')
    else:
        return value


def name_must_be_eng(value):
    for i in value:
        if ord(i) not in range(65, 91) and ord(i) not in range(96, 123):
            raise serializers.ValidationError('name must be written by eng letters')
    return value
