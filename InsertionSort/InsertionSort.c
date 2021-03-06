/*------------------------------------------------------------------------
- Compilation: gcc InsertionSort.c -o Insertion
- Execution: ./Insertion < test
- Read a input with integers and sort them using insertion sort algorithm
- ./Insertion < test
- 1 2 3 4 5 6
------------------------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
int* insertion(int* a){
    //the first position(index = 0) of the array is its length
    for(int i = 2; i <= a[0]; i++){
        int pivot = a[i]; //pivot stores the value to be insert
        int j;
        for(j = i-1; a[j] > pivot && j >= 1; j--){
            a[j+1] = a[j];
        }
        a[j+1] = pivot;
    }
    return a;
}
int* read_file(const char* filename){
    FILE* file = fopen(filename, "r");
    int* a = (int*)malloc(sizeof(int*));
    int i = 1;
    int n = 0;
    while(!feof(file)){
        fscanf(file, "%d", &n);
        a[i++] = n;
    }
    a[0] = (i-1);
    return a;
}
int main(int argc, char * argv[]){
    int* a = read_file(argv[1]);
    a = insertion(a);
    for(int i = 1; i <= a[0]; i++){
        printf("%d ", a[i]);
    }
    printf("\n");
    return 0;
}