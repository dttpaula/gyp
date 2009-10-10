#!/usr/bin/env python

"""
"""

import TestGyp

test = TestGyp.TestGyp()

test.run_gyp('build/all.gyp', chdir='src')

test.relocate('src', 'relocate/src')

test.build_all('build/all.gyp', chdir='relocate/src')

chdir = 'relocate/src/build'

if test.format == 'xcode':
  chdir = 'relocate/src/prog1'
test.run_built_executable('prog1',
                          chdir=chdir,
                          stdout="Hello from prog1.c\n")

if test.format == 'xcode':
  chdir = 'relocate/src/prog2'
test.run_built_executable('prog2',
                          chdir=chdir,
                          stdout="Hello from prog2.c\n")

test.pass_test()
