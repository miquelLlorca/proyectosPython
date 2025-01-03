#include <iostream>
#include <vector>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <unistd.h> 
#include <fstream>
#include <sstream>

using namespace std;

class Punto{

    private:
        int x;
        int y;
        char v;
        char type;

    
    public:

        static const char INICIO = 'I';
        static const char FINAL = 'F';
        static const char MURO = 'X';
        static const char SUELO = '_';
        static const char FILLED = 'o';


        Punto(int x, int y, char v){
            this->x = x;
            this->y = y;
            this->v = v;
            if(v == 0) this->v = MURO;
            if(v==1 || v==2 || v==3) this->v = SUELO;
        }

        int getX(){
            return x;
        }

        int getY(){
            return y;
        }

        void set(int pos, int v){
            if(pos==0) this->x=v;
            if(pos==1) this->y=v;
        }

        void setValue(char v){
            this->v = v;
        }

        
        int compare(int x, int y){
            return this->x == x && this->y == y;
        }

        char getValue(){
            return this->v;
        }

        void fill(){
            this->v = FILLED;
        }

        vector<Punto> adj(){
            vector<Punto> pAdj = {Punto( 0,  1, 'a'), 
                          Punto( 0, -1, 'a'),
                          Punto( 1,  0, 'a'),
                          Punto(-1,  0, 'a')};

            for(int i=0; i<4; i++){
                pAdj[i] += *this;
            }
            return pAdj;
        }

        friend ostream& operator <<(ostream &os, Punto &p){
            
            os << '(' << p.x << ',' << p.y << ") -> " << p.v;
            
            return os;
        }

        Punto& operator+=(const Punto& other){
            this->x += other.x;
            this->y += other.y;
            return *this;
        }

        bool operator==(const Punto& other){
            return this->x == other.x && this->y == other.y;
        }


};
