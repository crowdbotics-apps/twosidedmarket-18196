from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.utils.translation import ugettext_lazy as _
from allauth.account import app_settings as allauth_settings
from allauth.account.forms import ResetPasswordForm
from allauth.utils import email_address_exists, generate_unique_username
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from rest_auth.serializers import PasswordResetSerializer
from home.models import (
    Chat,
    CustomerProfile,
    CustomerPurchases,
    CustomText,
    Favorites,
    HomePage,
    Inbox,
    Message,
    Profile,
    RecentlyViewed,
    Reviews,
    Saved,
    SellerListings,
    SellerProfile,
)

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}},
            "email": {"required": True, "allow_blank": False,},
        }

    def _get_request(self):
        request = self.context.get("request")
        if (
            request
            and not isinstance(request, HttpRequest)
            and hasattr(request, "_request")
        ):
            request = request._request
        return request

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address.")
                )
        return email

    def create(self, validated_data):
        user = User(
            email=validated_data.get("email"),
            name=validated_data.get("name"),
            username=generate_unique_username(
                [validated_data.get("name"), validated_data.get("email"), "user"]
            ),
        )
        user.set_password(validated_data.get("password"))
        user.save()
        request = self._get_request()
        setup_user_email(request, user, [])
        return user

    def save(self, request=None):
        """rest_auth passes request so we must override to accept it"""
        return super().save()


class CustomTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomText
        fields = "__all__"


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "name"]


class PasswordSerializer(PasswordResetSerializer):
    """Custom serializer for rest_auth to solve reset password error"""

    password_reset_form_class = ResetPasswordForm


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = "__all__"


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = "__all__"


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = "__all__"


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"


class SavedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saved
        fields = "__all__"


class RecentlyViewedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentlyViewed
        fields = "__all__"


class SellerListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerListings
        fields = "__all__"


class CustomerPurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPurchases
        fields = "__all__"


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class InboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbox
        fields = "__all__"
