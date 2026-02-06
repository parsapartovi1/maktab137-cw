from django.db import models
from Patient.models import Patient
from choises import TreatmentState


class TreatmentPlan(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    Title = models.CharField(
        max_length=24,
        verbose_name="title",
        help_text="plese write the Title"

    )

    description = models.TextField(
        max_length=1024,
        verbose_name="deaciription",
        help_text="youcan wirte the somtings"
    )

    date = models.DateField(
        verbose_name="date",
        help_text=" please add the Date ")

    presence = models.BooleanField(
        verbose_name="presence",
        help_text="the status of  patient",
        default=True
    )

    new_plan = models.TextField(
        max_length=1024,
        verbose_name="previews_plan",
        help_text="the previews"
    )

    previews_plan = models.ForeignKey(
        'self.new_plan',
        on_delete=models.CASCADE,
        related_name="new_plan"
    )

    state = models.CharField(
        max_length=1,
        choices=TreatmentState.choises,
        default=TreatmentState.GOOD

    )

    create_date = models.DateTimeField(
        verbose_name='create date',
        auto_now_add=True
    )

    update_date = models.DateTimeField(
        verbose_name='update date',
        auto_now=True
    )

    def __str__(self):
        return str(self.Title) + "-" + str(self.patient)
