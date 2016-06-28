import requests
import json

from requests_oauthlib import OAuth1
from publisher_credentials import CREDENTIALS_STACKSYNC


class StackSync():
    def __init__(self):

        self.whoami = (self).__class__.__name__
        print self.whoami
        self.oauth = OAuth1(
            client_key=CREDENTIALS_STACKSYNC['client_key'],
            client_secret=CREDENTIALS_STACKSYNC['client_secret'],
            resource_owner_key=CREDENTIALS_STACKSYNC['resource_owner_key'],
            resource_owner_secrete=CREDENTIALS_STACKSYNC['resource_owner_secrete'],
        )
        self.server_base_url = "{}{}{}".format(
            CREDENTIALS_STACKSYNC['swift_url'],
            CREDENTIALS_STACKSYNC['swift_port'],
            CREDENTIALS_STACKSYNC['swift_api_version'],
        )

    def hello(self):
        print "{} say hello".format(self.whoami)

        headers = {}
        folder_id = 0
        if folder_id and folder_id != 0:
            url = self.server_base_url + '/folder/' + str(folder_id) + '/contents'
        else:  # if no folder_id provided -> list root
            url = self.server_base_url + '/folder/0'

        headers['StackSync-API'] = "v2"

        r = requests.get(url, headers=headers, auth=self.oauth)
        print 'response status', r
        print 'response', r.text

        # list root folder content list

    def publish(self, src, tgt):
        print "{} say publish".format(self.whoami)
        ###########
        ###PUT_File
        ###########
        # curl
        # -XPUT
        # -i
        # -k
        # -H "X-Auth-Token: 63bdc8aaa0ac4a2394482d203ba09713"
        # -H "stacksync-api: true"
        # -H "list: true" "https://10.30.239.228:8080/v1/AUTH_e26e8353dbd043ae857ad6962e02f5cc/stacksync/files?file_name=blabla&overwrite=true"
        # -T Path_file

        # lookup a file parent folder and create file.
        headers = {}

        # parent = raw_input("Parent id:  ")

        # parse file name from tgt

        file_name = tgt.split('/')[-1]

        # parse
        if len(tgt.split('/')) == 2:
            # lookup for the target parent folder file_id
            pass
        else:
            parent = None

        if parent:
            url = self.server_base_url + "/file?name=" + file_name + "&parent=" + parent
        else:
            url = self.server_base_url + "/file?name=" + file_name
        # uri, headers, _ = client.sign(url, http_method='GET')
        with open(src, "r") as myfile:
            data = myfile.read()
        headers['StackSync-API'] = "v2"
        r = requests.post(url, data=data, headers=headers, auth=self.oauth)
        print 'response', r
        print 'response', r.text


    def download(self, remote, local):
        print "{} say download".format(self.whoami)

# https://github.com/stacksync/swift-API/blob/3fe1d66ab94237cfc184b6275bd6576003f75aeb/tests/api_test_menu_v2.py
