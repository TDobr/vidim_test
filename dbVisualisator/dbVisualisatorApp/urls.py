from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('products', views.product_list_operations),
    path('products/<uuid:id>', views.product_by_id_operations),
    path('opentripmap', views.open_trip_map_operations)
]

urlpatterns = format_suffix_patterns(urlpatterns)

api_urls = {
    "OpenTripMap": {
        "main_url": "https://api.opentripmap.com/0.1",
        "api_gateways": {
            "get_autosuggest_places": "/{lang}/places/autosuggest"
        }
    }
}

MAIN_URL_KEY = "main_url"
API_GATEWAYS_KEY = "api_gateways"
