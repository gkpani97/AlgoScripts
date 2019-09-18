#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

bool prime(long long n){
    int mark {1};
    int limit = (int)sqrt(n);
    if(n==2 || n==3 || n==5 || n==7)
        return true;
    else if(n==4 || n==6 || n==8 || n==9)
        return false;
    else{
        for(long long i=3; i <= limit; i+= 2){
            if(n%i==0){
                mark = 0;
                break;
        } }
        if(mark == 0)
            return false;
        else
            return true;
        }
}

int main() {
    long long m,n;
    cin>>m>>n;
    
    vector <long long> prim;
    int count = 0;
    
    if(m%2==0)
        ++m;
    
    for(int i=m; i<n+1;i+=2){
        if(prime(i))
            prim.push_back(i);
    }
    
    
    for(long long k = 2; k<prim.size();k++){
        if(prim[k]-prim[k-1]==6 || prim[k]-prim[k-2]==6)
            ++count;
    }
    
    
    
    
    cout<<count<<endl;
    return 0;
}