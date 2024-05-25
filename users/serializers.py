from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "full_name",
            "artistic_name",
        ]

        extra_kwargs = {"password": {"write_only": True}}                     
    email = serializers.EmailField(validators=[
        UniqueValidator(User.objects.all(), "This field must be unique.")
        ],
    )

    def create(self, validated_data: dict) -> User:
        print(validated_data)
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        print(validated_data.items)
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance
