#!/bin/sh

set -e

export VENDOR=lge
export DEVICE=vs985
./../../$VENDOR/g3-common/extract-files.sh $@
