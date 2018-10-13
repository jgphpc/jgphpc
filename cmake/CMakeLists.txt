cmake_minimum_required(VERSION 3.3)
project(papi-wrap)
enable_language(CXX C Fortran)

# https://cmake.org/cmake-tutorial/
# set (papi-wrap_VERSION_MAJOR 1)
# set (papi-wrap_VERSION_MINOR 0)
# include_directories("${PROJECT_BINARY_DIR}")

# set(SPH_BUILD_NAME     "" CACHE STRING "SPHFlow_mockup configuration name")
# set(SPH_BUILD_NAME_DIR .  CACHE STRING "SPHFlow_mockup configuration directory")
# set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib-sph CACHE PATH "Single directory for all static libraries.")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib CACHE PATH "Single directory for all libraries.")
# set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin CACHE PATH "Single directory for all executables.")
# set(CMAKE_EXE_LINKER_FLAGS "-Wl,-rpath,\$ORIGIN/../lib:\$ORIGIN/../../lib:\$ORIGIN")
# set(CMAKE_Fortran_MODULE_DIRECTORY "${PROJECT_BINARY_DIR}/modules" CACHE PATH "Single directory for all fortran modules.")
set(CMAKE_Fortran_MODULE_DIRECTORY "${CMAKE_BINARY_DIR}/modules" CACHE PATH "Single directory for all fortran modules.")

# ----------
# Warnings:
OPTION (ENABLE_WARNINGS "Selects whether compiler warnings are enabled." FALSE)
IF (ENABLE_WARNINGS)
  SET(CMAKE_CXX_FLAGS "-Wall ${CMAKE_CXX_FLAGS}")
  SET(CMAKE_C_FLAGS "-Wall ${CMAKE_C_FLAGS}")  
ENDIF (ENABLE_WARNINGS)

# ----------
# install prefix:
#CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT is a hack and can be googled, not sure whether it is going to stay
#IF(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
# SET(CMAKE_INSTALL_PREFIX "1.0" CACHE PATH "Installation directory" FORCE)
#ENDIF(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)

#===================================
#Tests
#===================================
# OPTION (ENABLE_TESTS "Selects whether tests are built." FALSE)
# IF (ENABLE_TESTS)
#     INCLUDE (CTest)
#     ENABLE_TESTING()
#     ADD_SUBDIRECTORY(tests)
# ENDIF (ENABLE_TESTS)

include(CTest)

# does the executable run ?
add_test (cRuns c.exe)

# does it print: "Hello, world!" ?
add_test (cPrints c.exe)
set_tests_properties (cPrints PROPERTIES PASS_REGULAR_EXPRESSION "Hello, world!")

#-----------------------------------------------------------------------------
# - Compiling types availables
set(CMAKE_BUILD_TYPE_STRINGS " " "Debug" "Release" "MinSizeRel" "RelWithDebInfo" ${CMAKE_BUILD_TYPE_STRINGS_EXTRA})
# set(CMAKE_BUILD_TYPE_PREFIX_STRINGS "")
# foreach(type ${CMAKE_BUILD_TYPE_STRINGS})
#   list (APPEND CMAKE_BUILD_TYPE_PREFIX_STRINGS "_${type}" )
# endforeach()

# foreach(type "" ${CMAKE_BUILD_TYPE_PREFIX_STRINGS})
#   string(TOUPPER "${type}" type_UP)
#   set(CMAKE_Fortran_FLAGS${type_UP} "${CMAKE_Fortran_FLAGS${type_UP}} ${CMAKE_Fortran_FLAGS${type_UP}_${CMAKE_Fortran_COMPILER_ID}}")
#   message(STATUS "CMAKE_Fortran_FLAGS${type_UP}=${CMAKE_Fortran_FLAGS${type_UP}}")
# endforeach()

# # To allow the use of IN_3D macro with intel (-allow nofpp_comments ---> can replace by !):
# if(CMAKE_Fortran_COMPILER MATCHES "ifort" OR CMAKE_Fortran_COMPILER_ID MATCHES "Intel")
#   set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fpp -allow nofpp_comments")
# endif()

# Packages required
# find_package(MPI REQUIRED)
# include_directories(${MPI_Fortran_INCLUDE_PATH})

#-----------------------------------------------------------------------------
# - option
# - option_default
# - option_desc
# - option_values
# macro(add_option opt default desc)
# list(APPEND options ${opt})
# set(${opt}_DEFAULT ${default} CACHE INTERNAL "")
# set(${opt}_DESC    ${desc} CACHE INTERNAL "")
# set(${opt}_VALUES  ${ARGN} CACHE INTERNAL "")
# endmacro()


# include_directories(${CMAKE_Fortran_MODULE_DIRECTORY})
# include_directories(${SPHFlow_mockup_BINARY_DIR})


# add_library(saxpy OBJECT
#   ./src/hello_world_serial.f90
#  )
# add_library(sph_mockup $<TARGET_OBJECTS:sph_mockup_objs_f90>)

# add_executable(f.exe ./src/hello_world_serial.f90)
# add_executable(c.exe ./src/hello_world_serial.c)
# add_executable(C.exe ./src/hello_world_serial.cpp)
add_executable(f.exe ./src/hello_world_mpi.f90)
add_executable(c.exe ./src/hello_world_mpi.c)
add_executable(C.exe ./src/hello_world_mpi.cpp)
install (TARGETS c.exe DESTINATION bin)

# -DCMAKE_CXX_COMPILER=/apps/leone/UES/RH6.7_PE15.12/sandbox/easybuild/software/GCC/4.9.3-binutils-2.25/bin/g++
# -DCMAKE_C_COMPILER=/apps/leone/UES/RH6.7_PE15.12/sandbox/easybuild/software/GCC/4.9.3-binutils-2.25/bin/gcc
# -DCMAKE_Fortran_COMPILER=/apps/leone/UES/RH6.7_PE15.12/sandbox/easybuild/software/GCC/4.9.3-binutils-2.25/bin/gfortran
# -DCMAKE_INSTALL_PREFIX:PATH=

# target_link_libraries(sph-mockup ${MPI_Fortran_LIBRARIES})
