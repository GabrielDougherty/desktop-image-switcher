#!/usr/bin/env python

import argparse
import subprocess
parser = argparse.ArgumentParser(description='Generate a release')
parser.add_argument('version', metavar='version', type=str, nargs=1,
                    help='version for the release')
args = parser.parse_args()
print('args.version: ', args.version)

version_str = args.version[0]
if len(version_str) < 2 or version_str[0] != 'v':
    raise RuntimeError('Specify a version of the form vX.X.X i.e. v0.0.1')

src_dirname = 'desktop-image-switcher'
dest_zip = src_dirname + '-' + version_str + '.zip'

# -X is to avoid adding .DS_Store to the zip file
subprocess.Popen(['zip', '-r', dest_zip, src_dirname, '-X'])
