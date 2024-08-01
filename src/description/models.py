from django.db import models

# model for description.

class description(models.Model):
    description= models.CharField(max_length=225)
    recipe_description= models.TextField()


    def __str__(self):
        return str(self.name)