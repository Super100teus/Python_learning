import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Binario {


public static void binario_(){
    int cont=0;
    Pattern expresion = Pattern.compile("^10([01]{2})*(01|11)$");
     String texto = "101011";
     Matcher validacion = expresion.matcher(texto);
     if(validacion.matches()){
        System.out.println("Cadena valida");
     }else{System.out.println("Cadena no valida");}
    
}//genera una expresion regular que inicie con 10 binario y acepte cualquier cadena cuya longitud sea par y su magnitud sea impar
// que es la longitud y amplitud de un automata 


    public static void main(String[] args) {
        binario_();
    }
}
