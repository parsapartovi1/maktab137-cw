from django.db import models

# Create your models here.


class Patient(models.Model):

    first_name = models.CharField(
        max_length=24,
        verbose_name='first name',
        help_text='Enter your first name',
        blank=False,
        null=False
    )

    last_name = models.CharField(
        max_length=24,
        verbose_name='last name',
        help_text='Enter your last name',
        blank=False,
        null=False
    )

    national_id = models.CharField(
        max_length=10,
        verbose_name='national id',
        help_text='Your national id',

    )

    birthdate = models.DateField(
        verbose_name='birthdate',
        help_text='Your birthdate',
    )

    number = models.CharField(
        max_length=11,
        verbose_name='number',
        help_text='Enter your number',
        blank=False,
        null=False
    )

    create_date = models.DateTimeField(
        verbose_name='creation date',
        auto_now_add=True
    )

    last_update = models.DateTimeField(
        verbose_name='last update',
        auto_now=True
    )
