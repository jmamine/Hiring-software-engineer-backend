# # app/utils.py



# import os , uuid
# from flask import jsonify
# import logging
# from app import app 



# logger = logging.getLogger(__name__)



# def upload_script(request):
#     try:
#         code_file = request.files.get('file')
#         requirements_file = request.files.get('requirements')

#         if not code_file or code_file.filename == '':
#             return jsonify({"error": "No code file provided"}), 400

#         task_id = str(uuid.uuid4())
#         task_folder = os.path.join(app.config['UPLOAD_FOLDER'], task_id)
#         os.makedirs(task_folder, exist_ok=True)

#         code_filename = "code.py"
#         code_file_path = os.path.join(task_folder, code_filename)
#         code_file.save(code_file_path)

#         if requirements_file:
#             requirements_filename = "requirements.txt"
#             requirements_file_path = os.path.join(task_folder, requirements_filename)
#             requirements_file.save(requirements_file_path)
#         else:
#             requirements_filename = "requirements.txt"
#             requirements_file_path = os.path.join(task_folder, requirements_filename)
#             # Create an empty file
#             with open(requirements_file_path, 'w') as f:
#                 pass


#         return task_id
            
#     except Exception as e:
#         logger.exception("Error occurred during script upload:")
#         return jsonify({"error": "An error occurred during script upload"}), 500


# app/utils.py


import os
import uuid
import logging
from flask import jsonify
from app import app

# Setting up logging
logger = logging.getLogger(__name__)

# Function to handle script upload
def upload_script(request):
    try:
        # Getting files from request
        code_file = request.files.get('file')
        requirements_file = request.files.get('requirements')

        # Checking if code file is provided
        if not code_file or code_file.filename == '':
            return jsonify({"error": "No code file provided"}), 400

        # Generating unique task id
        task_id = str(uuid.uuid4())

        # Creating task folder
        task_folder = os.path.join(app.config['UPLOAD_FOLDER'], task_id)
        os.makedirs(task_folder, exist_ok=True)

        # Saving code file
        code_filename = "code.py"
        code_file_path = os.path.join(task_folder, code_filename)
        code_file.save(code_file_path)

        # Saving requirements file if provided, else create an empty requirements file
        if requirements_file:
            requirements_filename = "requirements.txt"
            requirements_file_path = os.path.join(task_folder, requirements_filename)
            requirements_file.save(requirements_file_path)
        else:
            requirements_filename = "requirements.txt"
            requirements_file_path = os.path.join(task_folder, requirements_filename)
            # Create an empty file
            with open(requirements_file_path, 'w') as f:
                pass

        # Returning task id
        return task_id

    # Handling exceptions
    except Exception as e:
        logger.exception("Error occurred during script upload:")
        return jsonify({"error": "An error occurred during script upload"}), 500
