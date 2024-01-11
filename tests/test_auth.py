import os

from pebbleauthclient.constants import JWKS_EXP_TIME
from pebbleauthclient import auth

token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjBfdl8ycWFYTFFrb1NIYjBRX0d5Ulp1OFZ1X2llVTVHT1UtN0JhUFY4M0UiLCJ0eXAiOiJhdCtqd3QifQ.eyJzdWIiOiJ0ZXN0QHBlYmJsZS5iemgiLCJpc3MiOiJNYWNCb29rLVByby1kZS1HdWlsbGF1bWUubG9jYWwiLCJhdWQiOlsiYXBpLnBlYmJsZS5zb2x1dGlvbnMvdjUvcHJvamVjdCIsImFwaS5wZWJibGUuc29sdXRpb25zL3Y1L2FjdGlvbiJdLCJ0aWQiOiIxamUzNGstZWQ0NWRzc3EtZWsiLCJyb2xlcyI6WyJtYW5hZ2VyIl0sImx2Ijo1LCJjbGllbnRfaWQiOiIwMUhLUTVHUkdHU1I3U0ZCQjFCTTRTUkY4NSIsInNjb3BlIjoicHJvamVjdDpyZWFkIHByb2plY3Q6Y3JlYXRlIHByb2plY3Q6d3JpdGUub3duIGFjdGlvbjpyZWFkIGFjdGlvbjp3cml0ZS5hc3NpZ25lZCBhY3Rpb246Y3JlYXRlIHByb2plY3Q6ZGVsZXRlIiwiaWF0IjoxNzA0OTYzNDQ1LCJleHAiOjE3MDQ5NjcwNDUsImp0aSI6IjY3YzVhZDNhLTFmZDktNDhjNy1hZTU4LTNkYjQ1MTJiMWI5NyJ9.SWa0YCXaE_0TG_sqy0wTBvwNV20hpcRXIXpO2kRhkh_Y4yVag9WTHMN5SadPZXdXb7t2C25nvZcWR9OHwFsPVmLw-GjFjSSFyT2B_kkTx0rjXq4MsbPEE1KjqR4VXrdZUctrdAC3WkcCF0uoZre2dbEarZoMEhkyuqQTaGE6NBKyYwEtsKULQbt31bZdx_33DdPWI-lAOoITYqBVdvv9r9MY2pAc3B6KvMFHiCYYeRu8FNJ39tWwLjn0r8s_nwCyxlEzTD2EodQKuFx_ICVUlJn1M3hvjkeMFxZizxFiALWXDTuE-7Uo0Rre91hTlLGVPYknOWRndNjzAqRgDg7S3g"

"""
while True:
    print("Input a valid JWT token (type Q to exit) : ")
    token = input()

    if token.lower() == "q":
        break"""

auth_token = auth(token, options={
    'audience': "api.pebble.solutions/v5/action"
})
user = auth_token.get_user()
licence = auth_token.get_authenticated_licence()

print(JWKS_EXP_TIME)
print(os.getenv('PBL_JWKS_LAST_UPDATE'))

print(auth_token)
print(user)
print(licence)
