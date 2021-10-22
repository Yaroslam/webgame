from django import template

register = template.Library()

def create_range(value, start_index=0):
    return range(start_index, value+start_index)

register.filter('create_range', create_range)