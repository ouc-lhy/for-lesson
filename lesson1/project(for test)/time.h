// Default constructor, Parameterized constructor, Copy constructor, setTime, showTime
class Time {
public:
    Time(); // Default constructor
    Time(int h, int m, int s); // Constructor with 3 parameters
    Time(const Time& t); // Copy constructor
    void setTime(int hour, int minute, int second); // Set time
    void showTime(); // Display time
private:
    int hour;
    int minute;
    int second;
};
