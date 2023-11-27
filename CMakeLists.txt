cmake_minimum_required(VERSION 3.0)

project(shapr3d VERSION 0.0.1)

# find_package(Boost COMPONENTS unit_test_framework REQUIRED)
# find_package(Threads REQUIRED)
add_subdirectory(lib)
add_executable(${CMAKE_PROJECT_NAME} src/main.cpp)
target_link_libraries(${CMAKE_PROJECT_NAME} MyCustomLibrary)

# target_include_directories(${CMAKE_PROJECT_NAME} PRIVATE include)
# target_link_libraries(${CMAKE_PROJECT_NAME} Threads::Threads)

# add_executable(appTest test/src/test.cpp)
# target_include_directories(appTest PRIVATE include)
# target_link_libraries(appTest ${Boost_UNIT_TEST_FRAMEWORK_LIBRARY} )

set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES
    CXX_STANDARD 17
    CXX_STANDARD_REQUIRED ON
    COMPILE_OPTIONS "-Wcomma;-Wpedantic;-Wall;-Wextra;-Werror"
)

# enable_testing()
# add_test(appTest appTest)

