from conans import ConanFile, CMake, tools


class CmakefindboostmonolithicConan(ConanFile):
    name = "CMake_FindBoost_Monolithic"
    version = "0.1"
    license = "MIT"
    author = "Ede Bittner bittner.ede@gmail.com"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "Custom find boost for the "
    topics = ("cmake", "conan", "boost")
    settings = None
    exports_sources = "cmake/FindBoost.cmake"

    def package(self):
        self.copy("*.cmake", keep_path=False)
