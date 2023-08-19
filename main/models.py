from django.db import models
import uuid

from processor.fitting_utils import Box
from processor.helpers import get_package_from_list


class Session(models.Model):
    uuid = models.UUIDField("Session uuid", primary_key=True, default=uuid.uuid4, editable=False)
    box_matrix = models.JSONField("Box", help_text="The current box at its latest state", null=True, blank=True)

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"

    def __str__(self):
        return "%s" % self.uuid

    @classmethod
    def initial_new_box(cls, rows, cols):
        box = Box(rows=rows, cols=cols)
        return cls.objects.create(box_matrix=box.matrix)

    def place_package(self, package_identifier, rotation=False, rtl=False, horizontal=False):
        # we can find a way to prevent passing the rows / cols in case of instance is passed
        box = Box(instance=self.box_matrix, rotation=rotation, rtl=rtl, horizontal=horizontal)
        package = get_package_from_list(identifier=package_identifier)
        result = box.place(package)
        self.box_matrix = box.matrix
        self.save()
        self.refresh_from_db()

        return result, self.box_matrix
