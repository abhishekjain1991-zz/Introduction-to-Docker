FROM hypriot/rpi-node:0.12.0

#Install required packages
RUN apt-get update
RUN apt-get -y install python

# Add our python app code to the image
RUN mkdir -p /app
ADD . /app
WORKDIR /app







