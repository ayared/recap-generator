"""gmail.py
Interacts with the Gmail API to create the email draft
"""

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
from apiclient import errors
from config import RECIPIENTS, SENDER

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

SUBJECT = "Gameweek N Recap"
MESSAGE = "Lol Benny lost again"


def main():
    service = start_service()
    email = create_message(SENDER, RECIPIENTS, SUBJECT, MESSAGE)
    create_draft(service, 'me', email)


def mail_runner(subject, message):
    """Main entry point for gmail.py
    Creates an email draft with the given subject and messages
    Populates sender and recipients based on config.py

    Args:
        subject (str): subject line for the email
        message (str): body for the email
    Returns:
        None
    """
    service = start_service()
    email = create_message(SENDER, RECIPIENTS, subject, message)
    create_draft(service, 'me', email)


def start_service():
    """Start a gmail API session

    Args: none
    Returns:
        A authenticated gmail service
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'C:\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service


def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.

    Returns:
        An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    return {'raw': raw}


def create_draft(service, user_id, message_body):
    """Create and insert a draft email. Print the returned draft's message and id.

    Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        message_body: The body of the email message, including headers.

    Returns:
        Draft object, including draft id and message meta data.
    """
    try:
        message = {'message': message_body}
        draft = service.users().drafts().\
            create(userId=user_id, body=message).execute()

        print('Draft id: %s\nDraft message: %s' %
              (draft['id'], draft['message']))

        return draft
    except Exception as error:
        print('An error occurred %s' % error)
        return None


if __name__ == '__main__':
    main()
