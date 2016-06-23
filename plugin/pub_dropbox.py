import dropbox
import os
import sys
from publisher_credentials import CREDENTIALS_DROPBOX


class Dropbox():

    def __init__(self):

        self.whoami = (self).__class__.__name__
        self.client = None
        print self.whoami

    def hello(self):
        print "{} say hello".format(self.whoami)

        """
        Connect and authenticate with dropbox
        """
        TOKEN = CREDENTIALS_DROPBOX['auth_token']
        LOCALFILE = 'sample/sample.txt'
        BACKUPPATH = '/sample.txt'

        # create instance of dropbox class
        self.client = dropbox.Dropbox(TOKEN)

        # check that the access token is valid
        try:
            print self.client.users_get_current_account()
        except dropbox.exceptions.ApiError as ex:
            print ex.message


        # print 'linked account: ', client.account_info()
        # f = open('sample/sample.txt','rb')
        # response = client.put_file('/sample.txt', f)
        # print 'uploaded: ', response

    def publish(self, src, tgt):
        print "{} say publish".format(self.whoami)
        # backup


    def download(self, remote, local):
        print "{} say download".format(self.whoami)


