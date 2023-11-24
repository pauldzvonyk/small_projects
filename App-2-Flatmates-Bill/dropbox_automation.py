import dropbox
import hashlib
import dropbox.files
import os

# Replace with your Dropbox access token
with open("token.txt", 'r') as f:
    ACCESS_TOKEN = f.read()

dbx = dropbox.Dropbox(ACCESS_TOKEN)


def upload_bills():
    for bill in os.listdir("my_files"):
        with open(os.path.join("my_files", bill), "rb") as f:
            data = f.read()
            dbx.files_upload(data, f"/{bill}")


def download_bills():
    for entry in dbx.files_list_folder("").entries:
        dbx.files_download_to_file(os.path.join("my_files", entry.name), f"/{entry.name}")


def dropbox_content_hash(file):
    hash_chunk_size = 4 * 1024 * 1024
    with open(file, "rb") as f:
        block_hashes = bytes()
        while True:
            chunk = f.read(hash_chunk_size)
            if not chunk:
                break
            block_hashes += hashlib.sha256(chunk).digest()
        return hashlib.sha256(block_hashes).hexdigest()


def download_changed():
    for entry in dbx.files_list_folder("").entries:
        if os.path.exists(os.path.join("my_files", entry.name)):
            local_hash = dropbox_content_hash(os.path.join("my_files", entry.name))
            if local_hash != entry.content_hash:
                print('FILE HAS CHANGED', entry.name)
                dbx.files_download_to_file(os.path.join("my_files", entry.name), f"/{entry.name}")
            else:
                print("FILE UNCHANGED", entry.name)
        else:
            print("NEW FILE", entry.name)
            dbx.files_download_to_file(os.path.join("my_files", entry.name), f"/{entry.name}")


def upload_changed():
    # Create a dictionary with cloud file names as keys and hashes as values
    cloud_files = {e.name: e.content_hash for e in dbx.files_list_folder("").entries}
    for file in os.listdir("my_files"):
        if file in cloud_files.keys():
            # Compute local hash
            local_hash = dropbox_content_hash(os.path.join("my_files", file))
            if local_hash != cloud_files[file]:
                print("FILE CHANGED: ", file)
                with open(os.path.join("my_files", file), "rb") as f:
                    data = f.read()
                    dbx.files_upload(data, f"/{file}", mode=dropbox.files.WriteMode("overwrite"))
            else:
                print("UNCHANGED", file)
        else:
            print("NEW FILE", file)
            with open(os.path.join("my_files", file), "rb") as f:
                data = f.read()
                dbx.files_upload(data, f"/{file}", mode=dropbox.files.WriteMode("overwrite"))

upload_changed()