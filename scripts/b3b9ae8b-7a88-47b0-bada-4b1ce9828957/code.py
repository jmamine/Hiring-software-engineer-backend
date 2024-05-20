

# total = 0







# for i in range(1, 11):





#     total += i







# print("The sum of the first ten positive integers is:", total)


# simple_script.py
import requests

def main():
    try:
        response = requests.get("https://api.github.com")
        print("Status code:", response.status_code)
        print("Requirements are well used!")
    except ImportError:
        print("Failed to import necessary packages. Make sure to install the requirements.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()


# import schedule
# import time

# def print_hi():
#     print("Hi")

# schedule.every(1).seconds.do(print_hi)

# while True:
#     schedule.run_pending()
#     time.sleep(1)



# Example Python script file using schedule
# import schedule
# import time

# def job():
#     print("Job is running...")

# if __name__ == "__main__":
#     schedule.every(2).seconds.do(job)  # Change 1 to 10 for every 10 seconds
#     while True:
#         schedule.run_pending()
#         time.sleep(1)









# def create_python_task(request):
    

#     code_file = request.files.get('file')  # Assuming 'file' is the key for the Python file upload

#     # Read the content of the uploaded Python file
#     code = code_file.read().decode('utf-8')

#     # Encode the user's code using base64
#     encoded_code = base64.b64encode(code.encode('utf-8')).decode('utf-8')

#     # Define Dockerfile content to create a Python script container
#     dockerfile_content = f'''
#     FROM python:3.8

#     WORKDIR /app
#     COPY . .
#     CMD python -c "$(echo '{encoded_code}' | base64 -d)"
#     '''

#     # Build Docker image from Dockerfile content
#     image, _ = client.images.build(fileobj=io.BytesIO(dockerfile_content.encode('utf-8')), rm=True)

#     # Run a container from the built image
#     container = client.containers.run(image, detach=True)

#     # Generate a unique task ID
#     task_id = str(uuid.uuid4())

#     # Store the task, its corresponding container, and script type in the tasks dictionary
#     tasks[task_id] = {'container': container, 'script_type': 'python'}

#     return jsonify({"message": f"Task {task_id} created successfully!", "script_type": "python", "task_id": task_id})



# def create_python_task(request):
#     code_file = request.files.get('file')  # Assuming 'file' is the key for the Python file upload
#     requirements_file = request.files.get('requirements')  # Assuming 'requirements' is the key for the requirements file upload

#     # Read the content of the uploaded Python file
#     code = code_file.read().decode('utf-8')

#     # Read the content of the requirements file
#     requirements = requirements_file.read().decode('utf-8') if requirements_file else ''

#     # Encode the user's code and requirements using base64
#     encoded_code = base64.b64encode(code.encode('utf-8')).decode('utf-8')
#     encoded_requirements = base64.b64encode(requirements.encode('utf-8')).decode('utf-8')

#     # Define Dockerfile content to create a Python script container
#     dockerfile_content = f'''
#     FROM python:3.8

#     WORKDIR /app
#     COPY . .
#     RUN pip install -r "$(echo '{encoded_requirements}' | base64 -d)"
#     CMD python -c "$(echo '{encoded_code}' | base64 -d)"
#     '''

#     # Build Docker image from Dockerfile content
#     image, _ = client.images.build(
#         fileobj=io.BytesIO(dockerfile_content.encode('utf-8')),
#         rm=True)

#     # Run a container from the built image
#     container = client.containers.run(image, detach=True)

#     # Generate a unique task ID
#     task_id = str(uuid.uuid4())

#     # Store the task, its corresponding container, and script type in the tasks dictionary
#     tasks[task_id] = {'container': container, 'script_type': 'python'}

#     return jsonify({"message": f"Task {task_id} created successfully!", "script_type": "python", "task_id": task_id})



# def create_python_task(request):
#     code_file = request.files.get('file')  # Assuming 'file' is the key for the Python file upload
#     requirements_file = request.files.get('requirements')  # Assuming 'requirements' is the key for the requirements file upload

#     # Read the content of the uploaded Python file
#     code = code_file.read().decode('utf-8')

#     # Read the content of the requirements file
#     requirements = requirements_file.read().decode('utf-8') if requirements_file else ''

#     # Encode the user's code and requirements using base64
#     encoded_code = base64.b64encode(code.encode('utf-8')).decode('utf-8')
#     encoded_requirements = base64.b64encode(requirements.encode('utf-8')).decode('utf-8')

#     # Define Dockerfile content to create a Python script container
#     dockerfile_content = f'''
#     FROM python:3.8

#     WORKDIR /app
#     COPY . .
#     RUN pip install -r requirements.txt
#     CMD python -c "$(echo '{encoded_code}' | base64 -d)"
#     '''

#     # Build Docker image from Dockerfile content
#     image, _ = client.images.build(
#         fileobj=io.BytesIO(dockerfile_content.encode('utf-8')),
#         rm=True,
#         buildargs={'requirements.txt': base64.b64decode(encoded_requirements).decode('utf-8')}
#     )

#     # Run a container from the built image
#     container = client.containers.run(image, detach=True)

#     # Generate a unique task ID
#     task_id = str(uuid.uuid4())

#     # Store the task, its corresponding container, and script type in the tasks dictionary
#     tasks[task_id] = {'container': container, 'script_type': 'python'}

#     return jsonify({"message": f"Task {task_id} created successfully!", "script_type": "python", "task_id": task_id})