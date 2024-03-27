#include <iostream>
int main(){
	int in;
	int ans;
	std::cin>>in;
	while(in!=0){
		if(in%10==1){
			ans+=1;
		}
		in/=10;
	}
	std::cout<<ans;
	return 0;
}
