#include<bits/stdc++.h>
using namespace std;

bool binary(int a[],int target, int len){
    int start = 0;
    int end = len-1;
    while (start<=end){
        int mid = int((start+end)/2);
        if (a[mid]==target){
            return true;
        }
        else if (a[mid]<target){
            start = mid+1;
        }
        else{
            end = mid-1;
        }
    }
    return false;
}
int main(){
    int s, target;
    bool ans;
    cout<<"enter the size - ";
    cin>>s;
    int a[s];
    cout<<"\nEnter the elements - \n";
    for (int i=0;i<s;i++){
        cin>>a[i];
    }
    int len = sizeof(a)/sizeof(a[0]);
    sort(a,a+len);
    cout<<"Enter the element to search - ";
    cin>>target;
    ans = binary(a,target,len);
    cout<<ans;
    return 0;

}