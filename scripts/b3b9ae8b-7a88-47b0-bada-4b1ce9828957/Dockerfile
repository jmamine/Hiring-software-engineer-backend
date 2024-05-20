
            FROM python:3.8

            # Set the working directory in the container
            WORKDIR /app

            # Copy the requirements file into the container
            COPY requirements.txt .

            # Install Python dependencies
            RUN pip install -r requirements.txt

            # Copy the Python script into the container
            COPY code.py .

            # Command to run the Python script
            CMD ["python", "code.py"]
            