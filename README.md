# Playing Video With 5,170 tmux Windows

[Read more about it on my blog](https://willhbr.net/2025/03/17/playing-video-with-5170-tmux-windows/)

Tested tested in an Alpine podman container with tmux 3.5a.

- turn a video into images: `ffmpeg -i video.mp4 -r 2 frames/output_%04d.png`
- compile the images into tmux and run it: `pod run` (using [pod](https://pod.willhbr.net))
