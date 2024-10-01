from werkzeug.utils import secure_filename
import os

def upload_file(request, upload_folder, allowed_extensions, file_name):

    file_name = str(file_name)
    # Validate allowed extensions
    if not allowed_extensions:
        return None, "No allowed extensions"

    # Validate upload folder
    if not upload_folder:
        return None, "No upload folder is given"

     # Validate file_name parameter (should not include extension)
    if file_name.startswith("."):
        return None, "The file name parameter should not start with a dot"
    if os.path.splitext(file_name)[1]:
        return None, "The file name parameter should not include an extension"

    # Check if file was uploaded
    if "file" not in request.files:
        return None, "No file uploaded"  # Return error message

    # Retrieve the uploaded file
    file = request.files['file']
    # Check if a file was selected
    if file.filename == '':
        return None, "No selected file"  # Return error message

    filename = secure_filename(file.filename)
    file_extension = os.path.splitext(filename)[1].lower()   # Extract extension with case-insensitivity

    # Validate the file extension
    if file_extension not in allowed_extensions:
        allowed_extensions_str = ', '.join(allowed_extensions)
        return None, f"Invalid file format. Allowed formats are : {allowed_extensions_str}"  # Return error message
    
    # Create the new file name
    file_name_new = f"{file_name}{file_extension}"

    # Construct the full file path
    file_path = os.path.join(upload_folder, file_name_new)

    try:
        # Save the file
        file.save(file_path)
        return file_path, None   # Return the saved file path
    except Exception as e:
        # Handle exceptions (consider more specific handling in production)
        return None, str(e)   # error message for debugging

def delete_file(file_path):
        if not file_path or not isinstance(file_path, str):
            return None, "File path must be a non-empty string"
        
        if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    return "File Deleted", None
                except OSError  as e:
                    # Handle exceptions (consider more specific handling in production)
                    return None, f"Error deleting file: {e}"   # error message for debugging
        else:
            return None, "No image associated with this user to delete."
