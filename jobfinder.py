# !/usr/bin/python

path = "/Volumes/LaCie/Ingest/"
# path = "/Volumes/nickpiegari/Desktop/dv concatenation test/"

import os, csv, ffmpeg

videoformats = ["dv"]

with open("videolist.csv", "w") as csvfile:
	rofl = csv.writer(csvfile)
	rofl.writerow(["filename", "filesize", "job", "status", "convertdate"])
	for root, dirs, files in os.walk(path, topdown=False):
		for name in files:
			filepath = os.path.join(root, name)
			filesize = os.path.getsize(filepath)

			try:
				if name.rsplit(".")[1] in videoformats and filepath.find(".Spotlight") == -1 and filepath.find(".Trashes") == -1:
					rofl.writerow([filepath.replace(path, ""), filesize, "transcode", "pending", ""])
					print (filepath)
			except IndexError:
				pass
			# rofl.writerow([filepath, filesize])
		# for name in dirs:
			# print(os.path.join(root, name))
   
			

	  
