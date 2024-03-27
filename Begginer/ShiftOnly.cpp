#include<iostream>
using namespace std;

int main(){
	int sum=0;
	int N;
	cin>>N;
	for (int i=0;i<N;i++){
		int num;
		cin>>num;
		sum+=num;
	}
	int i=0;
	while(sum%2!=0){
		sum/=2;
		i+=1;
	}
	cout<<i;
	return 0;
}
