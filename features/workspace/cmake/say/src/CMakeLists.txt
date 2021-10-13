cmake_minimum_required(VERSION 2.8.12)

project(Say)

add_library(say say.cpp)
add_library(say::say ALIAS say)
target_include_directories(say PUBLIC .)
