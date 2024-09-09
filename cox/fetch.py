from google.cloud import storage
import os

def download_blob(bucket_name, blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Download the blob to a file
    blob.download_to_filename(destination_file_name)
    print(f"Downloaded {blob_name} to {destination_file_name}.")

def main():
    bucket_name = 'audioprobe'
    blobs = [
  "2024-09-09 23:03:39.235405",
  "2024-09-09 23:04:00.940375",
  "2024-09-09 23:04:09.423531",
  "2024-09-09 23:04:28.784388",
  "2024-09-09 23:05:11.517816",
  "2024-09-09 23:05:21.571042",
  "2024-09-09 23:05:43.570130",
  "2024-09-09 23:06:12.190154",
  "2024-09-09 23:06:33.336258",
  "2024-09-09 23:06:53.501875",
  "2024-09-09 23:07:11.299027",
  "2024-09-09 23:07:23.363733",
  "2024-09-09 23:07:37.087076",
  "2024-09-09 23:07:52.608464",
  "2024-09-09 23:08:03.892618",
  "2024-09-09 23:08:20.706135",
  "2024-09-09 23:09:01.319258",
  "2024-09-09 23:09:13.183217",
  "2024-09-09 23:09:36.873176",
  "2024-09-09 23:10:23.132622",
  "2024-09-09 23:10:38.234884",
  "2024-09-09 23:11:03.731418",
  "2024-09-09 23:11:18.079991",
  "2024-09-09 23:11:43.516481",
  "2024-09-09 23:12:23.737328",
  "2024-09-09 23:12:37.518426",
  "2024-09-09 23:12:49.347099",
  "2024-09-09 23:13:05.283830",
  "2024-09-09 23:13:30.209511",
  "2024-09-09 23:14:12.624157"
    ]

    download_path = 'C:\\Users\\james\\Desktop\\cox\\'

    for blob_name in blobs:
        # Replace invalid characters for Windows filenames
        safe_blob_name = blob_name.replace(':', '-')
        destination_file_name = os.path.join(download_path, safe_blob_name)
        download_blob(bucket_name, blob_name, destination_file_name)

if __name__ == '__main__':
    main()
