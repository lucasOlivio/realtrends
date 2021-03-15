from django.views.generic import TemplateView

from realtrends.core.utils.MercadoAPI import MercadoAPI


class CategoryTopSellersView(TemplateView):
    template_name = "core/top_category_sellers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get top sellers
        mercado = MercadoAPI()
        context["sellers"] = mercado.get_category_top_sellers("MLA420040")
        return context


class CategoryTopPricesView(TemplateView):
    template_name = "core/top_category_prices.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get top sellers
        mercado = MercadoAPI()
        context["prices"] = mercado.get_category_top_prices("MLA420040")
        return context
