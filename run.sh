#!/bin/bash

IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
/usr/X11/bin/xhost +

function build() {
    docker build -t phelp_img -f Docker/Dockerfile .
}

function run() {
    docker run --rm -it \
        -v $PWD/data:/data \
        -e DISPLAY=$IP:0 \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        phelp_img \
        python3 main.py
}

case $1 in
build)
    build
    ;;
run)
    run
    ;;
*)
    build
    run
    ;;
esac
