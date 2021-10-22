from import_export import resources
from .models import *

class PersonResource(resources.ModelResource):
    class Meta:
        model = OnGameUsers
        fields = ('id', 'user_name', 'status',)