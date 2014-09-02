#!/bin/sh

set -e

export VENDOR=lge
export DEVICE=d851
./../../$VENDOR/klte-common/extract-files.sh $@
