// #include <stdio.h>
#include <miniz.h>
#include <string_ops.h>
#include <stdexcept>

using namespace std;

size_t compressString(const string &str, unsigned char **pCmp)
{
    int cmp_status;
    uLong cmpLen = compressBound(str.size());
    auto p = new unsigned char[cmpLen]{0};
    *pCmp = p;

    // Compress the string.
    cmp_status = compress(*pCmp, &cmpLen, reinterpret_cast<const unsigned char *>(str.c_str()), str.size());
    if (cmp_status != Z_OK)
    {
        throw runtime_error("Compression failed");
    }

    return cmpLen;
}

void uncompressString(const unsigned char *pCmp, size_t cmpLen, string &out)
{
    int cmp_status;

    if (!pCmp || !cmpLen)
    {
        throw runtime_error("Wrong byte buffer is passed to uncompression function");
    }

    size_t uncompLen = deflateBound(mz_streamp{}, cmpLen);
    unsigned char *pUncomp = new unsigned char[uncompLen]{0};

    cmp_status = uncompress(pUncomp, &uncompLen, pCmp, cmpLen);

    if (cmp_status != Z_OK)
    {
        throw runtime_error("Uncompression failed");
    }

    out.assign(reinterpret_cast<char *>(pUncomp));
    delete[] pUncomp;
}