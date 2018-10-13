#include <iostream>
#include <cstdint>

// https://www.learncpp.com/cpp-tutorial/24a-fixed-width-integers/
 
int main()
{
    std::cout << "bool:\t\t" << sizeof(bool) << " bytes" << std::endl;
    std::cout << "char:\t\t" << sizeof(char) << " bytes" << std::endl;
    std::cout << "wchar_t:\t" << sizeof(wchar_t) << " bytes" << std::endl;
    std::cout << "char16_t:\t" << sizeof(char16_t) << " bytes" << std::endl; // C++11, may not be supported by your compiler
    std::cout << "char32_t:\t" << sizeof(char32_t) << " bytes" << std::endl; // C++11, may not be supported by your compiler
    std::cout << "short:\t\t" << sizeof(short) << " bytes" << std::endl;
    std::cout << "int:\t\t" << sizeof(int) << " bytes" << std::endl;
    std::cout << "long:\t\t" << sizeof(long) << " bytes" << std::endl;
    std::cout << "long long:\t" << sizeof(long long) << " bytes" << std::endl; // C++11, may not be supported by your compiler
    std::cout << "float:\t\t" << sizeof(float) << " bytes" << std::endl;
    std::cout << "double:\t\t" << sizeof(double) << " bytes" << std::endl;
    std::cout << "long double:\t" << sizeof(long double) << " bytes" << std::endl;

// dom:
// bool:    1 bytes
// char:    1 bytes
// wchar_t:  4 bytes
// char16_t:  2 bytes
// char32_t:  4 bytes
// short:    2 bytes
// int:    4 bytes
// long:    8 bytes
// long long:  8 bytes
// float:    4 bytes
// double:    8 bytes
// long double:  16 bytes

    std::cout << "\nint8_t  :\t\t" << sizeof(int8_t) << " bytes" << std::endl;
    std::cout << "uint8_t :\t\t" << sizeof(uint8_t) << " bytes" << std::endl;
    std::cout << "int16_t :\t\t" << sizeof(int16_t) << " bytes" << std::endl;
    std::cout << "uint16_t:\t\t" << sizeof(uint16_t) << " bytes" << std::endl;
    std::cout << "int32_t :\t\t" << sizeof(int32_t) << " bytes" << std::endl;
    std::cout << "uint32_t:\t\t" << sizeof(uint32_t) << " bytes" << std::endl;
    std::cout << "int64_t :\t\t" << sizeof(int64_t) << " bytes" << std::endl;
    std::cout << "uint64_t:\t\t" << sizeof(uint64_t) << " bytes" << std::endl;

// dom:
// int8_t  :    1 bytes
// uint8_t :    1 bytes
// int16_t :    2 bytes
// uint16_t:    2 bytes
// int32_t :    4 bytes
// uint32_t:    4 bytes
// int64_t :    8 bytes
// uint64_t:    8 bytes

    return 0;
}


