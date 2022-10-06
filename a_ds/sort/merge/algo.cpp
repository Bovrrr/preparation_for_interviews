#include <iostream>

using namespace std;

void array_fill_from_terminal(float *arr, size_t arr_size) {
  for (size_t i = 0; i < arr_size; ++i) {
    cin >> arr[i];
  }
}

void print_array(float *arr, size_t arr_size) {
  for (size_t i = 0; i < arr_size; ++i) {
    cout << arr[i] << " ";
  }
  cout << endl;
}

float *merge(float *arr_left, size_t arr_left_size, float *arr_right,
             size_t arr_right_size) {
  size_t size = arr_left_size + arr_right_size;
  float *arr = new float[size];

  size_t i = 0, j = 0;
  while (i < arr_left_size or j < arr_right_size) {
    if (arr_left[i] < arr_right[j]) {
      arr[i + j] = arr_left[i];
      ++i;
    } else {
      arr[i + j] = arr_right[j];
      ++j;
    }
  }
  while (i < arr_left_size) {
    arr[i + j] = arr_left[i];
    ++i;
  }
  while (j < arr_right_size) {
    arr[i + j] = arr_right[j];
    ++j;
  }

  return arr;
}

float *sort(float *arr, size_t size) {
  if (1 == size) {
    return arr;
  }
  size_t l = 0;
  size_t r = size;
  size_t m = (l + r) / 2;
  return merge(arr, m - l + 1, &(arr[m]), r - m);
}

int main() {
  size_t arr_size;
  cin >> arr_size;
  float *array = new float[arr_size];
  array_fill_from_terminal(array, arr_size);
  print_array(array, arr_size);

  float *arr_sorted = sort(array, arr_size);
  print_array(arr_sorted, arr_size);

  return 0;
}