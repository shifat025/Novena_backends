from rest_framework import serializers
from .models import Doctor,Speacialization,Designation,AvailableTime,Review

class DoctorSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    # specialization = serializers.StringRelatedField(many=True)
    # designation = serializers.StringRelatedField(many=True)
    # availabletime = serializers.StringRelatedField(many=True)
    class Meta:
        model = Doctor
        fields = '__all__'

class SpeacializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speacialization
        fields = '__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Review
        fields = '__all__'