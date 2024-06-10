# stringapp/models.py
from django.db import models

class StringCalculation(models.Model):
    input_string = models.CharField(max_length=255)
    max_f_value = models.IntegerField()

    def __str__(self):
        return f"{self.input_string} - {self.max_f_value}"
