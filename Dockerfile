FROM python:3.11-slim

WORKDIR /app

# Install required system packages (if needed)
RUN apt update && apt install -y git curl && rm -rf /var/lib/apt/lists/*

# Copy your project files
COPY . /app/

# Upgrade pip & install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run your bot
CMD ["python", "main.py"]
