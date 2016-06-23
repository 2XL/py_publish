import dropbox
import os
import sys
from publisher_credentials import CREDENTIALS_DROPBOX


class Dropbox():

    def __init__(self):

        self.whoami = (self).__class__.__name__
        self.client
        print self.whoami

    def hello(self):
        print "{} say hello".format(self.whoami)

        """
        Connect and authenticate with dropbox
        """

        app_key = CREDENTIALS_DROPBOX['app_key']
        app_secret = CREDENTIALS_DROPBOX['app_secret']
        access_type = "dropbox"
        session = dropbox.session.DropboxSession(app_key, app_secret, access_type)

        request_token = session.obtained_request_token()

        url = session.build_authorize_url(request_token)
        msg


        #
        # print 'linked account: ', client.account_info()
        # f = open('sample/sample.txt','rb')
        # response = client.put_file('/sample.txt', f)
        # print 'uploaded: ', response

    def publish(self, src, tgt):
        print "{} say publish".format(self.whoami)

    def download(self, remote, local):
        print "{} say download".format(self.whoami)
