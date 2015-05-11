import services.accounts
import services.asserts as asserts

import configs
import logging
import mandrill
import re
import urllib


# Basic email sanity check.
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")


def is_valid_email(email):
    """Performs a basic email sanity check."""
    asserts.type_of(email, basestring)
    return EMAIL_REGEX.match(email) is not None


class EmailService(object):
    """Email service wrapper around Mandrill API.
    Docs: https://mandrillapp.com/api/docs/index.python.html
    """

    from_name = 'HumanLink'
    from_email = 'support@humanlink.co'

    def __init__(self):
        self._md = None

    @property
    def md(self):
        """Mandrill instance."""
        self._md = self._md or mandrill.Mandrill(configs.MANDRILL_API_KEY)
        return self._md

    def send_email_verification(self, account_id):
        """Sends an email to the specified account with email verification URL.

        :param account_id: (int)
            ID of the Account entity.
        :return: (None)
        """
        account = services.accounts.account_by_id(account_id, _dto=False)

        qs = {'email': account.email, 'token': account.verification_token}
        verif_url = ('https://www.humanlink.co/verify?' + urllib.urlencode(qs))
        message = {
            'global_merge_vars': [
                {'name': 'VERIFICATION_URL', 'content': verif_url},
            ],
            'to': [
                {'email': account.email},
            ],
        }
        self._send_from_us(self.md.messages.send_template,
                           template_name='humanlink-welcome',
                           template_content=[],
                           message=message,
                           async=True)

    @staticmethod
    def md_send(func, **kwargs):
        try:
            func(**kwargs)
        except mandrill.Error as e:
            logging.exception(e)
            raise e

    def _send_from_us(self, func, **kwargs):
        """Populate from field in the message and send it over."""
        message = kwargs.get('message')
        message['from_email'] = self.from_email
        message['from_name'] = self.from_name
        self.md_send(func, **kwargs)


_email_service = EmailService()

send_email_verification = _email_service.send_email_verification
