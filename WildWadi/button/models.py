from django.db import models

class Articles(models.Model):
    title = models.CharField("Name", max_length=100)
    full_text = models.TextField("Description")
    price = models.CharField("Price", max_length=200)
    date = models.DateTimeField("Date")

    def __str__(self):
        return f'Package: {self.title}'

    class Meta:
        verbose_name = "Ticket type"
        verbose_name_plural = "Ticket types"
