## File Transfer Module

Overview

The File Transfer Module is a Python package that scans a specified directory and its subdirectories for files. It classifies files into images, media, and documents, and then uploads them to cloud storage services. Images and media files are uploaded to AWS S3, while documents are uploaded to Google Cloud Storage. The types of files to be uploaded to each service are configurable.

## Features

- Scans a directory and its subdirectories for files.
- Categorizes files into images, media, and documents.
- Uploads images and media files to AWS S3.
- Uploads document files to Google Cloud Storage.
- Configurable file types for each cloud storage service.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/augastyaa-commits/SecondProject.git
   
    ```

2. **Install the package**:

    ```bash
    pip install .
    ```

3. **Install required dependencies**:

    ```bash
    pip install -r requirements.txt
 
