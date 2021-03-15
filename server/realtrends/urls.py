from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, reverse_lazy
from django.views.generic.base import RedirectView

from realtrends.core.views import CategoryTopPricesView, CategoryTopSellersView

urlpatterns = [
    path("top-sellers", CategoryTopSellersView.as_view(), name="category-top-sellers"),
    path("top-prices", CategoryTopPricesView.as_view(), name="category-top-prices"),
    re_path(
        r"^$",
        RedirectView.as_view(url=reverse_lazy("category-top-prices"), permanent=False),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
