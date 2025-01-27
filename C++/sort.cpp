#include <iostream>
#include <vector>
using namespace std;

class SortingAlgorithms {
public:
    // O(n^2) - Repeatedly swap adjacent elements if they are in wrong order
    void bubbleSort(vector<int>& arr) {
        int n = arr.size();
        for(int i = 0; i < n-1; i++)
            for(int j = 0; j < n-i-1; j++)
                if(arr[j] > arr[j+1])
                    swap(arr[j], arr[j+1]);
    }

    // O(n^2) - Find minimum element and place it at the beginning
    void selectionSort(vector<int>& arr) {
        int n = arr.size();
        for(int i = 0; i < n-1; i++) {
            int min_idx = i;
            for(int j = i+1; j < n; j++)
                if(arr[j] < arr[min_idx])
                    min_idx = j;
            swap(arr[min_idx], arr[i]);
        }
    }

    // O(n^2) - Build sorted array one element at a time
    void insertionSort(vector<int>& arr) {
        int n = arr.size();
        for(int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;
            while(j >= 0 && arr[j] > key) {
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = key;
        }
    }

    // O(n log n) - Divide array into two halves, sort them and merge
    void mergeSort(vector<int>& arr) {
        if(arr.size() <= 1) return;
        
        int mid = arr.size() / 2;
        vector<int> left(arr.begin(), arr.begin() + mid);
        vector<int> right(arr.begin() + mid, arr.end());
        
        mergeSort(left);
        mergeSort(right);
        merge(arr, left, right);
    }

    // O(n log n) - Build heap tree and repeatedly extract maximum element
    void heapSort(vector<int>& arr) {
        int n = arr.size();
        for(int i = n/2-1; i >= 0; i--)
            heapify(arr, n, i);
        
        for(int i = n-1; i > 0; i--) {
            swap(arr[0], arr[i]);
            heapify(arr, i, 0);
        }
    }

    // O(d * (n + k)) where d is number of digits and k is range - Sort by processing each digit
    void radixSort(vector<int>& arr) {
        int max = getMax(arr);
        for(int exp = 1; max/exp > 0; exp *= 10)
            countSort(arr, exp);
    }

private:
    void merge(vector<int>& arr, vector<int>& left, vector<int>& right) {
        int i = 0, j = 0, k = 0;
        while(i < left.size() && j < right.size()) {
            if(left[i] <= right[j])
                arr[k++] = left[i++];
            else
                arr[k++] = right[j++];
        }
        while(i < left.size()) arr[k++] = left[i++];
        while(j < right.size()) arr[k++] = right[j++];
    }

    void heapify(vector<int>& arr, int n, int i) {
        int largest = i;
        int left = 2*i + 1;
        int right = 2*i + 2;

        if(left < n && arr[left] > arr[largest])
            largest = left;
        if(right < n && arr[right] > arr[largest])
            largest = right;

        if(largest != i) {
            swap(arr[i], arr[largest]);
            heapify(arr, n, largest);
        }
    }

    int getMax(vector<int>& arr) {
        int max = arr[0];
        for(int i = 1; i < arr.size(); i++)
            if(arr[i] > max)
                max = arr[i];
        return max;
    }

    void countSort(vector<int>& arr, int exp) {
        vector<int> output(arr.size());
        vector<int> count(10, 0);

        for(int i = 0; i < arr.size(); i++)
            count[(arr[i]/exp)%10]++;

        for(int i = 1; i < 10; i++)
            count[i] += count[i-1];

        for(int i = arr.size()-1; i >= 0; i--) {
            output[count[(arr[i]/exp)%10]-1] = arr[i];
            count[(arr[i]/exp)%10]--;
        }

        for(int i = 0; i < arr.size(); i++)
            arr[i] = output[i];
    }
};

int main() {
    vector<vector<int>> test_cases = {
        {64, 34, 25, 12, 22, 11, 90},
        {1, 200, 3, 4, 0, 10, 15, 20},
        {5, 5, 5, 5, 5},
        {1, 4, 2, 4, 5, 6, 3, 2},
        {30, 20, 10}
    };
    
    SortingAlgorithms sorter;
    
    // Test all sorting algorithms
    for(auto test_arr : test_cases) {
        cout << "\nOriginal array: ";
        for(int num : test_arr) cout << num << " ";
        cout << endl;
        
        // Bubble Sort
        vector<int> arr1 = test_arr;
        sorter.bubbleSort(arr1);
        cout << "Bubble Sort  : ";
        for(int num : arr1) cout << num << " ";
        cout << endl;
        
        // Selection Sort
        vector<int> arr2 = test_arr;
        sorter.selectionSort(arr2);
        cout << "Selection Sort: ";
        for(int num : arr2) cout << num << " ";
        cout << endl;
        
        // Insertion Sort
        vector<int> arr3 = test_arr;
        sorter.insertionSort(arr3);
        cout << "Insertion Sort: ";
        for(int num : arr3) cout << num << " ";
        cout << endl;
        
        // Merge Sort
        vector<int> arr4 = test_arr;
        sorter.mergeSort(arr4);
        cout << "Merge Sort   : ";
        for(int num : arr4) cout << num << " ";
        cout << endl;
        
        // Heap Sort
        vector<int> arr5 = test_arr;
        sorter.heapSort(arr5);
        cout << "Heap Sort    : ";
        for(int num : arr5) cout << num << " ";
        cout << endl;
        
        // Radix Sort
        vector<int> arr6 = test_arr;
        sorter.radixSort(arr6);
        cout << "Radix Sort   : ";
        for(int num : arr6) cout << num << " ";
        cout << endl;
        
        cout << "----------------------------------------" << endl;
    }
    
    return 0;
}