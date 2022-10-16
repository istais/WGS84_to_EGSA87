import csv
import sys
import os
from decimal import Decimal

if len(sys.argv) < 2:
	print("Transforms exported points of simple EGSA CSV of format 'name lat lon egsa_lat egsa_lon' to GML polygon for ktimatologio.gr")
	print("Example:")
	print("./egsa87_2_GML.py google_mymaps_egsa87_output.csv google_mymaps_egsa87_output.gml")
else:

	polygon = ""
	upper_a = 0
	upper_b = 0
	lower_a = 999999999999999
	lower_b = 999999999999999
	first_a = 0
	first_b = 0
	original_stdout = sys.stdout
	with open(sys.argv[2], 'w') as f: 
		sys.stdout = f # Change the standard output to the file we created.
		with open(sys.argv[1]) as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
			for row in spamreader:
				polygon = polygon +row[3]+" "+row[4]+ " "
				if Decimal(row[3]) > Decimal(upper_a):
					upper_a = row[3]
				if Decimal(row[3]) < Decimal(lower_a):
					lower_a = row[3]
				if Decimal(row[4]) > Decimal(upper_b):
					upper_b = row[4]
				if Decimal(row[4]) < Decimal(lower_b):
					lower_b = row[4]
				if first_a == 0:
					first_a = row[3]
					first_b = row[4]
			polygon = polygon +first_a+" "+first_b
			print """
		<?xml version="1.0" encoding="UTF-8"?>
		<gml:FeatureCollection xmlns:gml="http://www.opengis.net/gml" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:fme="http://www.safe.com/gml/fme" xsi:schemaLocation="http://www.safe.com/gml/fme mesogeion.xsd">
		<gml:boundedBy>
		<gml:Envelope srsName="EPSG:2100" srsDimension="2">
		<gml:lowerCorner>"""+lower_a+""" """+lower_b+"""</gml:lowerCorner>
		<gml:upperCorner>"""+upper_a+""" """+upper_b+"""</gml:upperCorner>
		</gml:Envelope>
		</gml:boundedBy>
		<gml:featureMember>
		<gml:surfaceProperty>
		<gml:Surface srsName="EPSG:2100" srsDimension="2">
		<gml:patches>
		<gml:PolygonPatch>
		<gml:exterior>
		<gml:LinearRing>
		<gml:posList>"""+polygon+"""</gml:posList>
		</gml:LinearRing>
		</gml:exterior>
		</gml:PolygonPatch>
		</gml:patches>
		</gml:Surface>
		</gml:surfaceProperty>
		</gml:featureMember>
		</gml:FeatureCollection>
			"""
		sys.stdout = original_stdout

				
