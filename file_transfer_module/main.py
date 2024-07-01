import configparser
import os
import sys
from file_transfer_module.aws_manager import upload_file_to_s3
from file_transfer_module.gcs_manager import upload_file_to_gcs
from file_transfer_module.file_processor import get_files

def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def main(config_file, directory):
    config = read_config(config_file)
    files = get_files(directory)

    aws_bucket = config.get('AWS', 'BucketName')
    gcs_bucket = config.get('GCS', 'BucketName')

    for file in files['images'] + files['media']:
        upload_file_to_s3(file, aws_bucket)

    for file in files['documents']:
        upload_file_to_gcs(file, gcs_bucket, os.path.basename(file))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <config_file> <directory>")
        sys.exit(1)

    config_file = sys.argv[1]
    directory = sys.argv[2]
    main(config_file, directory)
