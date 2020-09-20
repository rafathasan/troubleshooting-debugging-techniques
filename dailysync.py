#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
import os
src = "/home/student-04-46008fc61844/data/prod/"
dest = "/home/student-04-46008fc61844/data/prod_backup/"


def run(path):
	subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
	paths = []

	for root, dirs, files in os.walk(src, topdown=False):
	    for name in files:
	        paths.append([os.path.join(root, name), os.path.join(dest, name)])

	p=Pool(len(paths))
	p.map(run, paths)
