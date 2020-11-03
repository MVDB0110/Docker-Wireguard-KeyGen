FROM ubuntu:latest

WORKDIR /keygen
ADD . /keygen
RUN apt update && apt install wireguard-tools python3-pip -y
RUN pip3 install flask
EXPOSE 80
CMD [ "python3", "app.py" ]