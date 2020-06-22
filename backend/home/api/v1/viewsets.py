from rest_framework import viewsets
from rest_framework import authentication
from .serializers import (
    ChatSerializer,
    CustomerProfileSerializer,
    CustomerPurchasesSerializer,
    CustomTextSerializer,
    FavoritesSerializer,
    HomePageSerializer,
    InboxSerializer,
    MessageSerializer,
    ProfileSerializer,
    RecentlyViewedSerializer,
    ReviewsSerializer,
    SavedSerializer,
    SellerListingsSerializer,
    SellerProfileSerializer,
)
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from home.api.v1.serializers import (
    SignupSerializer,
    CustomTextSerializer,
    HomePageSerializer,
    UserSerializer,
)
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


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class CustomTextViewSet(ModelViewSet):
    serializer_class = CustomTextSerializer
    queryset = CustomText.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "put", "patch"]


class HomePageViewSet(ModelViewSet):
    serializer_class = HomePageSerializer
    queryset = HomePage.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "put", "patch"]


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Profile.objects.all()


class SellerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = SellerProfileSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = SellerProfile.objects.all()


class CustomerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerProfileSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CustomerProfile.objects.all()


class FavoritesViewSet(viewsets.ModelViewSet):
    serializer_class = FavoritesSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Favorites.objects.all()


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Reviews.objects.all()


class SavedViewSet(viewsets.ModelViewSet):
    serializer_class = SavedSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Saved.objects.all()


class RecentlyViewedViewSet(viewsets.ModelViewSet):
    serializer_class = RecentlyViewedSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = RecentlyViewed.objects.all()


class SellerListingsViewSet(viewsets.ModelViewSet):
    serializer_class = SellerListingsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = SellerListings.objects.all()


class CustomerPurchasesViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerPurchasesSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CustomerPurchases.objects.all()


class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Chat.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Message.objects.all()


class InboxViewSet(viewsets.ModelViewSet):
    serializer_class = InboxSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Inbox.objects.all()
