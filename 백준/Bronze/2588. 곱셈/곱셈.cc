#include <iostream>
#include<string>
using namespace std;

int main() {
	int num1, num2;
	cin >> num1 >> num2;

	int hun =  num2 / 100 ; // 백의 자리
	int ten = (num2 % 100) /10 ; //십의 자리
	int num =  (num2 % 100) % 10; //일의 자리

	cout << num1 * num << endl;
	cout << num1 * ten << endl;
	cout << num1 * hun << endl;
	cout << num1 * num2 << endl;
	

	return 0 ;
}