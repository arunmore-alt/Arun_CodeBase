#include <iostream>
using namespace std;

class Student
{
private:
    string name;
    int age;
    float marks;

public:
    // Default constructor
    Student()
    {
        name = "Unknown";
        age = 0;
        marks = 0.0;
    }

    // Parameterized constructor
    Student(string n, int a, float m)
    {
        name = n;
        age = a;
        marks = m;
    }

    // Setter methods
    void setName(string n)
    {
        name = n;
    }

    void setAge(int a)
    {
        age = a;
    }

    void setMarks(float m)
    {
        marks = m;
    }

    // Getter methods
    string getName()
    {
        return name;
    }

    int getAge()
    {
        return age;
    }

    float getMarks()
    {
        return marks;
    }

    // Normal Method
    void displayInfo()
    {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Marks: " << marks << endl;
    }
};


int main()
{
    // Using parameterized constructor
    Student s1("Neha", 20, 88.5);
    s1.displayInfo();

    cout << endl;
    

    // Using default constructor + setters
    Student s2;
    s2.setName("Arun");
    s2.setAge(22);
    s2.setMarks(92.0);

    s2.displayInfo();

    return 0;
}
