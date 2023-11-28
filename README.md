# Shapr3D home assignment
## Abstract
This is a home assignment for Shapr3D company. The main goal of this assignment is to demostrate compilation time optimization techiques as well as production-like CMake environment. The project consists of a custom library and a main application source files that consumes the library symbols.
## Custom library
The custom library contains two major parts:
1. BuildLoadLib provides sufficient amount of symbols that have signficant impact on the build time. All source files are generated out of `generate.py` python script.
2. Miniz wrapper library. There is a simple wrapper provideing `compress` and `uncompress` functions working over std::string objects.
Both parts of the Custom Library are used for demonstration purposes only.

## Build
### Prerequisites
Python >= 3.8.10
Clang >= 10.0.0
CMake >= 3.16
Ccache >= 3.7.7

------------

Run `./build_init.sh` to initialize the repository. It generates source files for BuildLoadLib and configures CMake root project.
Run `./build.exec.sh` to execute the build for the main app and all dependencies.
### Tweaks
Open `build_init.sh` and find the following CMake options:
`SUPPRESS_ECOMMA` - Turns `comma` errors to warnings.
`CCACHE_ENABLE` - Enables ccache
`PCH_ENABLE` - Enables precompiled headers usage

### Compilation improvements
As long as the custom code used in the compilation optimization is pretty primitive, the most efficient techniques are used: precompiled headers and ccache.
There is a comparative table for build time corresponding clean build for
- All features disabled
- Precompiled headers enabled only
- Precompiled headers and ccache enabled both
All measurements are in seconds and they were done on a BuildLoadLib which exposes 100 symbols. Main source of measurements is Linux `time` utility. More detailed build profiling may be done using `ClangBuildAnalyzer` utility. This may have a sense in complex projects. You may enable profiling files generation adding `-DBUILD_PROF=ON` key to `build_init.sh` script.
Note: number of exported symbols may be changed in `build_init.sh` script.

| Original  | PCH  | PCH & CCACHE  |
| :------------: | :------------: | :------------: |
|  13.5 | 5.7  | 2.5 |

### Compilation flags
As the industry standard for production code the following warning detection flags were used: `-Wpedantic -Wall -Wextra -Werror`
Additionally, as requested, the `-Wcomma` flag was used. In the meantime as Miniz code generates a number of comma usage errors, the `-Wno-error=comma` suppression flag is optionally introduced and managed by the user.
In order to improve the code speed `-O3` optimization flag was used.