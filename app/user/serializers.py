from django.contrib.auth import get_user_model as User, authenticate
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User()
        fields = ('email', 'password', 'name')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5},

        }

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        """Update the user setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
