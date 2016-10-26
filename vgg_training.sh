#!/usr/bin/env sh

./build/tools/caffe train \
    --solver=vggface2/solver.prototxt \
    --weights=vggface2/VGG_FACE.caffemodel -gpu 0
