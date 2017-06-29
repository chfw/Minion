# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /srv/minion

# Copy the current directory contents into the container at /app
ADD . /srv/minion

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN python setup.py install

# Make port 80 available to the world outside this container
EXPOSE 3000

# Define environment variable
ENV NAME Minion

# Run app.py when the container launches
CMD ["minion"]