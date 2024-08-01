from django.db import models

# Model for recipe.

class Recipe(models.Model):
    # class attributes
    name = models.CharField(max_length=50)
    ingredients = models.CharField(
        max_length=225, help_text="Enter the ingredients, separated by a comma"
    )
    description = models.TextField(max_length=225, help_text="Enter a description")
    cooking_time = models.IntegerField(help_text="Enter cooking time in minutes")

     # string representation
    def __str__(self):
        return str(self.name)
