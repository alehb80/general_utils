import datetime

import pytz


def get_current_time_in_city(city):
    # Dizionario delle città e dei rispettivi fusi orari
    city_timezones = {
        "TIV": "Europe/Rome",
        "MAK": "Asia/Colombo",
        "XNT": "Asia/Shanghai",
        "FEC": "America/Bahia"
    }

    # Verifica se la città è nel dizionario
    if city in city_timezones:
        timezone = pytz.timezone(city_timezones[city])
        current_time = datetime.datetime.now(timezone)
        return current_time
    else:
        return "Città non trovata o non supportata"


# import datetime
# from typing import Optional
#
# import pytz
# from opencage.geocoder import OpenCageGeocode
#
# api_key = "39ea59524d5145148defae5f8124daf5"
#
#
# def country_from_city(city: str, api_key: str) -> Optional[str]:
#     try:
#         # Crea un oggetto geolocalizzatore OpenCage con la tua chiave API
#         geolocator = OpenCageGeocode(api_key)
#         # Ottieni le informazioni sulla posizione (città, stato/regione)
#         location = geolocator.geocode(city)
#         if location:
#             # Estrai il nome dello stato o della regione dalla risposta di OpenCage
#             components = location[0].get('components', {})
#             return components.get('country')
#             # return components.get('continent') + "/" + components.get('city')
#         else:
#             return None
#     except Exception as e:
#         print(f"Si è verificato un errore: {str(e)}")
#         return None
#
#
# def timezone_from_country(country: str, api_key: str) -> Optional[str]:
#     try:
#         # Crea un oggetto geolocalizzatore OpenCage con la tua chiave API
#         geolocator = OpenCageGeocode(api_key)
#         results = geolocator.geocode(f"capital of {country}")
#         if results and len(results):
#             return results[0]["annotations"]["timezone"]["name"]
#         else:
#             return None
#     except Exception as e:
#         print(f"Si è verificato un errore: {str(e)}")
#         return None
#
#
# def current_timezone_from_country(timezone_country: str) -> Optional[datetime.datetime]:
#     try:
#         # Trova il fuso orario dello stato o della regione
#         tz = pytz.timezone(timezone_country)
#         # Ottieni l'ora corrente per quel fuso orario
#         return datetime.datetime.now(tz)
#     except pytz.UnknownTimeZoneError:
#         return None


# def get_city_from_short_city(short_city: str) -> str:
#     city_mapping = {
#         "TIV": "Tivoli",
#         "TSL": "TSL",
#         "HBI": "Hebei",
#         "FDS": "Feira de Santana",
#     }
#     return city_mapping.get(short_city)


if __name__ == '__main__':
    # Esempio di utilizzo
    city = "MAK"
    current_time = get_current_time_in_city(city)
    print(f"Ora corrente a {city}: {current_time}")

    # short_city = "HBI"
    # print(short_city)
    # city = get_city_from_short_city(short_city=short_city)
    # print(city)
    # country = country_from_city(city=city, api_key=api_key)
    # print(country)
    # timezone_country = timezone_from_country(country=country, api_key=api_key)
    # print(timezone_country)
    # current_timezone = current_timezone_from_country(timezone_country=timezone_country)
    # print(current_timezone)
