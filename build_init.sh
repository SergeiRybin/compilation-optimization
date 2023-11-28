#!/bin/bash
set -e

cd ./lib/build_load_lib/
python generate.py 100 ../../src
cd -

cmake --no-warn-unused-cli \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=TRUE \
 -DCMAKE_C_COMPILER:FILEPATH=/usr/bin/clang \
 -DCMAKE_CXX_COMPILER:FILEPATH=/usr/bin/clang++ \
 -DSUPPRESS_ECOMMA=ON \
 -DAUTO_CCACHE=OFF \
 -DPCH_ENABLE=ON \
 -S. \
 -Bbuild \
 -G "Unix Makefiles"