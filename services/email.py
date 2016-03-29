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
        verif_url = ('http://www.humanlink.co/verify?' + urllib.urlencode(qs))
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

    def send_email_to_support(self, email, name, message):
        """Sends an email to the specified account with email verification URL.

        :param account_id: (int)
            ID of the Account entity.
        :return: (None)
        """

        message = {
            'global_merge_vars': [
                {'name': 'FROM_EMAIL', 'content': email},
                {'name': 'MESSAGE', 'content': message},
                {'name': 'NAME', 'content': name},
            ],
            'to': [
                {'email': 'support@humanlink.co'},
            ],
        }
        self._send_from_us(self.md.messages.send_template,
                           template_name='humanlink-support',
                           template_content=[],
                           message=message,
                           async=True)

    def send_password_reset(self, account_id):
        """Sends an email to the specified account with password reset URL.

        :param account_id: (int)
            ID of the Account entity.
        :return: (None)
        """
        account = services.accounts.account_by_id(account_id, _dto=False)
        qs = {'email': account.email, 'token': account.verification_token}
        verif_url = (
            'http://www.humanlink.co/accounts#/reset_password?' + urllib.urlencode(qs))

        message = {
            'global_merge_vars': [
                {'name': 'VERIFICATION_URL', 'content': verif_url},
            ],
            'to': [
                {'email': account.email},
            ],
        }
        self._send_from_us(self.md.messages.send_template,
                           template_name='humanlink_password_reset',
                           template_content=[],
                           message=message,
                           async=True)

    def send_connection_request(self, from_fname, from_lname, from_email, to_fname,
                                to_email, message):
        """Sends an connection request email

        :param
                from_fname: (string)
                from_lname: (string)
                from_email: (string)
                to_fname: (string)
                to_email: (string)
                message: (string)
        :return: (None)
        """
        message = {
            'global_merge_vars': [
                {'name': 'FNAME1', 'content': to_fname},
                {'name': 'FNAME2', 'content': from_fname},
                {'name': 'LNAME2', 'content': from_lname},
                {'name': 'FROM_EMAIL', 'content': from_email},
                {'name': 'MESSAGE', 'content': message}
            ],
            'to': [
                {'email': to_email},
            ],
        }
        self._send_from_us(self.md.messages.send_template,
                           template_name='humanlink-connection-request',
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
send_email_to_support = _email_service.send_email_to_support
send_password_reset = _email_service.send_password_reset
send_connection_request = _email_service.send_connection_request
