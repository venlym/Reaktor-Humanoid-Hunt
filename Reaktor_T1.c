#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int binaryToDecimal(char *byte); 

int main(void)
{
    FILE *stream = fopen("Reaktor_T1_data","r");

    printf("The password is: ");

    for(int channel = 0; channel < 14; channel++)
    {
        int len = 40*8; // length of binary string
        char line[len+1]; 
        fscanf(stream, "%s\n", line);
        line[len] = '\0';
        // printf("%s\n",line);

        int byteIndex = 0;
        unsigned int firstValidFound = 0;
        unsigned int done = 0;

        do {
            char byte[9];
            strncpy(byte, line + (byteIndex * 8), 8);
            byte[8] = '\0';

            int dec = binaryToDecimal(byte);
            // printf("%d ", dec);

            if(dec < len/8) { // valid index 0 to 39
                firstValidFound = 1;
                byteIndex = dec;
            } else {
                if(firstValidFound == 1) {
                    printf("%c", dec);
                    done = 1;
                } else byteIndex++;
            }
        } while(done == 0);
    }

    printf("\n");
    
    fclose(stream);

    return 0;
};

int binaryToDecimal(char *byte)
{
    int sum = 0;
    for(int i = 0; i < 8; i++){
        // char to decimal: (int) '0' == 48, (int) '1' == 49
        sum += ((int) byte[i] - 48) * pow(2,7-i);
    }

    return sum;
};