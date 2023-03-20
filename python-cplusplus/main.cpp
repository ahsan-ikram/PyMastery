#include <iostream>
#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <chrono>
#include <thread>

namespace py = pybind11;

// Complex processing which is designed to run in C/C++ Code for performance reasons
float processInC(float arg1, float arg2) {
  return arg1 + arg2;
}

class CClass {
  float multiplier;
public:
  CClass(float multiplier_) : multiplier(multiplier_) {};

  float multiply(float input) {
    return multiplier * input;
  }

  std::vector<float> multiply_list(std::vector<float> items) {
    for (auto i = 0; i < items.size(); i++) {
      items[i] = multiply(items.at(i));
    }
    return items;
  }

  std::vector<std::vector<uint8_t>> make_image() {
    auto out = std::vector<std::vector<uint8_t>>();
    for (auto i = 0; i < 128; i++) {
      out.push_back(std::vector<uint8_t>(64));
    }
    for (auto i = 0; i < 30; i++) {
      for (auto j = 0; j < 30; j++) { out[i][j] = 255; }
    }
    return out;
  }

  void set_mult(float val) {
    multiplier = val;
  }

  float get_mult() {
    return multiplier;
  }

// Handing Python GIL in C/C++ (Parallelize)
  void function_that_takes_a_while() {
    py::gil_scoped_release release;
    std::cout << "starting" << std::endl;
    // Some abstract complex processing
    std::this_thread::sleep_for(std::chrono::milliseconds(2000));
    std::cout << "ended" << std::endl;

    // py::gil_scoped_acquire acquire;
    // auto list = py::list();
    // list.append(1);
  }
};

// Factor function to provide CClass instance
CClass getCClass(float multiplier) {
  return CClass(multiplier);
}

/*

Code segment defines what python module exposes

*/
PYBIND11_MODULE(module_name, module_handle) {
  // Python module docstring
  module_handle.doc() = "Python module doc string is defined in C code";
  // Python module defining the function written in C/C++
  module_handle.def("process_in_c", &processInC);
  // Python module defining the factory function written in C/C++
  module_handle.def("get_c_class", &getCClass);
  // Python module defining the class (with constructors) written in C/C++
  py::class_<CClass>(
			module_handle, "PyCClass"
			).def(py::init<float>())
    .def_property("multiplier", &CClass::get_mult, &CClass::set_mult)
    .def("multiply", &CClass::multiply)
    .def("multiply_list", &CClass::multiply_list)
    .def_property_readonly("image", [](CClass &self) {
				      py::array out = py::cast(self.make_image());
				      return out;
				    })
    .def("multiply_two", [](CClass &self, float one, float two) {
			   return py::make_tuple(self.multiply(one), self.multiply(two));
			 })
    .def("function_that_takes_a_while", &CClass::function_that_takes_a_while)
    ;
}