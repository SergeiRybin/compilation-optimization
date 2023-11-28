import os
import shutil
import sys

def clean_up(source_dirs):
    for dir in source_dirs:
        if os.path.exists(dir):
            shutil.rmtree(dir)
        os.makedirs(dir)
        
def generate_h_file(file_path, function_name):
    with open(file_path, 'w') as file:
        file.write("#include <string>\n\n")
        file.write("std::string {}();\n".format(function_name))

def generate_cpp_file(file_path, function_name, complexity):
    with open(file_path, 'w') as file:
        file.write("#include <iostream>\n\n")
        file.write("std::string {}() {{\n".format(function_name))
        for _ in range(complexity):
            file.write("    for (int i = 0; i < 10000; ++i) {\n")
            file.write("        // Some complex code\n")
            file.write("    }\n")
        file.write("    std::cout << \"{} called\" << std::endl;\n".format(function_name))
        file.write("    return std::to_string({});\n".format(complexity))
        file.write("}\n")

def generate_cmake_file(source_files):
    with open('LibSources.cmake', 'w') as file:
        file.write("set(LIB_SOURCES {})\n".format(" ".join(source_files)))
    
def generate_caller_file(fpath_prefix, function_names, header_files):
    with open(fpath_prefix + '/build_load.cpp', 'w') as file:
        file.write("#include <build_load.h>\n")
        file.write("#include <iostream>\n")
        for header in header_files:
            file.write("#include <{}>\n".format(header))
        file.write("\n")
        file.write("void buildLoadCall() {\n")
        for function in function_names:
            file.write("    std::cout << {}() << std::endl;\n".format(function))
        file.write("}\n")

if __name__ == "__main__":
    amount = int(sys.argv[1])
    source_prefix = sys.argv[2]
    source_dir = "src"
    inc_dir = "include"
    source_files = []
    header_files = []
    function_names = []
    header_names = []

    clean_up({source_dir, inc_dir})

    for i in range(1, amount):
        source_files.append("{}/lib{}.cpp".format(source_dir, i))
        header_files.append("{}/lib{}.h".format(inc_dir, i))
        function_names.append("function{}".format(i))
        header_names.append("lib{}.h".format(i))

    # Create C++ source files with varying complexities
    for i, source_file in enumerate(source_files, start=1):
        generate_cpp_file(source_file, function_names[i-1], i)

    # Create C++ header files with varying complexities
    for i, header_file in enumerate(header_files, start=1):
        generate_h_file(header_file, function_names[i-1])

    # Create C++ source file for calling all generated symbols
    generate_caller_file(source_prefix, function_names, header_names)

    # Create LibSources.cmake file
    generate_cmake_file(source_files)

    print("C++ source files and LibSources.cmake generated.")