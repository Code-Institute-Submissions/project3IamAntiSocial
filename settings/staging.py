from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.parse(
    "mysql://bce8728ef94639:dec5b67a@eu-cdbr-west-01.cleardb.com/heroku_54ef77cf2eb9b46?reconnect=true")

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_DN78rrac6Vda1ito3iAlshPc')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_6VOZz0QegToWvMWYrcGF5qFs')

# Paypal environment variables
SITE_URL = 'https://project3-i-am-anti-social.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'https://project3-i-am-anti-social.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'brendanjgreene-merchant2@gmail.com'
