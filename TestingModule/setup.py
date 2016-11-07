from distutils.core import setup, Extension

extension_mod = Extension("hello", ["hellomodule.c", 'hello.'])
