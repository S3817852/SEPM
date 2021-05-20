from django import forms, template

register = template.Library()

@register.filter
def search_empty(empty_list, house_id):
    return empty_list.filter(house_id = house_id)

@register.filter
def search_rented(rented_list, house_id):
    return rented_list.filter(house_id = house_id)