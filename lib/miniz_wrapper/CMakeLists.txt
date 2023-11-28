# CMakeLists.txt
cmake_minimum_required(VERSION 3.16)
project(MinizWrapper)

# Build Miniz library
add_subdirectory(miniz)

# Add library source files
add_library(${PROJECT_NAME} src/string_ops.cpp)
target_include_directories(${PROJECT_NAME} PRIVATE miniz)
target_include_directories(${PROJECT_NAME} PUBLIC include)

# Include the current source directory
target_link_libraries(${PROJECT_NAME} miniz)
