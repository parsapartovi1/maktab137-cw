from django.db import models
from Patient.models import Patient
from treatment.choices import TreatmentState, Treatmenttype , Treatmentstatus
from django.core.validators import MinValueValidator, MaxValueValidator


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



class Treatmentsession(models.model):

    treatment_plan = models.ForeignKey(
        "TreatmentPlan",
        verbose_name = "treatmentplan",
        help_text = "Treatment plan according to this session",
        on_delete = models.CASECADE
    )


    session_date = models.DateTimeField(
        verbose_name = "session_date",
        help_text = "Date and time of your meeting"

    )

    duration = models.TimeField(
        verbose_name = "duration",
        help_text = "Duration of your session",
        validators = [MinValueValidator(1 , message= "The session duration is at least one minute."),
                      MaxValueValidator(60, message = "The meeting duration is more than one hour.")],

        default = 60
        
    )

    session_type = models.CharField(
        max_length = 30,
        choices= Treatmenttype.choices,
        verbose_name = "session_type",
        help_text = "Choose your treatment session type"

    )

    status = models.CharField(
        max_length=20,
        choices = Treatmentstatus.choices,
        verbose_name = "status",
        help_text = "Patient condition"
        
    )