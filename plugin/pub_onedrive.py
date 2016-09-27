import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer

class OneDrive():

    def __init__(self):

        self.whoami = (self).__class__.__name__
        print self.whoami
        self.client = None

        self._authenticate_with_helper()

    def _authenticate(self):
        redirect_uri = 'http://localhost:8080/'
        client_secret = '25107EA031A7DE26B238B9E318D97D755BF3163F'
        client_id = 'fcb741cb-be05-4349-80d6-cd4f7926d258'
        api_base_url = 'https://api.onedrive.com/v1.0/'
        scopes=['w1.signin', 'w1.offline_access','onedrive.readwrite']

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

        redirect_uri = "http://localhost:8080/"
        client_secret = "DVB14Cm4LRCuPEjViSfeduD"
        scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
        self.client = onedrivesdk.get_default_client(
            client_id="fcb741cb-be05-4349-80d6-cd4f7926d258",
            scopes=scopes
        )

        auth_url = self.client.auth_provider.get_auth_url(redirect_uri)

        # this will block until we have the code

        code = GetAuthCodeServer.get_auth_code(auth_url=auth_url, redirect_uri=redirect_uri)

        self.client.auth_provider.authenticate(code, redirect_uri, client_secret)








    def hello(self):
        print "{} say hello".format(self.whoami)

    def publish(self, src, tgt):
        print "{} say publish".format(self.whoami)

    def download(self, remote, local):
        print "{} say download".format(self.whoami)