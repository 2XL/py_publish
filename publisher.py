import publisher_credentials
import traceback
from plugin.box import Box as box
from plugin.clouddrive import CloudDrive as clouddrive
from plugin.dropbox import Dropbox as dropbox
from plugin.googledrive import GoogleDrive as googledrive
from plugin.mega import Mega as mega
from plugin.onedrive import OneDrive as onedrive
from plugin.owncloud import OwnCloud as ownloud
from plugin.stacksync import StackSync as stacksync
from plugin.sugarsync import SugarSync as sugarsync


class Publisher(object):
    '''
    this is the base object file publisher
    '''

    def __init__(self, personal_cloud=None):
        print "Constructor"

        self.action = None
        if personal_cloud is None:
            raise NotImplemented
        else:
            self.action = eval(personal_cloud)()

    def publish(self, local_file_path, dst_remote_path = "/"):
        """
        upload a local file to the personal cloud storage
        :param local_file_path:
        :param remote_path:
        :return:
        """
        try:
            self.action.publish(local_file_path, dst_remote_path)
            return 0
        except Exception as ex:
            print ex.message
            return 1

    def download(self, remote_file_path, dst_local_path = "sample_response"):
        """
        retrieve a file hosted at personal cloud storage
        :param remote_file_path:
        :param dst_local_path:
        :return:
        """
        try:
            self.action.download(remote_file_path, dst_local_path)
            return 0
        except Exception as ex:
            print ex.message
            return 1

    def hello(self):
        try:
            self.action.hello()
            return 0  # successfully logged to personal cloud service
        except Exception as ex:
            print ex.message
            print traceback.print_tb(None)
            return 1