#!/usr/bin/env python
#
# Shorted out version of test.py to test authentication only.
#
# Copyright (c) 2011 anatanokeitai.com(sakurai_youhei)
# 
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
# 
# The Software shall be used for *YOUNGER* than you, not *OLDER*.
# 
 
import sys
import unittest
from cStringIO import StringIO
import time
import xml.dom.minidom

import pyacd
pyacd.debug_level=2

if len(sys.argv)!=3:
  sys.stderr.write("usage: ./test.py email password")
  sys.exit(2)

email=sys.argv[1]
password=sys.argv[2]

print "*** Inputs are here ***"
print "email:",email
print "password:",password
print "*"*20
print ""

session=None

class AuthTest(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def testLogin(self):
    global session
    session=pyacd.login(email,password)
    self.assertTrue(session.is_logged_in(),"not logined %s"%session)
    self.assertNotEqual(session.username,None,"username is None %s"%session)
    self.assertNotEqual(session.customer_id,None,"customer_id is None %s"%session)

def main():
  suites=[]
  
  suites.append(unittest.TestLoader().loadTestsFromTestCase(AuthTest))

  runner = unittest.TextTestRunner(verbosity=2)

  for s in suites:
    runner.run(s)

if __name__=="__main__":
  main()
