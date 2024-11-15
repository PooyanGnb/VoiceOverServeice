import uuid
from pathlib import Path
import shutil


def cleanup_directory(directory_path):
    shutil.rmtree(directory_path, ignore_errors=True)


def generate_unique_path(base_dir="temp"):
    """Generate a unique directory for a request."""
    unique_id = uuid.uuid4().hex
    path = Path(base_dir) / unique_id
    path.mkdir(parents=True, exist_ok=True)
    return path