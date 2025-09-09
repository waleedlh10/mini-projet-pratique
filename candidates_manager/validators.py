from django.core.exceptions import ValidationError
import time, os


def validate_cv_file(file):
    allowed_extensions = ["pdf", "doc", "docx"]
    ext = file.name.split(".")[-1].lower()
    if ext not in allowed_extensions:
        raise ValidationError("Only PDF, DOC, or DOCX files are allowed.")

    max_size = 5 * 1024 * 1024
    if file.size > max_size:
        raise ValidationError("File size must be under 5MB.")


def cv_upload_path(instance, filename):
    """
    Generate file path: candidates/cvs/<name>_<timestamp>.<ext>
    """
    ext = filename.split(".")[-1].lower()
    name_clean = instance.name.replace(" ", "_")
    timestamp = int(time.time())
    filename = f"{name_clean}__{timestamp}.{ext}"
    return os.path.join("CVs/", filename)
