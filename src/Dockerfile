#__copyright__   = "Copyright 2024, VISA Lab"
#__license__     = "MIT"

# Define global args
ARG FUNCTION_DIR="/home/app/"
ARG RUNTIME_VERSION="3.8"
ARG DISTRO_VERSION="3.12"

FROM alpine:latest
FROM python:${RUNTIME_VERSION} AS python-alpine

#RUN apt-get update \
#    && apt-get install -y cmake ca-certificates libgl1-mesa-glx
RUN python${RUNTIME_VERSION} -m pip install --upgrade pip

FROM python-alpine AS build-image

# Include global args in this stage of the build
ARG FUNCTION_DIR
ARG RUNTIME_VERSION
# Create function directory
RUN mkdir -p ${FUNCTION_DIR}

# Install Lambda Runtime Interface Client for Python
RUN python${RUNTIME_VERSION} -m pip install awslambdaric --target ${FUNCTION_DIR}

# Stage 3 - final runtime image
# Grab a fresh copy of the Python image
FROM python-alpine
# Include global arg in this stage of the build
ARG FUNCTION_DIR
# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}
# Copy in the built dependencies
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

# Install ffmpeg
RUN apt-get update
RUN apt-get install -y python3-opencv

# Copy handler function
COPY requirements.txt ${FUNCTION_DIR}
COPY pytorch-requirements.txt ${FUNCTION_DIR}

RUN python${RUNTIME_VERSION} -m pip install -r requirements.txt --target ${FUNCTION_DIR}
RUN python${RUNTIME_VERSION} -m pip install -r pytorch-requirements.txt --target ${FUNCTION_DIR}
COPY entry.sh /

# Copy function code
COPY data.pt ${FUNCTION_DIR}
COPY face_recognition_code.py ${FUNCTION_DIR}
COPY handler.py ${FUNCTION_DIR}
ENV TORCH_HOME=/tmp/

RUN chmod 777 /entry.sh

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
ENTRYPOINT [ "/entry.sh" ]
CMD [ "handler.handler" ]