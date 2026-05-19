# Step 1: Use an official, lightweight Python runtime image as a parent image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY app.py /app/

# Step 4: Expose port 80 to the outside world
EXPOSE 80

# Step 5: Define the command to run the app when the container launches
CMD ["python", "app.py"]
