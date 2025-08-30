#include "time.h"
#include<iostream>
using namespace std;

// Default constructor
Time::Time():hour(0),minute(0),second(0){}

// Constructor with 3 parameters
Time::Time(int h, int m, int s){
    hour=h;
    minute=m;
    second=s;
}

// Copy constructor
Time::Time(const Time& p){
    hour=p.hour;
    minute=p.minute;
    second=p.second;
    }

// Set time values
void Time::setTime(int h,int m,int s){
    hour=h;
    minute=m;
    second=s;
}

// Display time in HH:MM:SS format
void Time::showTime(){
    cout<<"Current time: "
        <<(hour<10?"0":"")<<hour<<":"
        <<(minute<10?"0":"")<<minute<<":"
        <<(second<10?"0":"")<<second<<"\n\n";
}
