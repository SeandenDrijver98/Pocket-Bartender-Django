from rest_framework import serializers
from bartender_app.models import Drink, Ingredient, User, UserIngredient


class DrinkSerializer(serializers.ModelSerializer):
    ingredients = serializers.StringRelatedField(many=True)

    class Meta:
        model = Drink
        fields = ["id", "title", "ingredients", "instructions", "description", "image"]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "title", "type"]


class UserIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=False, read_only=True)

    class Meta:
        model = UserIngredient
        fields = ["ingredient"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User(
            email=validated_data["username"], username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()

        return user
