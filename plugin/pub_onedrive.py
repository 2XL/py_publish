import onedrivesdk
from publisher_credentials import CREDENTIALS_ONEDRIVE
from onedrivesdk.helpers import GetAuthCodeServer

class OneDrive():

    def __init__(self):

        self.whoami = (self).__class__.__name__
        print self.whoami
        self.client = None

        self._authenticate_with_helper()

    def _authenticate(self):
        redirect_uri = CREDENTIALS_ONEDRIVE["redirect_uri"]
        client_secret = CREDENTIALS_ONEDRIVE["client_secret"]
        client_id = CREDENTIALS_ONEDRIVE["client_id"]
        api_base_url = CREDENTIALS_ONEDRIVE["api_base_url"]
        scopes = CREDENTIALS_ONEDRIVE["scopes"]

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
        scopes = CREDENTIALS_ONEDRIVE["scopes"]
        self.client = onedrivesdk.get_default_client(
            client_id=CREDENTIALS_ONEDRIVE["client_secret"],
            scopes=scopes
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

    def publish(self, src, tgt):
        print "{} say publish".format(self.whoami)

    def download(self, remote, local):
        print "{} say download".format(self.whoami)