from rest_framework import serializers
from .models import Reporting

class ReportingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporting
        fields = [ "pk", "townName", "timeOfDay"]

