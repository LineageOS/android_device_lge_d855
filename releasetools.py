# Copyright (C) 2009 The Android Open Source Project
# Copyright (c) 2011, The Linux Foundation. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import binascii
import common
import hashlib
import re

lg_magic = "41a9e467744d1d1ba429f2ecea655279"

def bumped(boot_img):
  data = binascii.hexlify(boot_img[-1024:])
  return data.endswith(lg_magic) or data.startswith(lg_magic)

def bump(boot_img):
  magic = binascii.unhexlify(lg_magic)
  boot_img += magic
  return boot_img

def FullOTA_Assertions(info):
  AddBasebandAssertion(info)
  return

def IncrementalOTA_Assertions(info):
  AddBasebandAssertion(info)
  return

def AddBasebandAssertion(info):
  android_info = info.input_zip.read("OTA/android-info.txt")
  m = re.search(r'require\s+version-baseband\s*=\s*(\S+)', android_info)
  if m:
    versions = m.group(1).split('|')
    if len(versions) and '*' not in versions:
      cmd = 'assert(g3.verify_baseband(' + ','.join(['"%s"' % baseband for baseband in versions]) + ') == "1");'
      info.script.AppendExtra(cmd)
  return

def FullOTA_InstallEnd(info):
  try:
    boot_img = info.input_zip.read("IMAGES/boot.img")
    if not bumped(boot_img):
      common.ZipWriteStr(info.output_zip, "boot.img", bump(boot_img))
  except KeyError:
    print "No boot.img found in target_files"
  else:
    print "done"
  return
