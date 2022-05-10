#include <stdio.h>  // file handling functions
#include <stdlib.h> // atoi
#include <string.h> // strtok
#include <math.h>

#include "egsa87.h"


void calculate(double phlam[2], FILE * fout){
    double phlam2[2];
    memcpy (phlam2, phlam, 2*1*sizeof(double));
    double xy[2];
    phlam[0]*=M_PI/180.0;
    phlam[1]*=M_PI/180.0;
    wgs84egsa87(phlam, xy);
    printf("%lf, %lf -> %lf, %lf\n", phlam2[0], phlam2[1], xy[0], xy[1]);
    fprintf(fout,"%lf, %lf\n", xy[0], xy[1]);
}



int main (int argc, const char * argv[]) {

    if (argc < 2){
        printf("Not enough parameters\n");
        printf("calculate input_file output_file\n");

    }
  
    char *ptr;
    double ret;
    double latitude;
    double longitude;

    FILE* fp = fopen(argv[1], "r");
    FILE* fout = fopen(argv[2], "w");
 
    if (!fp)
        printf("Can't open input file\n");

    if (!fout)
        printf("Can't open output file\n");
 

        // Here we have taken size of
        // array 1024 you can modify it
        char buffer[1024];
 
        int row = 0;
        int column = 0;

        while (fgets(buffer,1024, fp)) {
            column = 0;
            row++;
            // Splitting the data
            char* value = strtok(buffer, ", \r\n");
           
            latitude = 0;
            longitude = 0;
 
            while (value) {
                // Column 1
                if (column == 0) {

                  latitude = strtod(value, &ptr);
                }
 
                // Column 2
                if (column == 1) {
                   longitude = strtod(value, &ptr);
                }
 
                value = strtok(NULL, ", \r\n");
                column++;
            }
            //printf("%lf %lf\n",latitude, longitude);
            double phlam[2] = {latitude, longitude};
            calculate(phlam, fout);
        }
 
        // Close the file
        fclose(fp);
        fclose(fout);
    return 0;
}
