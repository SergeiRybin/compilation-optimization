#include <iostream>
#include <string>
#include <string_ops.h>
#include <build_load.h>

using namespace std;

int main()
{
    string rawString = "Hello, let's compress me!";
    unsigned char *compressedArray;

    try
    {
        size_t compressedLen = compressString(rawString, &compressedArray);

        string uncompString;
        uncompressString(compressedArray, compressedLen, uncompString);

        cout << "Raw string: " << rawString << endl;
        cout << "Compressed/Uncompressed string: " << uncompString << endl;
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }

    delete[] compressedArray;

    buildLoadCall();
    return 0;
}