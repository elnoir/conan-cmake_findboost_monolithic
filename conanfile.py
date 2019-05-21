from conans import ConanFile, CMake, tools


class CmakefindboostmonolithicConan(ConanFile):
    name = "CMake_FindBoost_Monolithic"
    version = "1.0"
    license = "MIT"
    author = "Ede Bittner bittner.ede@gmail.com"
    url = "https://github.com/elnoir/conan-cmake_findboost_monolithic/issues"
    description = "Custom find boost for the "
    topics = ("cmake", "conan", "boost")
    settings = None
    exports_sources = "cmake/FindBoost.cmake"
    exports = "LICENSE.md"

    def package(self):
        self.copy("*.cmake", keep_path=False)
