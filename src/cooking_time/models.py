from django.db import models

# model for cooking time.

class cooking_time(models.Model):
    cooking_time = models.CharField(max_length=120)
    recipe_cooking_time = models.TextField()


    def __str__(self):
        return str(self.name)