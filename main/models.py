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

    def place_package(self, package_identifiers, rotation=False, rtl=False, horizontal=False):
        box = Box(instance=self.box_matrix, rotation=rotation, rtl=rtl, horizontal=horizontal)
        # package = get_package_from_list(identifier=package_identifier)
        packages = self.get_packages(packages_ids=package_identifiers)
        # result = box.place(package)
        result, number_of_failed = box.bulk_insertion(packages)
        self.box_matrix = box.matrix
        self.save()
        self.refresh_from_db()
        
        ctx = {
            "result": "Success" if result else "Failed", 
            "box_matrix": self.box_matrix, 
            "failed_to_fit": number_of_failed,
        }

        return ctx
    
    
    def get_packages(self, packages_ids):
        """
        Returns list of packages
        
        Args:
            - packages_ids (list): list of packages ids
            
        Returns:
            - Packages (list): List of packages instances
        """
        return [get_package_from_list(package_id) for package_id in packages_ids]
    