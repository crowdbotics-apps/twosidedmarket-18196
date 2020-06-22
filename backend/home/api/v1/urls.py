from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ChatViewSet,
    CustomerProfileViewSet,
    CustomerPurchasesViewSet,
    CustomTextViewSet,
    FavoritesViewSet,
    HomePageViewSet,
    InboxViewSet,
    MessageViewSet,
    ProfileViewSet,
    RecentlyViewedViewSet,
    ReviewsViewSet,
    SavedViewSet,
    SellerListingsViewSet,
    SellerProfileViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("profile", ProfileViewSet)
router.register("sellerprofile", SellerProfileViewSet)
router.register("customerprofile", CustomerProfileViewSet)
router.register("favorites", FavoritesViewSet)
router.register("reviews", ReviewsViewSet)
router.register("saved", SavedViewSet)
router.register("recentlyviewed", RecentlyViewedViewSet)
router.register("sellerlistings", SellerListingsViewSet)
router.register("customerpurchases", CustomerPurchasesViewSet)
router.register("chat", ChatViewSet)
router.register("message", MessageViewSet)
router.register("inbox", InboxViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
