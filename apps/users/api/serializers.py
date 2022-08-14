from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
      """ Create User """
      user = User(**validated_data)
      user.set_password(validated_data['password'])
      user.save()
      return user

    def update(self, instance, validated_data):
      update_user = super().update(instance, validated_data)
      update_user.set_password(validated_data['password'])
      update_user.save()
      return update_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
      return {
        'id': instance['id'],
        'nip': instance['nip'],
        'username': instance['username'],
        'password': instance['password'],
        'email': instance['email'],
        'name': instance['name'],
        'last_name': instance['last_name'],
        'is_active': instance['is_active'],
      }