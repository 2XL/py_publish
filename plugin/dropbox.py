import dropbox
from publisher_credentials import CREDENTIALS_DROPBOX


class Dropbox():

    def __init__(self):

        self.whoami = (self).__class__.__name__
        print self.whoami

    def hello(self):
        print "{} say hello".format(self.whoami)
        client = dropbox.client.DropboxClient()
        print 'linked account: ', client.account_info()
        f = open('sample/sample.txt','rb')
        response = client.put_file('/sample.txt', f)
        print 'uploaded: ', response

    def publish(self, src, tgt):
        print "{} say publish".format(self.whoami)

    def download(self, remote, local):
        print "{} say download".format(self.whoami)
