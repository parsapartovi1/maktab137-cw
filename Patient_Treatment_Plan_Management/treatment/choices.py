from django.db import models


class TreatmentState(models.TextChoices):
        UNDETERMINED = 'u' , 'undetermined'
        GOOD = 'g' , 'good'
        FAIR = 'f' , 'fair'
        SERIOUS = 's' , 'serious'
        CRITICAL = 'c' , 'critical'