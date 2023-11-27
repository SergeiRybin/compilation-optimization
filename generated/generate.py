import os
import shutil

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

def generate_cmake_file(library_name, source_files):
    with open('LibSources.cmake', 'w') as file:
        file.write("set(LIB_SOURCES {})\n".format(" ".join(source_files)))

if __name__ == "__main__":
    clean_up({"src", "include"})
    library_name = "MyDummyLibrary"
    source_files = ["src/lib{}.cpp".format(i) for i in range(1, 100)]
    header_files = ["include/lib{}.h".format(i) for i in range(1, 100)]

    # Create C++ source files with varying complexities
    for i, source_file in enumerate(source_files, start=1):
        generate_cpp_file(source_file, "function{}".format(i), i)

    for i, header_file in enumerate(header_files, start=1):
        generate_h_file(header_file, "function{}".format(i))

    # Create CMakeLists.txt file
    generate_cmake_file(library_name, source_files)

    print("C++ source files and CMakeLists.txt generated.")