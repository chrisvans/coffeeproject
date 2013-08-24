from django.db import models

# Create your models here.


# Use a model manager here to return orders based on paid or delivered booleans.


def parse_order_info(order_object):
    # Expects a string of order information, where each coffee order type is separated by commas,
    # and each order information element is separated by semicolons.
    # Returns a list with a nested list for each coffee order type,
    # with separated information elements in each list.
    # Validation of a proper string is not done here, but before this function is called.
    list_parse = order_object.strip().split(',')
    orders_list = []

    for single_order in list_parse:
        single_order_array = single_order.split(';')
        orders_list.append(single_order_array)
        single_order_list = []

    return orders_list

# Expected use -> parse_order_info('miralvalle;32oz Growler;5;14.00,villa sarchi;16oz Growler;5;12.00')