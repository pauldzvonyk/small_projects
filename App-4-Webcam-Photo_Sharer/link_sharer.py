import dropbox
from dropbox import files
from dropbox import exceptions
from dropbox import sharing
import os


class Uploader:
    def __init__(self, access_token_file='files/token.txt'):
        with open(access_token_file, 'r') as f:
            self.ACCESS_TOKEN = f.read()

        self.dbx = dropbox.Dropbox(self.ACCESS_TOKEN)
        self.last_uploaded_local_path = None
        self.last_uploaded_dropbox_path = None

    def upload_file(self, local_file_path, dropbox_folder='/files_to_share'):
        try:
            with open(local_file_path, "rb") as f:
                file_name = os.path.basename(local_file_path)
                dropbox_path = f"{dropbox_folder}/{file_name}"

                # Upload the file to Dropbox only if not already uploaded
                if self.last_uploaded_local_path != local_file_path:
                    uploaded_file = self.dbx.files_upload(f.read(), dropbox_path,
                                                          mode=dropbox.files.WriteMode("overwrite"))
                    self.last_uploaded_local_path = local_file_path
                    self.last_uploaded_dropbox_path = uploaded_file.path_lower
                    return self.last_uploaded_dropbox_path
                else:
                    print("File already uploaded.")
                    return self.last_uploaded_dropbox_path
        except dropbox.exceptions.ApiError as e:
            print(f"Error uploading file to Dropbox: {e}")
            return None

    def share_file(self):
        try:
            # Check if a file has been uploaded
            if self.last_uploaded_local_path:
                print(f"File to share: {self.last_uploaded_local_path}")

                # Check if a shared link already exists
                existing_links = self.dbx.sharing_list_shared_links(self.last_uploaded_dropbox_path).links
                if existing_links:
                    return existing_links[0].url  # Return the existing link
                else:
                    # Create a new shared link
                    settings = dropbox.sharing.SharedLinkSettings(
                        requested_visibility=dropbox.sharing.RequestedVisibility.public)
                    shared_link = self.dbx.sharing_create_shared_link_with_settings(self.last_uploaded_dropbox_path,
                                                                                    settings)
                    return shared_link.url
            else:
                print("No file has been uploaded yet.")
                return None
        except dropbox.exceptions.ApiError as e:
            print(f"Error creating/shareable link: {e}")
            return None

# EXAMPLES OF USAGES
# # Create an instance of Uploader
# file_uploader = Uploader()
# file_path = 'FILE_PATH_TO_UPLOAD_AND_SHARE'
#
# # Upload the file
# uploaded_path = file_uploader.upload_file(file_path)
# if uploaded_path:
#     print(f"File uploaded to Dropbox: {uploaded_path}")
#
# # Get the shareable link
# shareable_link = file_uploader.share_file()
# if shareable_link:
#     print(f"Shareable link: {shareable_link}")
