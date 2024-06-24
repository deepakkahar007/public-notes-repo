#include <iostream>
#include "person.cpp"
#include <string>
using namespace std;






int main(){

  
    




    return 0;
}


/*  function:-

int add(int num1, int num2){
    int num3 = num1 + num2;
    return num3;
}
*/

/*  main program:-

int c = add(23,27);
cout << "added value \n" << add(25,25)<<endl;

string name;
cout << "enter your name\n"<<endl;
cin >> name;
cout << " \n"<< name<<endl;
string fullname;
cout << "enter your full name"<<endl;
getline(cin,fullname);
cout << "the full name is"<<fullname<<endl;

boolean and boolaplha:-
bool red(true);
bool green(false);
cout << boolalpha;

if(red==true){
    cout << "the light is red"<<endl;
}else{
    cout << "the light is green"<<endl;
}

type casting:-
char a='a';
cout << " "<<static_cast<int>(a)<<endl;

Auto keyword:-
auto v1{23};
auto v2{'e'};
cout<< " "<< sizeof(v1)<<endl;
cout<< " "<< sizeof(v2)<<endl;

// pointer:-
int a{20};
int *p{&a};
int b{30};
int *p1{nullptr};
p1=&b;
cout << " "<< p<<endl;
cout << " "<< *p<<endl;
cout << " "<< p1<< endl;
cout << " "<< *p1<< endl;

//use array and pointer, change the value of string:-
const char *str{"hello"};
cout << " "<< str<<endl;
char a[] {"hello"};
cout<< " "<< a<<endl;
a[0]='a';
cout<< " "<< a<<endl;

//dynamic memory allocation:-
int *p{nullptr};
p=new int();    allocatng memory
cout<< " the dynamic memory "<<endl;
*p=35;  //assigning value
cout << " "<<*p<<endl;
delete p;   //releasing memory
cout << " "<<*p<<endl;
cout << " "<<p<<endl;

// reseting the pointer variable :-
p=nullptr;
p=new int();    //resusing the same variable after resting it
*p=50;
cout<<"the first assign value is : "<<*p<<endl;
delete p;

//refernce variable:-
int ab{50};
char cd{'d'};
int &ba{ab};
char &dc{cd};
cout<< " "<<&ba<<endl;
cout<< " "<<&dc<<endl;
cout<< " "<<ab<<endl;
cout<< " "<<cd<<endl;
ba=300;
dc='e';
cout <<"==============="<<endl;
cout<< " "<<&ba<<endl;
cout<< " "<<&dc<<endl;
cout<< " "<<ab<<endl;
cout<< " "<<cd<<endl;

//const variable:-
int a{50};
const int &b{a};    //const refernce variable
cout<<""<<a<<endl;
cout<<""<<b<<endl;
cout<<""<<&b<<endl;

//lambda function with name:-
 auto func=[](){
     cout<<" hello world"<<endl;
 };
 func();

//annonymous lambda function with no name:-
 [](){
     cout<<"hello world"<<endl;
 }();
 cout<<"done"<<endl;

//a lambda function with parameters
[](int a,int b){
    cout<<"a+b: "<<a+b<<endl;
 }(45,5);

//to call it multiple tumes:-
auto func=[](int a,int b){
    cout<<"a+b:- "<<a+b<<endl;
};
func(23,45);
func(34,56);

//lambda function with returning value using variable:-
auto result=[](auto a,auto b){
    return a+b;
};
auto a=result(56,4);

cout<<" "<<a<<endl;
cout<<" "<<result(60,49)<<endl;

//using lambda's own return type:-
auto func=[](auto a,auto b)->int{
return a+b;
};
cout<<" "<<func(25,25)<<endl;
cout<<" "<<sizeof(func(23,27))<<endl;

//using capture list to access out of scope variables:-
int a{10},b{29};
auto func=[a,b]()->int{
return a+b;
};
int fun=func();
cout<<" "<<fun<<endl;

//using referncing we can change the value of lambda function adn outer variable as well
int c{50};
auto func=[&c](){
    cout<<"the inner value "<<c<<endl;
};
for (size_t i = 0; i < 5; i++)
{
    cout<<"outer value "<<c<<endl;
    func();
    ++c;
}

//using referncing to access all the elemnets
int a{10},b{20};
auto func=[&](){
    cout<<" "<<a+b<<endl;
};
for (size_t i = 0; i < 5; i++)
{
    a++,b++;
    func();
}

//template sunction:-
template <typename T>
T maxi(T a, T b) {
    return (a > b) ? a : b; }

template <typename A>
A multi(A a,A b) {
    return a*b; }
int main() {
    int c = multi(3, 6);
    cout << "" << c << endl;
    string hello = ("hello", "power comes with responbility");
    int c = maxi(23, 34);
    char d{maxi('B', 'Z')};
    cout << " " << c << endl;
    cout << " " << d << endl;
    cout << " " << hello << endl;
    cout << " " << sizeof(hello) << endl;
    int a{50},b{60};
    int *pt1{&a},*pt2{&b};
    cout<<" "<<maxi(a,b)<<endl;
    cout<<" "<<&pt1<<endl;
    cout<<" "<<&pt2<<endl;
    cout<<" "<<*maxi(pt1,pt2)<<endl;
    return 0; }

    













*/