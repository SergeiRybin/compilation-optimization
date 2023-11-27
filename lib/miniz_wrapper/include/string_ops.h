#pragma once
#include <string>

std::size_t compressString(const std::string &str, unsigned char **pCmp);
void uncompressString(const unsigned char *pCmp, std::size_t cmpLen, std::string &out);