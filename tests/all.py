#!/usr/bin/env python
#
# Copyright 2019 Rickard Armiento
#
# This file is part of a Python candidate reference implementation of
# the optimade API [https://www.optimade.org/]
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import unittest

import test_python_version
import test_parser
import test_optimade
import test_serve_example_sqlite3
import test_serve_example_mongodb
import test_serve_example_wsgi
import test_serve_example_django

suite = unittest.TestLoader().loadTestsFromTestCase(test_python_version.TestPythonVer)

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_parser.TestParserExamples))

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_optimade.TestOptimadeExamples))

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_serve_example_sqlite3.TestServeExampleSqlite3))

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_serve_example_mongodb.TestServeExampleMongoDB))

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_serve_example_wsgi.TestServeExampleWSGI))

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_serve_example_django.TestServeExampleDjango))

unittest.TextTestRunner(verbosity=2).run(suite)

    
