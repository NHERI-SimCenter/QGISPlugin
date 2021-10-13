//===-- Intel_SVML.td - Defines SVML call variants ---------*- tablegen -*-===//
//
//                     The LLVM Compiler Infrastructure
//
// This file is distributed under the University of Illinois Open Source
// License. See LICENSE.TXT for details.
//
//===----------------------------------------------------------------------===//
//
// This file is used by TableGen to define the different typs of SVML function
// variants used with -fveclib=SVML.
//
//===----------------------------------------------------------------------===//

class SvmlVariant;

def sin        : SvmlVariant;
def cos        : SvmlVariant;
def pow        : SvmlVariant;
def exp        : SvmlVariant;
def log        : SvmlVariant;
def acos       : SvmlVariant;
def acosh      : SvmlVariant;
def asin       : SvmlVariant;
def asinh      : SvmlVariant;
def atan2      : SvmlVariant;
def atan       : SvmlVariant;
def atanh      : SvmlVariant;
def cbrt       : SvmlVariant;
def cdfnorm    : SvmlVariant;
def cdfnorminv : SvmlVariant;
def cosd       : SvmlVariant;
def cosh       : SvmlVariant;
def erf        : SvmlVariant;
def erfc       : SvmlVariant;
def erfcinv    : SvmlVariant;
def erfinv     : SvmlVariant;
def exp10      : SvmlVariant;
def exp2       : SvmlVariant;
def expm1      : SvmlVariant;
def hypot      : SvmlVariant;
def invsqrt    : SvmlVariant;
def log10      : SvmlVariant;
def log1p      : SvmlVariant;
def log2       : SvmlVariant;
def sind       : SvmlVariant;
def sinh       : SvmlVariant;
def sqrt       : SvmlVariant;
def tan        : SvmlVariant;
def tanh       : SvmlVariant;

// TODO: SVML does not currently provide _ha and _ep variants of these fucnctions.
// We should call the default variant of these functions in all cases instead.

// def nearbyint  : SvmlVariant;
// def logb       : SvmlVariant;
// def floor      : SvmlVariant;
// def fmod       : SvmlVariant;
// def ceil       : SvmlVariant;
// def trunc      : SvmlVariant;
// def rint       : SvmlVariant;
// def round      : SvmlVariant;
