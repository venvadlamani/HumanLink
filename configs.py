"""
This file stores secret keys and tokens related to the application.

Note: Consider using ConfigParser in the future.
"""

# For cookie serialization/desrialization.
SESSION_SECRET = 'humanlink-095999b7ab19b8019c492ba63535c4cc'

# Used to hash an account's email verification token:
#   token = md5(VERIFY_SECRET + email).hexdigest()
VERIF_SECRET = 'humanlink-verif-secret'
