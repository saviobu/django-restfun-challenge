from rest_framework import serializers
from customer.models import Userauth

class UserauthSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Password"
    )

    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Password Confirm"
    )

    is_staff = serializers.BooleanField(
        label="Basic User",
    )

    is_superuser = serializers.BooleanField(
        label="Super User",
    )

    class Meta:
        model = Userauth
        fields = ('username','email', 'password', 'password_confirm', 'is_staff', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        conta = Userauth(
            email=self.validated_data['email'], 
            username=self.validated_data['username'],
            is_staff=self.validated_data['is_staff'],
            is_superuser=self.validated_data['is_superuser']
        )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({'password': 'Password mismatch'})
        conta.set_password(password)
        conta.save()
        return conta