from django.db import models


class Session(models.Model):
    uuid = models.UUIDField("Session uuid", auto_created=True)
    box = models.JSONField("Box", help_text="The current box at its latest state", null=True, blank=True)

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"

    def __str__(self):
        return "%s" % self.uuid
