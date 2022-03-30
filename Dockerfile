# # syntax=docker/dockerfile:1

# FROM python:3.10.3

# # ENV PYTHONUNBUFFERED 1

# # RUN mkdir /main

# WORKDIR /main
# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt

# COPY . .

# # COPY main.py /main
# # COPY app.py /main
# # COPY config.py /main

# # RUN pip install --upgrade 

# # COPY . /main
# ENV PORT = 5000

# EXPOSE 5000

# CMD [ "python", "main.py"]
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /newfolder
WORKDIR /newfolder
COPY requirements.txt /newfolder
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /newfolder
EXPOSE 5001
CMD [ "python", "main.py" ]