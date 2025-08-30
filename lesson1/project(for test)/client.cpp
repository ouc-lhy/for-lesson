#include <iostream>
#include "time.h"
using namespace std;

// General input function
int getInput(int minVal, int maxVal) {
    int value;
    int state=0;
    while(!state){
        cin>>value;
        if(cin.fail()){ // Check if input failed (not an integer)
            cin.clear(); // Clear error flag
            cin.ignore(100,'\n'); // Ignore invalid input in buffer
            cout<<"Invalid input, please try again:"<<endl;
        }
        else if(value<minVal||value>maxVal){ // Check range
            cout<<"Input out of range, please try again:"<<endl;
        }
        else{
            cin.ignore(100,'\n');
            state=1; // Valid input, exit loop
        }
    }
    return value;
}

int main() {
    // Create objects using different constructors
    cout<<"you will initialize t1,t2,t3_1 by three ways,finally stored in object array and output by two ways\n\n";
    Time t1; // Use default constructor
    cout<<"the object t1 has been initialized by using default constructor\nt1 ";
    t1.showTime();
    cout<<"initialize t2 by using constructor with 3 parameters"<<endl;
    cout<<"Enter hour (0-23): ";
    int hour2=getInput(0,23);
    cout<<"Enter minute (0-59): ";
    int minute2=getInput(0,59);
    cout<<"Enter second (0-59): ";
    int second2=getInput(0,59);
    Time t2(hour2,minute2,second2); // Use constructor with 3 parameters
    cout<<"t2 ";
    t2.showTime();

    Time t3_1(t2); // Use copy constructor
    Time t3_2=t2;//initialized by assigning it the value of another object
    cout<<"the object t3_1 has been initialized by copying t2\nt3_1 ";
    t3_1.showTime();
    cout<<"the object t3_1 has been initialized by copying t2 value\nt3_2 ";
    t3_2.showTime();
    cout<<"initialize t4 by using 'new' and then delete"<<endl;
    cout<<"Enter hour (0-23): ";
    int hour=getInput(0,23);
    cout<<"Enter minute (0-59): ";
    int minute=getInput(0,59);
    cout<<"Enter second (0-59): ";
    int second=getInput(0,59);
    // Create and delete object using new and delete operators
    Time* t4=new Time(hour,minute,second);
    cout<<"t4 ";
    t4->showTime();


    // Create object array and traverse
    Time arr[5]={t1,t2,t3_1,t3_2,*t4};
    // Traverse using array index
    cout << "Traversing the array of Time objects using array index:" << endl;
    for(int i=0;i<5;++i){
        cout<<"t"<<i<<" ";
        arr[i].showTime();
    }
    // Traverse using object pointer
    cout << "Traversing the array of Time objects using pointers:" << endl;
    Time* pArr=arr;
    for(int i=0;i<5;++i){
        cout<<"t"<<i<<" ";
        pArr->showTime();
        pArr++;
    }
    delete t4;
    cout<<"the object t4 has been deleted\n\n";
    return 0;
}
