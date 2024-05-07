from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        # fieds = (
        #     'id',
        #     'name',
        #     'age',
        #     'created',
        #     'missing_date',
        #     'founded',
        # )
