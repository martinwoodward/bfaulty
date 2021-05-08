import json
import os, sys
import time
import datetime
from azure.storage.blob import BlobServiceClient, ContentSettings
from retry import retry

class azuploader:
    def __init__(self, connection_string: str, root_path: str):
        self.connection_string = connection_string
        self.root_path = root_path
        self.container_name = "$web"

    @retry(delay=1, backoff=2, max_delay=64)
    def upload(self, filename: str):

        # Strip the root path from the filename to get relative path
        blob_filename = filename[-(len(filename)-len(self.root_path)-1):]
        print("Uploading", filename, "to", blob_filename)

        # Upload files
        # Connect to the Azure blob service
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        container_client = blob_service_client.get_container_client(self.container_name)

        # Create a blob in the storage account
        blob_client = blob_service_client.get_blob_client(container=self.container_name,
                                                        blob=blob_filename)

        # Filetype
        # Build the blob upload filename by removing the source folder
        filetype = filename.split(".")[-1]
        mimetype = "application/octet-stream"
        if filetype == "html":
            mimetype = "text/html"
        elif filetype == "jpg":
            mimetype = "image/jpeg"

        print("type: ", mimetype)

        # Read the file off disk and write it to the blob
        with open(filename, "rb") as data:
            blob_client.upload_blob(data, overwrite=True, content_settings = ContentSettings(content_type=mimetype))



