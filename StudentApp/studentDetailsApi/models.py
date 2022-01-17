from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.


def validate_age(value):
    if value < 0:
        raise ValidationError(
            {'title': f"Enter valid age, given age is {value}"}
        )


SHIRT_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)

SECTIONS = (
    ('P', 'Primary'),
    ('U', 'Upper-Primary')
)


class StudentTShirtDetails(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[validate_age])
    email_id = models.EmailField()
    section = models.CharField(max_length=1, choices=SECTIONS)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    guardian_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
