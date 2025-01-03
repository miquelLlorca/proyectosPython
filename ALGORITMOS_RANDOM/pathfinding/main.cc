#include<iostream>
#include <vector>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <unistd.h> 
#include <fstream>
#include <time.h>
#include <sstream>
#include "Tablero.cc"


using namespace std;


bool reachable(int n){

    Tablero t = Tablero(n, 'r');

    bool stop = true;

    Punto a = Punto(0, 0, Punto::INICIO);
    Punto b = Punto(0, 0, Punto::INICIO);

    do{
        a = Punto( rand()%t, rand()%t, Punto::INICIO);
        
        for(Punto p : a.adj()){
            if(p.getValue() == Punto::SUELO){
                stop = true;
            }
        }
    }while(!stop);

    stop = true;
    do{
        b = Punto( rand()%t, rand()%t, Punto::FINAL);
        
        for(Punto p : b.adj()){
            if(p.getValue() == Punto::SUELO){
                stop = true;
            }
        }
    }while(!stop);


    t.addCourse(a, b);
    cout << t << endl;
    
    bool reached = false;
    vector <Punto> newPs = t.fill(a, reached);
    vector <Punto> aux;

    while(!(newPs.empty() || reached)){
        

        ofstream fOut;
        fOut.open("tablero.txt");

        fOut << t;

        fOut.close();



        usleep(500000);

        for(Punto p: newPs){
            for(Punto p2: t.fill(p, reached)){
                aux.push_back(p2);
            }
        }

        newPs.clear();

        for(Punto p: aux){
            newPs.push_back(p);
        }
        
        aux.clear();

        //cout << t << endl;
    }

    return reached;
}




void pathfind(int t){
    
    Tablero t = Tablero(n, 'l');

    Punto a = Punto(0, 0, Punto::INICIO);
    Punto b = Punto(0, 0, Punto::INICIO);

    Vector<Punto> 

    
}


// ---------------------------------------------- MAIN -----------------------------------------------------
int main(int argc, char *argv[]){

    srand(time(NULL));

    int t=0;
    cout << "Tamaño: ";
    cin >> t;

    if(fork()){
        
        ofstream fOut;
        fOut.open("tablero.txt");
        fOut.close();
        execlp("python3", "python3", "./graficos.py", to_string(t).c_str(), NULL);

    }else{
        sleep(5);
        pathfind(t);
    }

    return 0;
}
