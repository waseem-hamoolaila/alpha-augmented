from django.db import models
import uuid

from processor.fitting_utils import Package, Box


class Session(models.Model):
    uuid = models.UUIDField("Session uuid", primary_key=True, default=uuid.uuid4, editable=False)
    box_matrix = models.JSONField("Box", help_text="The current box at its latest state", null=True, blank=True)

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"

    def __str__(self):
        return "%s" % self.uuid

    @classmethod
    def initial_new_box(cls, rows, cols, rotation=False, rtl=False):
        box = Box(rows=rows, cols=cols)
        return cls.objects.create(box_matrix=box.matrix)

    def get_main_box(self):
        return self.box
