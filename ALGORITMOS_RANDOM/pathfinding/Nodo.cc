#include <iostream>
#include <vector>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <unistd.h> 
#include <fstream>
#include <sstream>
#include "Punto.cc"
using namespace std;

class Nodo : public Punto{

    private:

        Vector<Punto> caminos;

    
    public:

        void calculaCaminos(Punto ini){
            
        }

        Vector<Punto> getCaminos(){

        }

};
