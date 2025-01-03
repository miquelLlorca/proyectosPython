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

class Tablero{

    private:
        vector <Punto> tablero;
        int t;

    public:

        Tablero(int t, char type){
            this->t = t;

            if(type == 'r'){
                int ns[] = {0, 0, 1};

                for(int i=0; i<t; i++){
                    for(int j=0; j<t; j++){
                        tablero.push_back(Punto(i, j, rand()%4));
                    }
                }
            }else if(type == 'l'){
                for(int i=0; i<t; i++){
                    for(int j=0; j<t; j++){
                        tablero.push_back(Punto(i, j, Punto::MURO));
                    }
                }

                for(int i=0; i<2*t; i++){
                    
                    Punto a = Punto(rand()%t, rand()%t, Punto::SUELO);
                    Punto b = Punto(0, 0, Punto::SUELO);
                    int p = rand()%2;

                    if(p){
                        b.set(0, a.getX());
                        b.set(1, rand()%t);
                    }else{
                        b.set(0, rand()%t);
                        b.set(1, a.getY());
                    }
                    cout << a << b << endl;
                    int dir = a.getX() < b.getX();
                    int x = a.getX(), y = a.getY();

                    for(int i=0; i < abs(a.getX() - b.getX()); i++){
                        for(int j=0; j<tablero.size(); j++){
                            if(tablero[j].compare(x, y)){
                                tablero[j].setValue(Punto::SUELO);
                            }
                        }
                        x++;
                    }
                    
                    dir = a.getY() < b.getY();
                    x = a.getX();
                    y = a.getY();
                    for(int i=0; i < abs(a.getY() - b.getY()); i++){
                        for(int j=0; j<tablero.size(); j++){
                            if(tablero[j].compare(x, y)){
                                tablero[j].setValue(Punto::SUELO);
                            }
                        }
                        y++;
                    }


                }


            }else{
                for(int i=0; i<t; i++){
                    for(int j=0; j<t; j++){
                        tablero.push_back(Punto(i, j, Punto::SUELO));
                    }
                }
            }
            
        }

        Punto getPoint(int x, int y){
            for(int i=0; i<tablero.size(); i++){
                if(tablero[i].compare(x, y)){
                    return tablero[i];
                }
            }
        }

        void addCourse(Punto a, Punto b){
            for(int i=0; i<tablero.size(); i++){
                if(tablero[i] == a){
                    tablero.erase(tablero.begin()+i);
                    tablero.push_back(a);
                }
            }

            for(int i=0; i<tablero.size(); i++){
                if(tablero[i] == b){
                    tablero.erase(tablero.begin()+i);
                    tablero.push_back(b);
                }
            }
        }

        vector<Punto> fill(Punto p, bool &reached){
            vector <Punto> filled;
            vector <Punto> ps = p.adj();

            for(int i=0; i<tablero.size(); i++){
                for(int j=0; j<4; j++){
                    if(tablero[i] == ps[j] && tablero[i].getValue()==Punto::SUELO){
                        tablero[i].fill();
                        filled.push_back(tablero[i]);
                    }

                    if(tablero[i] == ps[j] && tablero[i].getValue()==Punto::FINAL){
                        reached = true;
                    }
                }
            }

            return filled;
        }

        friend ostream& operator <<(ostream &os, Tablero &tab){
            
            for(unsigned i=0; i<tab.t; i++){
                for(unsigned j=0; j<tab.t; j++){
                    os << tab.getPoint(i, j).getValue();
                }
                os << '\n';
                
            }
            
            return os;
        }
        
};
