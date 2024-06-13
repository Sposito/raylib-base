cmake_minimum_required(VERSION 3.28)
project(raylib_base C)

set(CMAKE_C_STANDARD 11)


#

include(FetchContent)
FetchContent_Declare(
        raylib
        GIT_REPOSITORY https://github.com/raysan5/raylib.git
        GIT_TAG 5.0
)
FetchContent_MakeAvailable(raylib)

add_executable(raylib_base main.c)
target_link_libraries(raylib_base raylib)

