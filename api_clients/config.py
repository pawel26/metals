# first integration with internal API
import os

api_key = os.environ.get('METALS_API_KEY', '')
metals_base_ulr = os.environ.get('METALS_API_URL', '')
METALS_API = {
    "api_key": api_key,
    "base_url": metals_base_ulr,
    "default_currency": 'USD',
    "metals_to_fetch": 'XAU,XAG'
}
