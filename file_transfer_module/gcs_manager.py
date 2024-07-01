from google.cloud import storage as gcs_storage

def upload_file_to_gcs(gcs_bucket, local_file_path, gcs_blob_name):
    gcs_client = gcs_storage.Client()
    bucket = gcs_client.bucket(gcs_bucket)
    blob = bucket.blob(gcs_blob_name)
    blob.upload_from_filename(local_file_path)
    print(f"Uploaded file {local_file_path} to GCS bucket {gcs_bucket} as {gcs_blob_name}.")
