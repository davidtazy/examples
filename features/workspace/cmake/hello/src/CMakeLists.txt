cmake_minimum_required(VERSION 2.8.12)
project(Hello)

if(NOT TARGET say::say)
  find_package(say REQUIRED)
endif()

add_library(hello hello.cpp)
add_library(hello::hello ALIAS hello)

target_link_libraries(hello PUBLIC say::say)
target_include_directories(hello PUBLIC .)
