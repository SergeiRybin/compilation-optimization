cmake_minimum_required(VERSION 3.16)
project(BuildLoadLib)
include(LibSources.cmake)

# Add library source files from LibSources.cmake
add_library(${PROJECT_NAME} ${LIB_SOURCES})
target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR} include)
set_target_properties(${PROJECT_NAME} PROPERTIES
    CXX_STANDARD 11
    CXX_STANDARD_REQUIRED ON
)

# Enable precompiled headers usage
option(PCH_ENABLE "Use precompiled headers" ON)
if(PCH_ENABLE)
    target_precompile_headers(${PROJECT_NAME} PRIVATE
    "$<$<COMPILE_LANGUAGE:CXX>:<iostream$<ANGLE-R>>"
    "$<$<COMPILE_LANGUAGE:CXX>:<string$<ANGLE-R>>"
    )
endif(PCH_ENABLE)