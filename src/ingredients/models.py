from django.db import models

# model for ingredients.

class ingredients(models.Model):
    ingredients= models.CharField(max_length=225)
    recipe_ingredients= models.TextField()


    def __str__(self):
        return str(self.name)