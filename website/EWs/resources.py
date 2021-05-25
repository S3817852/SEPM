from import_export import resources
from .models import MonthlyEW

class EWresources(resources.ModelResource):
    class meta:
        model = MonthlyEW