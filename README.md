# WGS84 to EGSA87 CSV Converter

This is a fork of egsa87 project that can be used to convert a CSV from WGS84 to EGSA87 (ΕΓΣΑ87)

## Build

```
$ make
```

## Use

```
$ ./calculate input_file.csv output_file.csv
```

##  File Format

The input_file.csv must have the following format:

name, latitude, longitude

-----------------------

# Google MyMaps to CSV

Export as CSV the points from Google MyMaps. Only the Latitude and Longitude which is associated with the point and the point name will be maintained.


```
python google_mymaps_2_egsa87.py inputfromgoogle.csv 
```

The inputfromgoogle.csv must have the following format:

```
WKT,name,.....
"POINT (25.533135 37.145893 0.0)",pointname,....
```


-----------------------

# Google MyMaps to EGSA87

Export as CSV the points from Google MyMaps. Only the Latitude and Longitude which is associated with the point and the point name will be maintained.

```
python google_mymaps_2_egsa87.py inputfromgoogle.csv  google_mymaps_egsa87_output.csv
```

```
WKT,name,.....
"POINT (25.533135 37.145893 0.0)",pointname,....
```

The output will have the following format:

```
name, 25.533135, 37.145893, 1827965.198315, 2890138.776154
```

-----------------------
# egsa87 to GML
Transforms exported points of simple EGSA CSV of format 'name lat lon egsa_lat egsa_lon' to GML polygon for ktimatologio.gr. The input should have the following format:

```
PART A	25.528307	37.150476	635570.480603	4112370.610919
PART B	25.528242	37.150388	635564.865287	4112360.754550
PART C	25.528437	37.150448	635582.075885	4112367.690413
PART D	25.528068	37.150260	635549.641196	4112346.304348
PART E	25.527863	37.150203	635531.537070	4112339.687090
PART F	25.527877	37.150340	635532.535584	4112354.906899
PART G	25.527888	37.150434	635533.344508	4112365.351683
PART H	25.528021	37.150444	635545.138296	4112366.651416
PART I	25.528107	37.150362	635552.922469	4112357.676770
```

To execute:

```
python egsa87_2_GML.py test.xml test.gml 
```

The output:

```
		<?xml version="1.0" encoding="UTF-8"?>
		<gml:FeatureCollection xmlns:gml="http://www.opengis.net/gml" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:fme="http://www.safe.com/gml/fme" xsi:schemaLocation="http://www.safe.com/gml/fme test.xsd">
		<gml:boundedBy>
		<gml:Envelope srsName="EPSG:2100" srsDimension="2">
		<gml:lowerCorner>635531.537070 4112339.687090</gml:lowerCorner>
		<gml:upperCorner>635582.075885 4112370.610919</gml:upperCorner>
		</gml:Envelope>
		</gml:boundedBy>
		<gml:featureMember>
		<gml:surfaceProperty>
		<gml:Surface srsName="EPSG:2100" srsDimension="2">
		<gml:patches>
		<gml:PolygonPatch>
		<gml:exterior>
		<gml:LinearRing>
		<gml:posList>635570.480603 4112370.610919 635564.865287 4112360.754550 635582.075885 4112367.690413 635549.641196 4112346.304348 635531.537070 4112339.687090 635532.535584 4112354.906899 635533.344508 4112365.351683 635545.138296 4112366.651416 635552.922469 4112357.676770 635570.480603 4112370.610919</gml:posList>
		</gml:LinearRing>
		</gml:exterior>
		</gml:PolygonPatch>
		</gml:patches>
		</gml:Surface>
		</gml:surfaceProperty>
		</gml:featureMember>
		</gml:FeatureCollection>
```

-----------------------
# egsa87
Functions to convert geodetic coordinates from the [World Geodetic System](https://en.wikipedia.org/wiki/World_Geodetic_System) 1984 (**WGS84**) to the [Hellenic Geodetic Reference System 1987](https://en.wikipedia.org/wiki/Hellenic_Geodetic_Reference_System_1987) (**HGRS87/EGSA87**) Greek geodetic system and vice versa.

The root directory contains Matlab implementations; C ports of the same functions are in directory ./C

Code is based on the [icoordstrans](https://github.com/skozan/icoordstrans) library.
For an overview of spatial referencing, see [this.](https://unstats.un.org/Unsd/geoinfo/UNGEGN/docs/_data_ICAcourses/_HtmlModules/_Documents/D06/documents/D06-03_KnippersPPTeaching.pdf)
-----------------------

There is also a sidecar utility to transform Google mymaps points into simple CSV.


## Disclaimer
Use these conversion functions at your own risk. No warranties are made regarding the accuracy and reliability of the provided code. 

## License
GPL

### Funding
_Development has received funding from the European Union’s Horizon 2020 Research and Innovation program under grant agreement No 826506 -- [sustAGE](https://www.sustage.eu/)._
