# Step 1 - System Configuration

* Install cmake on system
* Clone git repository of pybind11 into your project

# Step 2 - Create Files

* Create C/C++ files with code and Python module info as in this example
* Create CMakeLists.txt into your project as in this example
* Create python file as client code into your project

# Step 3 - Build the C/C++ code as python Module

Run the following commands

* mkdir build
* cd build
* cmake ..
* make

Now you may use *.so C/C++ dynamically linked library (dll) as package / module in your python code

# Step 4 - Execute the Python Code

* Undefined reference from Pycharm can be muted with comment "# noqa"
* Run the python code and see the results
