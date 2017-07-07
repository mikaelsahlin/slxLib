#!/usr/bin/env python3
import zipfile
import sys


the_file = sys.argv[1]
the_path = sys.argv[2]
	
zip_ref = zipfile.ZipFile(the_file, 'r')
zip_ref.extractall(the_path)
zip_ref.close()
