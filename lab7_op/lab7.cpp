#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <ctime>
using namespace std;

const int n = 10;
int arr[n];
void input_arr(int*);
void output_arr(int*);
int aver(int[]);

int main() {	
	input_arr(arr);
	cout << "C(n): "; output_arr(arr);
	printf("Average of negatives is: %2d\n", aver(arr));
	cout << "F(n): ";
	for (int x = 1; x < n; x += 2) {
		cout << arr[x] * aver(arr) << " ";
	}
	cout << "\n";
	system("pause");
}

void input_arr(int* p) {
	srand(time(NULL));
	for (int i = 0; i < n; i++) {
		*p = rand() % 20 - 10;
		p++;
	}
}

void output_arr(int* p) {
	for (int i = 0; i < n; i++) {
		printf("%3d", *(p + i));
	}
	printf("\n");
}

int aver(int arr[]) {
	int s = 0, sum = 0, count = 0;
	for (int i = 0; i < n; i++) {
		if (arr[i] < 0) {
			sum += arr[i];
			count += 1;
		}
	}
	return (float)sum / count;
}