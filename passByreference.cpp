
//pass by reference is not availabe in c


#include<iostream>
using namespace std;

void fun(int &x, int &y){
    int temp ;
    temp = x;
    x = y;
    y = temp;
}

int main(){
    int a = 5 , b = 10;
    fun(a,b);
    cout<<"a = "<<a<<endl;
    cout<<"b = "<<b;
    return 0;
}
