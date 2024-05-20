
            FROM mcr.microsoft.com/powershell

            # Set the working directory in the container
            WORKDIR /app

            # Copy the PowerShell script into the container
            COPY script.ps1 .

            # Command to run the PowerShell script
            CMD ["pwsh", "-File", "script.ps1"]
            