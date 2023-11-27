cmake_minimum_required(VERSION 3.16)
include(LibSources.cmake)

set(ENV{CCACHE_SLOPPINESS} pch_defines,time_macros)

option(AUTO_CCACHE "Use ccache to speed up rebuilds" ON)
find_program(CCACHE_PROGRAM ccache)
if(CCACHE_PROGRAM AND ${AUTO_CCACHE})
  message(STATUS "Using ${CCACHE_PROGRAM} as compiler launcher")
  set(CMAKE_CXX_COMPILER_LAUNCHER "${CCACHE_PROGRAM}")
endif()

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

set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES
    CXX_STANDARD 11
    CXX_STANDARD_REQUIRED ON
    COMPILE_OPTIONS "-Wpedantic;-Wall;-Wextra;-Werror"
)

project(MyDummyLibrary)

add_library(${PROJECT_NAME} ${LIB_SOURCES})

target_precompile_headers(${PROJECT_NAME} PRIVATE
    "$<$<COMPILE_LANGUAGE:CXX>:<iostream$<ANGLE-R>>"
    "$<$<COMPILE_LANGUAGE:CXX>:<string$<ANGLE-R>>"
)

target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR} include)