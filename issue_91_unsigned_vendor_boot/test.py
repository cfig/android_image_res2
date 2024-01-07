#!/usr/bin/env python3

import shutil, os, os.path, subprocess, unittest, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../../.."))
from integrationTest import *

if sys.platform == "win32":
    gradleWrapper = "gradlew.bat"
    shellRun = True
else:
    gradleWrapper = "./gradlew"
    shellRun = False

def vendor_boot_with_dtc():
    log.info("test_case: vendor_boot_with_dtc()")
    cleanUp()
    decompressXZ("src/integrationTest/resources_2/issue_91_unsigned_vendor_boot/vendor_boot.img.xz", "vendor_boot.img")
    subprocess.check_call(gradleWrapper + " unpack", shell = True)
    subprocess.check_call(gradleWrapper + " pack", shell = True)
    unittest.TestCase().assertEqual("05113ad1dfeb0d7a7111ed114e4b64c8", hashFile("vendor_boot.img"))
    unittest.TestCase().assertEqual("05113ad1dfeb0d7a7111ed114e4b64c8", hashFile("vendor_boot.img.clear"))
    subprocess.check_call(gradleWrapper + " clear", shell = True)
    cleanUp()
    log.info("test_case: vendor_boot_with_dtc() success")

def vendor_boot_without_dtc():
    log.info("test_case: vendor_boot_without_dtc()")
    cleanUp()
    decompressXZ("src/integrationTest/resources_2/issue_91_unsigned_vendor_boot/vendor_boot.img.xz", "vendor_boot.img")
    subprocess.check_call(gradleWrapper + " unpack", shell = True)
    os.remove("build/unzip_boot/dtb.0.dts")
    subprocess.check_call(gradleWrapper + " pack", shell = True)
    unittest.TestCase().assertEqual("05113ad1dfeb0d7a7111ed114e4b64c8", hashFile("vendor_boot.img"))
    unittest.TestCase().assertEqual("05113ad1dfeb0d7a7111ed114e4b64c8", hashFile("vendor_boot.img.clear"))
    subprocess.check_call(gradleWrapper + " clear", shell = True)
    cleanUp()
    log.info("test_case: vendor_boot_without_dtc() success")

if __name__ == "__main__":
    vendor_boot_with_dtc()
    vendor_boot_without_dtc()
