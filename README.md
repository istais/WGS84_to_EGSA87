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
