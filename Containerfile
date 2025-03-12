FROM docker.io/library/alpine:latest
RUN apk add tmux ruby
WORKDIR /src
