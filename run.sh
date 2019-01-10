#!/bin/bash

function build() {
  docker build -t phelp_img -f Docker/Dockerfile .
}

function run() {
  docker run phelp_img python3 main.py
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
