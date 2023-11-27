# CMakeLists.txt
cmake_minimum_required(VERSION 3.16)
project(MinizWrapper)

# Add your library source files
add_subdirectory(miniz)

set_target_properties(miniz PROPERTIES
    CXX_STANDARD 17
    CXX_STANDARD_REQUIRED ON
    COMPILE_OPTIONS "-Wcomma;-Wpedantic;-Wall;-Wextra;-Werror"
)

add_library(${PROJECT_NAME} src/string_ops.cpp)
target_include_directories(${PROJECT_NAME} PRIVATE miniz)
target_include_directories(${PROJECT_NAME} PUBLIC include)

# Include the current source directory
target_link_libraries(${PROJECT_NAME} miniz)

