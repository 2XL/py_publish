import onedrivesdk
from publisher_credentials import CREDENTIALS_ONEDRIVE
from onedrivesdk.helpers import GetAuthCodeServer

class OneDrive():

    def __init__(self):

        self.whoami = (self).__class__.__name__
        self.client = None
        print self.whoami
        ##

    def _authenticate(self):
        redirect_uri = CREDENTIALS_ONEDRIVE["redirect_uri"]
        client_secret = CREDENTIALS_ONEDRIVE["client_secret"]
        client_id = CREDENTIALS_ONEDRIVE["client_id"]
        api_base_url = CREDENTIALS_ONEDRIVE["api_base_url"]
        scopes = ['w1.signin', 'w1.offline_access','onedrive.readwrite']

        http_provider = onedrivesdk.HttpProvider()

        auth_provider = onedrivesdk.AuthProvider(
            http_provider=http_provider,
            client_id=client_id,
            scopes=scopes,
        )

        client = onedrivesdk.OneDriveClient(
            base_url=api_base_url,
            auth_provider=auth_provider,
            http_provider=http_provider

        )

        auth_url = client.auth_provider.get_auth_url(redirect_uri=redirect_uri)

        # simular la opcion con selenium
        print "Open the following url into your browser and approve the app\'s access. \n{}".format(auth_url)
        # extract the field code="" from the auth_url and inject it to the client
        # code = auth_url.split('code=')[1]  # require additional parsings
        # print code
        # client.auth_provider.authenticate(code, redirect_uri, client_secret)

    def _authenticate_with_helper(self):

        redirect_uri = CREDENTIALS_ONEDRIVE["redirect_uri"]
        client_secret = CREDENTIALS_ONEDRIVE["client_secret"]

        self.client = onedrivesdk.get_default_client(
            client_id=CREDENTIALS_ONEDRIVE["client_id"],
            scopes=['wl.signin',
                    'wl.offline_access',
                    'onedrive.readwrite']
        )

        auth_url = self.client.auth_provider.get_auth_url(redirect_uri)
        print "Auth URL: {}".format(auth_url)
        # this will block until we have the code

        code = GetAuthCodeServer.get_auth_code(auth_url=auth_url, redirect_uri=redirect_uri)
        print "Code:     {}".format(code)
        self.client.auth_provider.authenticate(code, redirect_uri, client_secret)

        print "Client Authentication OK"

    def hello(self):
        print "{} say hello".format(self.whoami)
        self._authenticate_with_helper()

    def publish(self, src, tgt):
        print "{} say publish".format(self.whoami)
        self._authenticate_with_helper()
        try:
            self._authenticate_with_helper()
        except Exception as ex:
            print ex.message

        # f = open(src, 'rb')
        try:
            print "publish this {} to {}".format(src, tgt)
            remote_fileName = '.{}'.format(tgt)
            local_fileName = '{}'.format(src)

            # upload file to a certain directory.
            returned_item = self.client.item(drive='me', id='root').children[local_fileName].upload(remote_fileName)
            print returned_item
        except Exception as ex:
            print ex.message




    def download(self, remote, local):
        print "{} say download".format(self.whoami)