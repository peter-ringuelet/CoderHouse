from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request):
    return HttpResponse("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<br>Segunda vista!")

       4
     /    \
    2      7
   / \    /  \
  1   3   6   9

public int procesar (int k){
    int result = 0;

    if(this.esHoja) return ((k==0) ? 1 : 0);
    else{
        
        if(!(this.tieneHI() && this.tieneHD())) k--;
        if (this.tieneHI())
            result += this.getHI().procesar(k);
        if (this.tieneHD())
            result += this.getHD().procesar(k);
    }
}

public class ProcesadorDeArbol{
        ArbolBinario<intiger> arbol;
        public Resultado procesar(){
            Resultado aux = new Resultado();
            Resultado resultado = new Resultado();

            if(arbol.tieneHI){
                aux = arbol.getHI().procesar();
                resultado.actualizarDatos(aux.getLista(), aux.getContador());
            }
            if(arbol.tieneHD){
                aux = arbol.getHD().procesar();
                resultado.actualizarDatos(aux.getLista(), aux.getContador());
            }
            if ((arbol.getDato() % 2) == 1){
                if (arbol.tieneHD() || arbol.rieneHI()){
                    resultado.getLista().agregarFinal(arbol.getDato());
                }
                resultado.aumentarContador();
            }
            return resultado;
        }
}