from rest_framework import serializers

from core.models import Profile

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['url', 'avater', 'descriotion', 'email','github']

