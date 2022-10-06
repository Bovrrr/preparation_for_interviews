#include <iostream>
#include <vector>

using namespace std;

void get_array(size_t n)
{
    vector<float> arr(n);
    for (size_t i = 0; i < n; ++i)
    {
        cin >> arr[i];
    }
};

void swap(float &a, float &b)
{
    float temp = a;
    a = b;
    b = temp;
}

vector<float> sort(vector<float> arr)
{
    vector<float> arr_sorted = arr;
    for (size_t k = 1; k < arr_sorted.size(); ++k)
    {
        for (size_t j = k; j > 0; --j)
        {
            if (arr_sorted[j] < arr_sorted[j - 1])
            {
                swap(arr_sorted[j - 1], arr_sorted[j]);
            }
        }
    }
}

int main()
{
    return 0;
}