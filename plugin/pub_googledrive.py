import httplib2
import os
import apiclient
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive_credentials.json
# https://developers.google.com/drive/v3/web/about-auth#OAuth2Authorizing
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret_oauth.json'
APPLICATION_NAME = 'BenchBox upload file to drive'
CACHED_CREDENTIAL_FILE = 'drive_credentials.json'
# inserting file to certain folder id ... lookup required, none transactional operation error prone..*[]:

class GoogleDrive():

    def __init__(self):

        self.whoami = (self).__class__.__name__
        print self.whoami
        curr_dir = os.path.expanduser('.')
        credential_dir = os.path.join(curr_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, CACHED_CREDENTIAL_FILE)
        self.store = oauth2client.file.Storage(credential_path)
        self.credentials = self.store.get()

        if not self.credentials or self.credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            self.credentials = tools.run(flow, self.store)
            print 'New credentials Storing to ' + credential_path
        else:
            print "Credentials already cached!"
        http = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('drive', 'v3', http=http)

    def hello(self):
        print "{} say hello".format(self.whoami)

        # self.oauth = Gauth(settings_file="../quickstart/settings.yaml")
        # self.oauth = Gauth(settings_file="quickstart/settings.yaml")
        # self.oauth.LocalWebserverAuth()
        # self.drive = Gdrive(self.oauth)

        results = self.service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print('{0} ({1})'.format(item['name'], item['id']))


    def publish(self, src, tgt):
        print "{} say publish".format(self.whoami)
        # given a certain file path => move forward and try to upload the file



    def download(self, remote, local):
        print "{} say download".format(self.whoami)


