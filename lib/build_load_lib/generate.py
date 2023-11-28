#!/usr/bin/python3 
# This script generates a bunch of dummy files what makes significant impact on build time.

import os
import shutil
import sys

def cleanUp(sourceDirs):
    for dir in sourceDirs:
        if os.path.exists(dir):
            shutil.rmtree(dir)
        os.makedirs(dir)
        
def generateHeaderFiles(filePath, functionName):
    with open(filePath, 'w') as file:
        file.write("#include <string>\n\n")
        file.write("std::string {}();\n".format(functionName))

def generateSourceFiles(filePath, functionName, complexity):
    with open(filePath, 'w') as file:
        file.write("#include <iostream>\n\n")
        file.write("std::string {}() {{\n".format(functionName))
        for _ in range(complexity):
            file.write("    for (int i = 0; i < 10000; ++i) {\n")
            file.write("        // Some complex code\n")
            file.write("    }\n")
        file.write("    std::cout << \"{} called\" << std::endl;\n".format(functionName))
        file.write("    return std::to_string({});\n".format(complexity))
        file.write("}\n")

def generateCmakeFile(sourceFiles):
    with open('LibSources.cmake', 'w') as file:
        file.write("set(LIB_SOURCES {})\n".format(" ".join(sourceFiles)))
    
def generateConsumerSrc(pathPrefix, functionNames, headerFiles):
    with open(pathPrefix + '/build_load.cpp', 'w') as file:
        file.write("#include <build_load.h>\n")
        file.write("#include <iostream>\n")
        for header in headerFiles:
            file.write("#include <{}>\n".format(header))
        file.write("\n")
        file.write("void buildLoadCall() {\n")
        for function in functionNames:
            file.write("    std::cout << {}() << std::endl;\n".format(function))
        file.write("}\n")

if __name__ == "__main__":
    filesAmount = int(sys.argv[1])
    sourcePrefix = sys.argv[2]
    sourceDir = "src"
    includeDir = "include"
    sourceFiles = []
    headerFiles = []
    functionNames = []
    headerNames = []

    # Remove sources generated before
    cleanUp({sourceDir, includeDir})

    for i in range(1, filesAmount + 1):
        sourceFiles.append("{}/lib{}.cpp".format(sourceDir, i))
        headerFiles.append("{}/lib{}.h".format(includeDir, i))
        functionNames.append("function{}".format(i))
        headerNames.append("lib{}.h".format(i))

    # Create C++ source files with varying complexities
    for i, source_file in enumerate(sourceFiles, start=1):
        generateSourceFiles(source_file, functionNames[i-1], i)

    # Create C++ header files with varying complexities
    for i, header_file in enumerate(headerFiles, start=1):
        generateHeaderFiles(header_file, functionNames[i-1])

    # Create C++ source file for calling all generated symbols
    generateConsumerSrc(sourcePrefix, functionNames, headerNames)

    # Create LibSources.cmake file
    generateCmakeFile(sourceFiles)

    print("C++ source files and LibSources.cmake generated.")