import csv
import sys


if len(sys.argv) < 2:
	print("Transforms exported points from Google mymaps to simple CSV in form 'name, Lat, Lon'")
	print("Please provide file name")

else:
	matchstr = '"POINT ('
	with open(sys.argv[1]) as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:

			if row[0][:len(matchstr)] == matchstr:
				cleaned = row[0].replace(matchstr,"").replace(' 0.0)"',"").replace(')"',"").replace(" ",", ")
				print(row[1] + ", "+cleaned)
