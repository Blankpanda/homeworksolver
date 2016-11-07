#include <stdio.h>

char * hello(char * what);
#include <Python.h>

char * hello(char* what) {
  printf("%s", what);
}

static PyObject * hello_wrapper(PyObject * self, PyObject * args) {
  char * input;
  char * result;
  PyObject * ret;

  if(!PyArg_ParseTuple(args, "s", &input)) {
    return NULL;
  }

  result = hello(input);

  ret = PyString_FromString(result);
  free(result);

  return ret;
}

DL_EXPORT(void) inithello(void)
{
  Py_InitModule("hello", HelloMethods);
}

