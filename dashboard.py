#include <iostream>
#include <cstdlib>

using namespace std;

class Candle
{
protected:
    double height;
    string color;

public:
    Candle();
 Candle(double h, string c);

    
    void data_output();
    void update_height(double hours);
};

Candle::Candle() : height(0.0), color("undefined")
{
}

Candle::Candle(double h, string c) : height(h), color(c)
{
}

void Candle::data_output()
{
    cout << "Candle data:" << endl;
    cout << "Height: " << height << " cm" << endl;
    cout << "Color: " << color << endl;
}


void Candle::update_height(double hours)
{
    double loss;

    loss = hours * 1.5;          
    height = height - loss;

    if(height <= 0)
    {
        height = 0;
        cout << "The candle has burned down completely." << endl;
    }
    else
    {
        cout << "Current height of the candle: " << height << " cm" << endl;
    }
}

int main()
{
    
    Candle *candle1 = new Candle(20.0, "red");
    Candle *candle2 = new Candle(15.0, "white");

   
    candle2->data_output();

    cout << endl;

    
    candle1->update_height(5);

    
    delete candle1;
    delete candle2;

    system("pause");
    return 0;
}