#include <iostream>
#include <vector>
 
int main()
{
    const int n = 4;
#ifdef __GNUC__
#ifdef __GNUC_MINOR__
    std::cout << "g++/" << __GNUC__ << "." << __GNUC_MINOR__ << "\n";
#endif
#endif
    std::vector<int> clist;
    // comment out to create corefile:
    clist.resize(n);
    for (size_t i = 0; i < n; i++)
        clist[i] = i;
    for(int nn : clist) {
        std::cout << clist[nn] << '\n';
    }
/*
    // Create a vector containing integers
    std::vector<int> v = {7, 5, 16, 8};
    // Add two more integers to vector
    v.push_back(25);
    v.push_back(13);
    // Iterate and print values of vector
    for(int n : v) {
        std::cout << n << '\n';
    }
*/
}
