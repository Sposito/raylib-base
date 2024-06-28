cmake_minimum_required(VERSION 3.28)
project(raylib-base C)

set(CMAKE_C_STANDARD 11)

include(FetchContent)
FetchContent_Declare(
        raylib
        GIT_REPOSITORY https://github.com/raysan5/raylib.git
        GIT_TAG 5.0
)
FetchContent_MakeAvailable(raylib)

add_executable(raylib-base src/main.c
        src/cmd_handler.h
        src/utils.h)
target_link_libraries(raylib-base raylib)

# Create a testing build with the TESTING compile flag
add_executable(raylib-base-test src/main.c
        src/cmd_handler.h
        src/utils.h)
target_link_libraries(raylib-base-test raylib)
target_compile_definitions(raylib-base-test PRIVATE TESTING)
set_target_properties(raylib-base-test PROPERTIES COMPILE_FLAGS "-O0 -g")


enable_testing()
find_package (Python COMPONENTS Interpreter Development)

# TESTS BEGIN
add_test(NAME OpenClose COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/tests/run_test.py --test open_close)
set_tests_properties(OpenClose PROPERTIES TIMEOUT 30)
# TESTS END
