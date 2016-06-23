#!/usr/bin/python

import boxsdk
from publisher_credentials import CREDENTIALS_BOX



def store_token_function(access_token, refresh_token):
    # ASDF
    print "GET TOKEN:"
    print access_token,refresh_token


if __name__ == "__main__":
    """
    Connect and authenticate with box
    """
    TOKEN = CREDENTIALS_BOX['auth_token']
    CLIENT_ID = CREDENTIALS_BOX['client_id']
    CLIENT_SECRET = CREDENTIALS_BOX['client_secret']

    oauth = boxsdk.OAuth2(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        store_tokens=store_token_function,
        access_token=TOKEN
    )
    # create instance of box class
    oauth.authenticate()
    client = boxsdk.Client(oauth)

    app = client.user().get()
    # upload a file to box
    src = "sample/sample.txt"
    tgt = "/a/sample.txt"

    print src, tgt
    f = open(src, 'rb')

    # se requiere buscar o crear el parent folder del path que especifiquemos
    # se tiene que comprobar que el archivo exista o no, no deja overwrite... implicaria hacer un put y get
    # lo que no queremos es el cliente haga un delete + download cuando
    # solo queremos download.




    print "Testing while loop"

    str = tgt
    path_array = str.split('/')
    print str, path_array
    #  hacer un metodo lookup folder..

    root_folder = client.folder('0')
    current_folder = root_folder
    idx = 1
    while idx < len(path_array) - 1:
        print idx, path_array[idx]
        next_folder = path_array[idx]
        item_list = current_folder.get_items(limit=100, offset=0)
        print 'This is the first 100 items in the root folder:'
        for item in item_list:
            if next_folder == item.name:
                print "folder_found!"
                current_folder = item
                break
            else:
                print "missing_folder!"

        idx += 1
        # do find folder_id


    file_name = path_array.pop()
    # hacer un fectch si se puede subir el archivo...
    try:
        current_folder.preflight_check(name=file_name,size=0)
    except boxsdk.exception.BoxAPIException as ex:
        print ex.message
        item_list = current_folder.get_items(limit=100, offset=0)
        print "try remove file"
        for item in item_list:
            if item.name == file_name:
                item.delete()
                print "removed"
                break
            else:
                continue
                # remove the file
    finally:
        print "uploading file again"
        f = current_folder.upload_stream(f, file_name)
        print f.name
