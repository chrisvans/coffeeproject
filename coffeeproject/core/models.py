from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating ``created`` and ``modified`` fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
    	abstract = True

class ExtraModelMethods(models.Model):
	"""
    Extra methods applied to classes built around easy information display and utility.
	"""

	def attributes(self):
		"""
		Prints all attributes of a class ->  Name : Attribute_Value : Attribute_Type
		"""
		for field in self._meta.fields:
			attribute_item = getattr(self, field.name)
			print str(field.name) + " : " + str(attribute_item) + " : " + str(type(attribute_item))

	class Meta:
		abstract = True