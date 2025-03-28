from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout
from conan import ConanFile
from conan.tools.files import copy, mkdir, save

class Consumer(ConanFile):
  name = "consumer"
  version = "0.0.0"
  settings = "os", "arch", "compiler", "build_type"
  package_type = "application"

  def requirements(self):
    self.requires("libcurl/8.4.0")

  def layout(self):
    cmake_layout(self)

  def export_sources(self):
    copy(self, "*", self.recipe_folder, self.export_sources_folder)

  def generate(self):
    tc = CMakeToolchain(self)
    tc.generate()

    deps = CMakeDeps(self)
    deps.generate()

  def build(self):
    cmake = CMake(self)
    cmake.configure(variables={
      "CMAKE_SKIP_RPATH": True
    })
    cmake.build()

