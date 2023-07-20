# For more information please refer to https://github.com/checkout/checkout-sdk-python
import checkout_sdk
from checkout_sdk.checkout_sdk import CheckoutSdk
from checkout_sdk.common.common import Phone, Address
from checkout_sdk.common.enums import Country
from checkout_sdk.environment import Environment
from checkout_sdk.exception import CheckoutApiException, CheckoutArgumentException, CheckoutAuthorizationException
from checkout_sdk.tokens.tokens import CardTokenRequest

# API Keys
api = CheckoutSdk.builder() \
    .public_key('public_key') \
    .environment(Environment.sandbox()) \
    .build()
# or Environment.production()

phone = Phone()
phone.country_code = '44'
phone.number = '4155552671'

address = Address()
address.address_line1 = 'CheckoutSdk.com'
address.address_line2 = '90 Tottenham Court Road'
address.city = 'London'
address.state = 'London'
address.zip = 'W1T 4TJ'
address.country = Country.GB

request = CardTokenRequest()
request.number = 'number'
request.expiry_month = 10
request.expiry_year = 2027
request.cvv = 123
request.name = 'Name'
request.billing_address = address
request.phone = phone

try:
    response = api.tokens.request_card_token(request)
except CheckoutApiException as err:
    # API error
    request_id = err.request_id
    status_code = err.http_status_code
    error_details = err.error_details
    http_response = err.http_response
# except CheckoutArgumentException as err:
# # Bad arguments
#
# except CheckoutAuthorizationException as err:
# # Invalid authorization
