from rest_framework import serializers
from .models import Review, CustomUser

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user_id', 'user', 'Rating', 'Movie_title', 'Review_Content', 'Created_date']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email"]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(username=validated_data['email'], email=validated_data['email'])
        return user