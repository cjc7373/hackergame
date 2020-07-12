from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.models import User, Term


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("Password too short.")
        return value

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise ValidationError("Passwords are not same.")
        return data

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data['username'],
                                        password=validated_data['password'])


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    allow_terms = serializers.BooleanField(required=False)


class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='last_name')

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'token', 'name', 'date_joined']


class ProfileUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='last_name')

    class Meta:
        model = User
        fields = ['name']


class PublicProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='last_name')

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'name']