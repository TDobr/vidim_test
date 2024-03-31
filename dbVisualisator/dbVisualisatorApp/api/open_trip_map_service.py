import requests

from .. import urls

OPEN_TRIP_MAP_KEY = 'OpenTripMap'
GET_AUTOSUGGEST_KEY = "get_autosuggest_places"
API_KEY = "5ae2e3f221c38a28845f05b67c3a04e20354ee205d9477ba49661b86"


def get_autosuggest(lat, lon, name, lng, amount, rad):
    url = build_url(lat, lon, name, lng, amount, rad)
    response = requests.get(url)
    return response.json()


def build_url(lat, lon, name, lng, amount, rad):
    open_trip_map_settings = urls.api_urls.get(OPEN_TRIP_MAP_KEY)
    default_url = open_trip_map_settings.get(urls.MAIN_URL_KEY)
    api_gateways = open_trip_map_settings.get(urls.API_GATEWAYS_KEY)
    api_gateway_key = api_gateways.get(GET_AUTOSUGGEST_KEY)
    url = default_url + api_gateway_key + "?name={name}&radius={rad}&lon={lon}&lat={lat}&format=json&limit={limit}&apikey={apikey}"
    return url.format(lat=lat, lon=lon, name=name, lang=lng, limit=amount, rad=rad, apikey=API_KEY)
