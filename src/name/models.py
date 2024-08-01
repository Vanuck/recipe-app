from django.db import models

# model for recipe name.

class recipe_name(models.Model):
    recipe_name= models.CharField(max_length=50)
    recipe_name= models.TextField()


    def __str__(self):
        return str(self.name)
