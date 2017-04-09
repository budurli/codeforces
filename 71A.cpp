#include <iostream>
#include <string>

#define MAX 100

int main()
{
    int n = 0;
    std::string str = "";
    std::string result[MAX];
    std::cin >> n;
    for (int i = 0; i < n; ++i)
    {
        std::cin >> str;
        if (str.length() > 10)
            result[i] = str.front() + std::to_string(str.length()-2) + str.back();
        else
            result[i] = str;
    }

    for (int i = 0; i < n; ++i)
    {
        std::cout << result[i] << std::endl;
    }
    return 0;
}