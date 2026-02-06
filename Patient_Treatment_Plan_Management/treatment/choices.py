from django.db import models


class TreatmentState(models.TextChoices):
        UNDETERMINED = 'u' , 'undetermined'
        GOOD = 'g' , 'good'
        FAIR = 'f' , 'fair'
        SERIOUS = 's' , 'serious'
        CRITICAL = 'c' , 'critical'


class Treatmenttype(models.TextChoices):
        Physiotherapy = 'PYSIOTHERAPY'
        Consulting = "CONSULTING"
        Drugtherapy = "DRUGTHERAPY"
        Exercisetherapy = "EXERCISETHERAPY"

class Treatmentstatus(models.TextChoices):
        Held = "HELD"
        Cancelled = "CANCELLED"