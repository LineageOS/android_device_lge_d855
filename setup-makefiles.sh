#!/bin/bash

set -e

export VENDOR=lge
export DEVICE=vs985
./../../$VENDOR/g3-common/setup-makefiles.sh $@
