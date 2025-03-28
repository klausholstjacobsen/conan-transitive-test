set(CMAKE_VERBOSE_MAKEFILE ON CACHE STRING "")

project (Test LANGUAGES CXX)

find_package(CURL CONFIG REQUIRED)

add_executable(${PROJECT_NAME}
    main.cpp
)

target_link_libraries(${PROJECT_NAME} PUBLIC
  CURL::libcurl
)
