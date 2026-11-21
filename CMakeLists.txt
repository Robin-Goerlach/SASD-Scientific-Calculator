cmake_minimum_required(VERSION 3.20)
project(SASDScientificCalculator VERSION 0.1.0 LANGUAGES CXX)

# Development options: the present code is a generic modern RPN arithmetic
# foundation, NOT a historical CPU/firmware emulator or a native iOS app.
option(SASD_SCIENTIFIC_BUILD_CLI "Build the headless development CLI" ON)
option(SASD_SCIENTIFIC_BUILD_TESTS "Build unit tests" ON)

add_library(sasd_scientific_core STATIC
    src/rpn_engine.cpp
)
add_library(SASD::ScientificCore ALIAS sasd_scientific_core)

target_include_directories(sasd_scientific_core PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)
target_compile_features(sasd_scientific_core PUBLIC cxx_std_20)
if(MSVC)
    target_compile_options(sasd_scientific_core PRIVATE /W4 /permissive-)
else()
    target_compile_options(sasd_scientific_core PRIVATE -Wall -Wextra -Wpedantic)
endif()

if(SASD_SCIENTIFIC_BUILD_CLI)
    add_executable(sasd-scientific-cli apps/cli/main.cpp)
    target_link_libraries(sasd-scientific-cli PRIVATE SASD::ScientificCore)
endif()

if(SASD_SCIENTIFIC_BUILD_TESTS)
    enable_testing()
    add_executable(sasd-scientific-tests tests/rpn_engine_test.cpp)
    target_link_libraries(sasd-scientific-tests PRIVATE SASD::ScientificCore)
    add_test(NAME core-rpn COMMAND sasd-scientific-tests)
endif()
