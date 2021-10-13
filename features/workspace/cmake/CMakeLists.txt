cmake_minimum_required(VERSION 3.0)

project(WorkspaceProject)

include(${CMAKE_BINARY_DIR}/conanworkspace.cmake)

# hack; inject conan_paths.cmake in each componant to resolve third part
# libraries
get_cmake_property(_variableNames VARIABLES)
list(SORT _variableNames)
foreach(_variableName ${_variable_names})
  if(_variableName MATCHES "^PACKAGE_(.*)_BUILDS$")
    set("CMAKE_PROJECT_${CMAKE_MATCH_1}_INCLUDE ${${_variableName}}/conan_paths.cmake"
    )
  endif()
endforeach()

conan_workspace_subdirectories()
