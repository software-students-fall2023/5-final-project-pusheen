
FROM python:3.8

WORKDIR /app


COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000


ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]


# docker build -t alh8007/flaskapp .
# docker run -p 5000:5000 alh8007/flaskapp

