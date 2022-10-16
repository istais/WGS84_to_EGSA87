import csv
import sys
import os
if len(sys.argv) < 2:
	print("Transforms exported points from Google mymaps to simple CSV in form 'name, Lat, Lon'")
	print("Example:")
	print("./google_mymaps_2_egsa87.py inputfromgoogle.csv google_mymaps_egsa87_output.csv")
else:

	original_stdout = sys.stdout
	with open('google_mymaps_output.csv', 'w') as f:
		sys.stdout = f # Change the standard output to the file we created.
		matchstr = '"POINT ('
		with open(sys.argv[1]) as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
			for row in spamreader:

				if row[0][:len(matchstr)] == matchstr:
					cleaned = row[0].replace(matchstr,"").replace(' 0.0)"',"").replace(')"',"").replace(" ",", ")
					print(row[1] + ", "+cleaned)
	sys.stdout = original_stdout
	os.system("./calculate google_mymaps_output.csv "+sys.argv[2])
	os.system("rm google_mymaps_output.csv")
	os.system("sort "+sys.argv[2]+" -o "+sys.argv[2])
