import requests
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class FacebookBackend:
    def authenticate(self, request, code):
        def get_access_token(code):
            # authentication code -> get access_token
            url = 'https://graph.facebook.com/v3.0/oauth/access_token'
            params = {
                'client_id': settings.FACEBOOK_APP_ID,
                'redirect_uri': 'http://localhost:8000/members/facebook-login/',
                'client_secret': settings.FACEBOOK_APP_SECRET_CODE,
                'code': code,
            }
            response = requests.get(url, params)

            # if 'error' in response:
            #     raise FacebookAccessException(response['error']['message'])
            response_dict = response.json()
            print(response_dict)
            access_token = response_dict['access_token']

            return access_token

        def debug_token(token):
            # debug token
            url = 'https://graph.facebook.com/debug_token'
            params = {
                'input_token': token,
                'access_token': '{}|{}'.format(
                    settings.FACEBOOK_APP_ID,
                    settings.FACEBOOK_APP_SECRET_CODE,
                )
            }
            response = requests.get(url, params)
            return response.json()

        def get_user_info(token, fields=('id', 'name', 'first_name', 'last_name')):
            # facebook user info
            url = 'https://graph.facebook.com/v3.0/me'
            params = {
                'fields': ','.join(fields),
                'access_token': token,
            }
            response = requests.get(url, params)
            return response.json()

        def create_user_from_facebook_user_info(user_info):
            facebook_user_id = user_info['id']
            first_name = user_info['first_name']
            last_name = user_info['last_name']

            return User.objects.get_or_create(
                username=facebook_user_id,
                defaults={
                    'first_name': first_name,
                    'last_name': last_name,
                },
            )

        access_token = get_access_token(code)
        user_info = get_user_info(access_token)
        user, user_created = create_user_from_facebook_user_info(user_info)
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None