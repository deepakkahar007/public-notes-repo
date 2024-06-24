# C++ Notes

1. [preprocessors in c++](#preprocessor-in-c++)

# preprocessor in c++

```c++
#include<iostream>  //preprocessor for c++ header file
int main()
{
using namespace std;    // defing the standard library which will be used
cout << "hello"<<endl;
int a{10}, b=20;   //define variable
int c =a+b;
cout <<"added value\n"<<c<<endl;
return 0;
}
```

# functions in c++

the function must be define before main function or it will throw a error that "function was not declared in this scope".
for eg:-

```c++
int add(int num1, int num2){
int num3=num1+num2;
return num3;
}
int main(){
    int a= add(25,25);
    cout << "added value is =" << a<< endl;
    cout << "added value is ="<<add(25,25)<<endl;   //another way to call function
}
```

# Stream Manipulator:

cout =( this is used to print something in terminal)  
cin =( this is use to take input from terminal)  
cerr =(this is use to print error)
clog =( this is use for log the output)

to take input with spaces in string use getline()
getline(cin,fullname); //to use this function make sure add #include<string>

signed and unsigned variable:-
the signed variable can store positive and negative value, but the unsigned variable only store positive value.
signed a{300};
signed b{-300};

unsigned variable
unsigned a{200};
unsigned b{-200}; //it will throw a compile time error

boolean variable store either ture or false it will contain 1 byte in memory.
we can change their value using boolaplha for eg:-
cout << boolalpha;

# Type Casting

```c++
char a='a';
// to type cast use
cout << " "<< static_cast<int>(a) <<endl;
```

# Auto Keyword

this keyword is use to let compiler decide what kind of data type it is, it will automatically detect the value and assign the data type :-

```c++
auto a{20};
auto b{'e'};
auto c{10.5};
```

# Pointers

the pointer are the variable which store the address of another variable with same data type.

```c++
int a{10};
int *a1{nullptr};   //the nullptr is use to store zero in pointer variables.
a1=&a;
to access the address use :-
cout << " "<< a1 <<endl;
to access the valueusing pointer variable:-
cout << " "<< *a1 <<endl;

you can change the value of variable using pointer :-
char *str='d';   int *str=34;

you can use char type array to store value and point it to first value of an array using:-
const char *str{"hello"};   //but this is a const variable and its value can not be change in entire programe.

to change the value of array using pointer use:-
char a[] {"hello"};
char[0]='a';
cout << " "<< a<<endl;

```

# dynamic memory allocation in heap

the dynamic allocation is use to assign the memory to the programe in heap and stack. to allocate memory use new keyword with needed data type:-

```c++
int *p {nullptr};
p=new int ();
p=35;
cout <<" value of p is : "<<p<<endl;
delete p;   to release memory use delete keyword.
```

we can use single pointer multiple times using reset the pointer:-
to reset the pointer use after the delete option:-
delete p;
p=nullptr;
