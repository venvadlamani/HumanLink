import json
import webapp2
import configs
from google.appengine.api import urlfetch


class QueueHandler(webapp2.RequestHandler):
    """Task queue handler."""

    def slack(self):
        """Sends data to the Slack Webhook URL."""
        text = self.request.get('text')
        if not text:
            return
        payload = {
            'username': 'hl-bot',
            'icon_emoji': ':rocket:',
            'text': text
        }
        urlfetch.fetch(url=configs.SLACK_URL,
                payload=json.dumps(payload),
                method=urlfetch.POST,
                headers={'Content-Type': 'application/json'})
