#include <iostream>
using namespace std;

int main() {
    int x;  // создал переменную
    cout << "Введите число" << endl;
    cin >> x;  // вписал в нее значение

    if (x > 0) {  // если значение больше 0
        cout << "Это число больше 0" << endl;  // написать это
    } else {  // в любом другом случае
        cout << "Это число меньше 0" << endl;  // написать это
    }
    return 0;
}
