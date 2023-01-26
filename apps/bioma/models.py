from django.db import models

class BiomeModel(models.Model):
    class Meta:
        ordering=['name',]
        
    name = models.CharField(max_length=50, unique=True, primary_key=True, verbose_name='name')
    description = models.TextField(verbose_name='Description')

    def __str__(self) -> str:
        return self.name