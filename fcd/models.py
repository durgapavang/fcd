from django.db import models

# Create your models here.
class User(models, Models):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	class meta:
		db_table = "user"