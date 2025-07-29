# libcxn 

Various utilities for mathematical and scientific computing.

**License:** GPLv3

**Author:** Buğra Coşkun
https://github.com/j0shxn

**Disclaimer**
This library is provided as-is, without warranty. Use at your own risk. Not all
functions are guaranteed to be production-grade; review code before deployment
in critical systems.

## Usage

Import and use any module or function as needed. For example:

    from libcxn.math.symbolic import symbolic

    k = [1, 0, 0]
    ang = 3.1415 / 2
    R = symbolic.rodri(k, ang)
    print(R)

All modules and functions are documented—see the API documentation section below.

## Project Structure

libcxn/
  math/
    numeric/
      numeric.py
    symbolic/
      symbolic.py

    Add new modules to the appropriate subpackage as your codebase grows.

