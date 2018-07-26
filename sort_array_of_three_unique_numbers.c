#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define SWAP(x,y) int t;t=x;x=y;y=t;

static inline void print_array(int *arr, int size){
    int i;
    printf("\n-----------------------\n");
    for(i = 0; i < size; i++){
        printf(" %6d",*(arr+i));
    }
    printf("\n-----------------------\n");
}

int get_second_largest_element(int *a, int size){
    int first, second;
    int i;

    first = second = INT_MIN;
    for(i = 1; i < size; i++){
        if(a[i] > first){
            second = first;
            first = a[i];
        }
        else if(a[i] > second && a[i] != first){
            second = a[i];
        }
    }

    return second;
}

void sort_array_of_three_unique_numbers(int *a, int size){
    int i,j,k,mid;

    i = j = 0;
    k = size - 1;
    mid = get_second_largest_element(a,size);

    while(j <= k){
        if(a[j] < mid){
            SWAP(a[i],a[j]);
            i++,j++;
        }
        else if (a[j] > mid){
            SWAP(a[j],a[k]);
            k--;
        }
        else{
            j++;
        }
    }
}

int main(int argc, char **argv){
    int n, i;
    int *arr;

    if(argc < 4){
        printf("\n [Error] Text entered: ");
        for(i = 0; i < argc; i++){
            printf("%s ",argv[i]);
        }
        printf("\n \n Expected text: %s <size of array> <int 1> <int 2> ... <int n>",argv[0]);
        return -1;
    }

    n = atoi(argv[1]);
    if(n < 3){
        printf("[Error] Array size should be greater than 3 as it should contain three unique integers.");
        return -1;
    }

    arr = (int* ) malloc(sizeof(int) * n);
    for(i = 0; i < n; i++){
        *(arr+i) = atoi(argv[i + 2]);
    }

    //print_array(arr,n);

    sort_array_of_three_unique_numbers(arr, n);
    print_array(arr,n);

    return 0;
}