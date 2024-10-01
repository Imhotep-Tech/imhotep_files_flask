## Imhotep Files For Flask
This Python library simplifies file upload and deletion operations in web applications using Flask or similar frameworks. It includes two core functions:

upload_file: Handles file uploads with validation for allowed extensions and secure file saving.
delete_file: Safely deletes files from the server.
# Features
- Secure filename handling with werkzeug.utils.secure_filename.
- Validation for allowed file extensions.
- Error handling and debugging support for various scenarios.
- Clean and customizable file naming convention.
- Safe deletion of files with error handling.

# Installation
Before using the library, ensure you have the following dependencies installed:
```
pip install
```

# Usage
1. Uploading a File
The upload_file function handles uploading files to a specified folder with validations such as allowed extensions, correct file name format, and ensuring a file is provided.
```python
upload_file(request, upload_folder, allowed_extensions, file_name)
```
    
Parameters:
- request: The incoming HTTP request object that contains the file.
- upload_folder: The target folder path where the file will be saved.
- allowed_extensions: A list of allowed file extensions (e.g., ['.jpg', '.png', '.txt']).
- file_name: The base name for the file (without extension).

Returns:
- The full path to the uploaded file if successful.
- Error message if there is an issue.

2. Deleting a File
The delete_file function handles removing files from the filesystem with safety checks and error handling.
```python
delete_file(file_path):
```
Parameters:
file_path: The full path to the file that needs to be deleted.
Returns:
A success message if the file is deleted.
Error message if there is an issue (e.g., file does not exist).

# Function Details
upload_file(request, upload_folder, allowed_extensions, file_name)
This function is responsible for handling file uploads with the following steps:

1. Validates that allowed extensions and upload folder are provided.
2. Ensures the file name does not include an extension or start with a dot.
3. Checks for the presence of a file in the request.
4. Validates the file’s extension.
5. Saves the file in the specified upload folder with a secure name.
Example Flow:
- User uploads a .jpg file named picture.jpg.
- You pass 'profile_picture' as file_name, so the file will be saved as profile_picture.jpg in the upload folder.

delete_file(file_path)
This function safely deletes a file from the given path. It performs the following:

1. Checks if the file path is valid.
2. Ensures the file exists.
3. Tries to delete the file and handles any exceptions.

# Example
1. Uploading a File
   ```python
   from flask import Flask, request
   from imhotep_files_flask import upload_file
   @app.route("/file_upload", methods=["POST"])
   def file_upload():
        user_id = 1

        photo_path, upload_error = upload_file(request, "path/to/your/upload/file/directory" , (".png", ".jpg", ".jpeg"), user_id)
        if upload_error:
            print(upload_error)
            return upload_error
        if photo_path:
        # File uploaded successfully, do something with the file path
        return "File uploaded successfully!"
   ```
1. Deleting a File
      ```python
   from flask import Flask, request
   from imhotep_files_flask import delete_file
   @app.route("/file_delete", methods=["POST"])
   def file_delete():
         file_path = "path/to/the/file/you/wants/to/delete"
    
         file_delete , error = delete_file(file_path)
         if error:
            print(error)
            return error
         if file_delete:
         # File deleted successfully, do something pn the database for example
         return "File deleted successfully!"
   ```

# Error Handling
Both functions return clear error messages in case of failure:

- upload_file returns descriptive error messages such as "No file uploaded", "Invalid file format", or "File name parameter should not include an extension".
- delete_file returns errors like "File path must be a non-empty string" or "Error deleting file: <error details>".

# Contributing
Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.

# License
This project is licensed under the MIT License.
