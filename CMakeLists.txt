cmake_minimum_required(VERSION 3.16)

# Enable env variables for PCH and CCACHE co-usage
set(ENV{CCACHE_SLOPPINESS} pch_defines,time_macros)

# Enable CCACHE
option(AUTO_CCACHE "Use ccache to speed up rebuilds" ON)
find_program(CCACHE_PROGRAM ccache)
if(CCACHE_PROGRAM AND ${AUTO_CCACHE})
  message(STATUS "Using ${CCACHE_PROGRAM} as compiler launcher")
  set(CMAKE_CXX_COMPILER_LAUNCHER "${CCACHE_PROGRAM}")
endif()

# Enable build profiling
option(BUILD_PROF "Use clang buid tracing for profiling" OFF)
if(BUILD_PROF)
    add_compile_options(-ftime-trace)
endif(BUILD_PROF)

# Check the build type and set compilation flags accordingly
if(CMAKE_BUILD_TYPE STREQUAL "Release")
    message("Release build")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O3")
elseif(CMAKE_BUILD_TYPE STREQUAL "Debug")
    message("Debug build")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0 -g")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O0 -g")
else()
    message(FATAL_ERROR "Unsupported build type: ${CMAKE_BUILD_TYPE}")
endif()

project(shapr3d VERSION 0.0.1)

# Specify C++ standard
set(CXX_STANDARD 17)
set(CXX_STANDARD_REQUIRED ON)

# Specify compilation flags
add_compile_options(-Wcomma)
add_compile_options(-Wpedantic -Wall -Wextra -Werror)

option(SUPPRESS_ECOMMA "Turn comma errors to warnings" OFF)
if(SUPPRESS_ECOMMA)
    add_compile_options(-Wno-error=comma)
endif(SUPPRESS_ECOMMA)

# Build custom library with build load and Miniz wrapper
add_subdirectory(lib)

# Build main app that uses build load and Miniz wrapper
add_executable(${CMAKE_PROJECT_NAME} src/main.cpp src/build_load.cpp)
target_include_directories(${CMAKE_PROJECT_NAME} PRIVATE src)
target_link_libraries(${CMAKE_PROJECT_NAME} MyCustomLibrary)

