FROM docker.io/library/alpine:latest
RUN apk add tmux ruby python3 py3-pip
# I do what I want
RUN python3 -m pip install --upgrade --break-system-packages Pillow
WORKDIR /src
