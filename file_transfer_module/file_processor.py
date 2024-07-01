import os

def get_files(directory):
    file_types = {
        "images": ["jpg", "png", "svg", "webp"],
        "media": ["mp3", "mp4", "mpeg4", "wmv", "3gp", "webm"],
        "documents": ["doc", "docx", "csv", "pdf"]
    }
    files = {"images": [], "media": [], "documents": []}

    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            ext = filename.split('.')[-1].lower()
            for file_type, extensions in file_types.items():
                if ext in extensions:
                    files[file_type].append(file_path)
                    break  # Break to avoid adding the file to multiple categories

    return files
