# CMakeLists.txt
cmake_minimum_required(VERSION 3.16)
project(MyCustomLibrary)

add_subdirectory(miniz_wrapper)
add_subdirectory(build_load_lib)

# Add your library source files
add_library(${PROJECT_NAME} INTERFACE)

# Include the current source directory
target_link_libraries(${PROJECT_NAME} INTERFACE MinizWrapper)
target_link_libraries(${PROJECT_NAME} INTERFACE BuildLoadLib)

