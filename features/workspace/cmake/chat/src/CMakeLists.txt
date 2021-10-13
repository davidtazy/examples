cmake_minimum_required(VERSION 2.8.12)
project(Chat)

# company library can be in super build
if(NOT TARGET hello::hello)
  find_package(hello REQUIRED)
endif()

# assume that third part library never in super build
find_package(ZLIB REQUIRED)

add_library(chat chat.cpp)
target_link_libraries(chat PUBLIC hello::hello)

add_executable(app app.cpp)
target_link_libraries(app chat ZLIB::ZLIB)
