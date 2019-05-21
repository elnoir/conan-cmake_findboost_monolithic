# conan-cmake_findboost_monolithic
This package contains a FindBoost.cmake to wrap the conans boost package ( boost/1.69.0@conan/stable ) distributed in conan-center. The original FindBoost distributed with CMake does not work with the conan pacakage when you try to crosscompile with it to Android.

# Workaround
The cmake script works the following way:
 - sets the include / library dirs based on the variables provided by conan
 - adds imported target for header only and diagnostic target
 - parse the CONAN_LIBS_BOOST variable for boost components and creating Boost::< component>  target

# Notes
When using this script, use the conan_basic_setup(TARGETS), because the generated Boost::< component >-s will depend on the CONAN_Pkg::boost target.
