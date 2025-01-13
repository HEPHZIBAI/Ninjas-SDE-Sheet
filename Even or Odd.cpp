/*
Problem statement
Write a program that uses bitwise AND operator to check if a given positive integer is even or odd.

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1<=N<=10^4
*/

#include<iostream>
using namespace std;

int main() {
	int n;
	cin>>n;
	if(!(n&1))
		cout<<"Even";
	else
		cout<<"Odd";
}
