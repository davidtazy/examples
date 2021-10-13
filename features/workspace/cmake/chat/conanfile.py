from conans import ConanFile, CMake

class Pkg(ConanFile):
    name = "chat"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake_paths", "cmake_find_package"
    exports_sources = "src/*"
    requires = "hello/0.1@user/testing", "zlib/1.2.11"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        self.copy("*.h", src="src", dst="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
