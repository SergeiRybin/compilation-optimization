#!/bin/bash
cd build && time cmake --build . --clean-first -j`nproc - 1`