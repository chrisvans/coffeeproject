from django.db import models
from core.models import TimeStampedModel, ExtraModelMethods


# Use a model manager here to return orders based on paid or delivered booleans.

class ColdBrewOrder(TimeStampedModel, ExtraModelMethods):
    info = models.CharField(max_length=1000)
    notes = models.CharField(max_length=500)
    cost = models.CharField(max_length=50)
    is_delivered = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    user = models.ForeignKey('users.CoffeeUser')
    shipping_address = models.ForeignKey('shipping_data.ShippingAddress')

    def __unicode__(self):
        return unicode(self.user.email + " " + str(self.is_delivered) + " " + str(self.is_paid))

    def parse_order_info(self):
        """
        Expects a string of order information, where each coffee order type is separated by commas,
        and each order information element is separated by semicolons.
        Returns a list with a nested list for each coffee order type,
        with separated information elements in each list.
        Validation of a proper string is not done here, but before this function is called.
        """

        list_parse = self.info.strip().split(',')
        orders_list = []

        for single_order in list_parse:
            single_order_array = single_order.split(';')
            orders_list.append(single_order_array)
            single_order_list = []

        return orders_list

    # Expected use -> parse_order_info('miralvalle;32oz Growler;5;14.00,villa sarchi;16oz Growler;5;12.00')
    # Expected result -> [['miralvalle', '32oz Growler', '5', '14.00'], ['villa sarchi', '16oz Growler', '5', '12.00']]