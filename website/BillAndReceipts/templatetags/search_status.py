from django import forms, template

register = template.Library()

@register.filter
def search_year(personal_bill, year):
    return personal_bill.filter(year = year)

@register.filter
def search_month(personal_bill, month):
    return personal_bill.filter(month = month)

@register.filter
def search_status(personal_bill, status):
    return personal_bill.filter(status = status)

@register.simple_tag
def update_variable(value):
    """Allows to update existing variable in template"""
    return value

@register.simple_tag
def update_condition(value):
    """Allows to update existing variable in template"""
    return value

