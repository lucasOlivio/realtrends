import meli
from django.conf import settings
from meli.rest import ApiException
from more_itertools import take


class MercadoAPI:
    def __init__(self):
        # Defining the host, defaults to https://api.mercadolibre.com
        # See configuration.py for a list of all supported configuration parameters.
        self.configuration = meli.Configuration(host="https://api.mercadolibre.com")

    def get_full_list(self, api_instance, resource, offset=0, **kwargs):
        sellers = kwargs.get("sellers", {})
        api_response = api_instance.resource_get(f"{resource}&offset={offset}", "")
        for result in api_response["results"]:
            if "eshop" in result["seller"]:
                nick = result["seller"]["eshop"]["nick_name"]
            else:
                seller_response = api_instance.resource_get(
                    f"/users/{result['seller']['id']}", settings.MERCADO_API_TOKEN
                )
                nick = seller_response["nickname"]
            sellers[nick] = sellers.get(nick, 0) + result["sold_quantity"]
        next_offset = offset + 50
        if next_offset < api_response["paging"]["total"] and (
            next_offset <= 1000 or settings.MERCADO_API_TOKEN
        ):
            sellers = self.get_full_list(
                api_instance, resource, next_offset, **{"sellers": sellers}
            )
        return sellers

    def get_category_top_sellers(self, category):
        # Enter a context with an instance of the API client
        with meli.ApiClient() as api_client:
            # Create an instance of the API class
            api_instance = meli.RestClientApi(api_client)
            resource = f"sites/MLA/search?category={category}"
            sellers = {}
            try:
                sellers = self.get_full_list(
                    api_instance, resource, 0, **{"sellers": {}}
                )
            except ApiException as e:
                print("Exception when calling RestClientApi->resource_post: %s\n" % e)
        # Order the dict descending by sold units and take the top 10
        sellers = dict(sorted(sellers.items(), key=lambda item: item[1], reverse=True))
        return take(10, sellers.items())

    def get_category_top_prices(self, category):
        # Enter a context with an instance of the API client
        with meli.ApiClient() as api_client:
            # Create an instance of the API class
            api_instance = meli.RestClientApi(api_client)
            resource = f"sites/MLA/search?category={category}&sort=price_desc&limit=10"
            prices = {}
            try:
                api_response = api_instance.resource_get(resource, "")
            except ApiException as e:
                print("Exception when calling RestClientApi->resource_post: %s\n" % e)
            for result in api_response["results"]:
                prices[result["title"]] = {
                    "price": result["price"],
                    "link": result["permalink"],
                }
        return prices
