#include <iostream>
#include <cmath>

using namespace std;

float func(float a){
return pow(a,3)-a-1;
}

int main()
{
float a,b,root,e;
    a=1;
    b=2;

    while(1){
    if(func(a)*func(b)<0)
    break;
    else{
      a=b;
        b++;
        }
       }
int c=0;
root = (a+b)/2;
e = abs(a-b);
cout<<"a:"<<a<<",b:"<<b<<"\nX"<<c++<<": "<<root<<endl;

for(;;){
    cout<<endl;
if(e<=.0001){
        break;
    }
    else if((func(a)>0 && func(root)>0) || (func(a)<0 && func(root)<0)){
    a = root;
cout<<"update a:"<<a<<" b: "<<b<<endl;
    e = abs(a-b);
cout<<"Error =" <<e<<endl;
    }
    else{
        b = root;
        cout<<"a: "<<a<<" update b: "<<b<<endl;
        e = abs(a-b);
        cout<<"Error =" <<e<<endl;
    }
    root = (a+b)/2;

    cout<<"X"<<c++<<": "<<root<<endl;
    }

cout<<"\nRoot = "<<root<<endl;

return 0;
}
