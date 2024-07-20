import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.InputMismatchException;
import java.util.Scanner;
import java.util.regex.*;

public class Regex_Practica {
  
  public static void Pattern_matches(){
    String content = ""; /**/ String patternString = ".*tutorial.*"; 
    Scanner leer1 = new Scanner(System.in);
    System.out.println("La expresion regular que evaluara a la cadena es: "+patternString);
    System.out.println("Escribe la cadena a evaluar");
    content = leer1.nextLine();
    String patternString2 = ".*ebs.*";
    boolean isMatch = Pattern.matches(patternString, content);
    System.out.println("El texto contiene 'tutorial'? " + isMatch);
  }
  

  public static void Pattern_compile(){
    String cadena = ""; String patternString = ".*tuToRiAl.*";
     Scanner leer1 = new Scanner(System.in);
    System.out.println("La expresion regular que evaluara a la cadena es: "+patternString);
    System.out.println("Escribe la cadena a evaluar");
    cadena = leer1.nextLine();
    Pattern patron = Pattern.compile(patternString); // Pattern patron = Pattern.compile(patternString, Pattern.CASE_INSENSITIVE); insensible a mayusculas o minusculas
    Matcher matcher = patron.matcher(cadena);
    if(matcher.matches()){
System.out.println("Si se encuetra la cadena");
    }else{
System.out.println("No se encuetra la cadena");
    }
  }


  private static void checkMatch(){
    String text = "13444";
     Pattern pattern = Pattern.compile("\\d*");
      Scanner leer1 = new Scanner(System.in);
    System.out.println("La expresion regular que evaluara a la cadena es: "+pattern);
    System.out.println("Escribe la cadena a evaluar");
    text = leer1.nextLine();
    Matcher matcher = pattern.matcher(text);
    System.out.println(matcher.matches());//retorna false por que si bien una parte coincide la cadena 
    //completa no
}


  public static void Pattern_split(){
String cad = "sdfjrtyhsrt";
String separador="";
 Scanner leer1 = new Scanner(System.in);
    System.out.println("Escribe la cadena a evaluar");
    cad = leer1.nextLine();
    System.out.println("Cual sera el caracter que tomaras para dividir la cadena. Escribelo");
    separador=leer1.nextLine();
    Pattern expresion = Pattern.compile(separador);
    Matcher mat = expresion.matcher(cad);
String [] fragmentos = cad.split(separador);
int longitud_arreglo = fragmentos.length;
if (mat.find()) {
  System.out.println("La cadena se dividio en las siguientes partes:");
for(int i=0;i<longitud_arreglo;i++){
  System.out.println(fragmentos[i]);
}
} else {
  System.out.println("Ese caracter no existe en la cadena");
}
//System.out.println("La cadena se dividio en las siguientes partes:");
//for(int i=0;i<longitud_arreglo;i++){
 // System.out.println(fragmentos[i]);
//}
  }


  public static void  Metodo_find_(){
String text = "Sergio Mateus Guzman Zuñiga";
Pattern expresion = Pattern.compile(".*\\s.*");
 Scanner leer1 = new Scanner(System.in);
    System.out.println("La expresion regular que evaluara a la cadena es: "+expresion);
    System.out.println("Escribe la cadena a evaluar");
    text = leer1.nextLine();
Matcher valida = expresion.matcher(text);
System.out.println("Matcher dice .. "+valida.matches());
System.out.println("find dice .. "+valida.find());
  }//Aqui el find me da false por que no hay ninguna ocurrencia de 3 espacios consecutivos en blanco si la expresion fuese \\s aqui find me daria un true


  public static void looking_At(){
    String entrada = "12345-6789";
    Pattern patron = Pattern.compile("\\d{5}");
     Scanner leer1 = new Scanner(System.in);
    System.out.println("La expresion regular que evaluara a la cadena es: "+patron);
    System.out.println("Escribe la cadena a evaluar");
    entrada = leer1.nextLine();
    Matcher validacion = patron.matcher(entrada);

    if (validacion.lookingAt()) {// Verifica que el princio de la cadena coincida con la expresion regular (solo el principio)
        System.out.println("El principio de la cadena coincide con el patrón.");
    } else {
        System.out.println("El principio de la cadena NO coincide con el patrón.");
    }
  }


  public static void start_end(){
    String cadena = "La fecha de inicio es 2023-09-24 y la fecha de finalización es 2023-09-30";
        Pattern patron = Pattern.compile("\\d{4}-\\d{2}-\\d{2}");
         Scanner leer1 = new Scanner(System.in);
    System.out.println("La expresion regular que evaluara a la cadena es: "+patron);
    System.out.println("Escribe la cadena a evaluar");
    cadena = leer1.nextLine();
        Matcher validacion = patron.matcher(cadena);

        while (validacion.find()) {
            int start = validacion.start(); // Obtiene la posición de inicio de la coincidencia
            int end = validacion.end();     // Obtiene la posición de fin de la coincidencia
            String match = cadena.substring(start, end); // Obtiene la coincidencia actual

            System.out.println("Coincidencia: " + match);
            System.out.println("Posición de inicio: " + start);
            System.out.println("Posición de fin: " + end);
        }
        if(validacion.find()!= true){
          System.out.println("La subcadena no se encuentra");
        }
  }


  public static void practica_Simple(){
    String texto = "Esto es el comienzo de un texto largo fin.\n" +
    "Vamos a buscar palabras que no terminen en fin.\n" +
    "Palabra1 Palabra2 fin Palabra3 fin Palabra4.";

Pattern patron = Pattern.compile("\\w+\\s+(?!fin\\b)");
 Scanner leer1 = new Scanner(System.in);
    System.out.println("La expresion regular que evaluara a la cadena es: "+patron);
    System.out.println("Escribe la cadena a evaluar");
    texto = leer1.nextLine();
Matcher matcher = patron.matcher(texto);
/*\\b representa un límite de palabra, lo que significa que coincide con el punto en el que una palabra comienza o termina, sin incluir espacios en blanco u otros caracteres no alfanuméricos. */
while (matcher.find()) {
System.out.println("Coincidencia encontrada: " + matcher.group());
}
if(!matcher.find()){
  System.out.println("Ninguna coicidencia encontrada");
}
  }

  public static void Teams_1(){//Comprobar si la cadena tiene exactamente el patron "abc"
  System.out.println("Comprobar si la cadena tiene exactamente el patron \"abc\"");
    String texto = "";
    System.out.println("Escribe la cadena a evaluar");
    Scanner leer = new Scanner(System.in);
    texto = leer.nextLine();
        Pattern patron = Pattern.compile("abc");
    Matcher mat = patron.matcher(texto);
    if (mat.matches()) {
      System.out.println("SI coincide");
    } else {
      System.out.println("NO coincide");
    }
  }

   public static void Teams_2(){//Comprobar si el string contiene en alguna parte el patron "abc"
   System.out.println("Comprobar si el string contiene en alguna parte el patron \"abc\"");
    String texto = "";
    System.out.println("Escribe la cadena a evaluar");
    Scanner leer = new Scanner(System.in);
    texto = leer.nextLine();
        Pattern patron = Pattern.compile(".*abc.*");
    Matcher mat = patron.matcher(texto);
    if (mat.matches()) {
      System.out.println("SI coincide");
    } else {
      System.out.println("NO coincide");
    }
  }


  public static void Teams_3(){//Comprobar si el string empieza por "abc"
  System.out.println("Comprobar si el string empieza por \"abc\"");
    String texto = "";
    System.out.println("Escribe la cadena a evaluar");
    Scanner leer = new Scanner(System.in);
    texto = leer.nextLine();
        Pattern patron = Pattern.compile("^abc.*");
    Matcher mat = patron.matcher(texto);
    if (mat.matches()) {
      System.out.println("SI coincide");
    } else {
      System.out.println("NO coincide");
    }
  }


  public static void Teams_4(){//Comprobar si la cadena empieza por "Abc" o "abc"
  System.out.println("Comprobar si la cadena empieza por \"Abc\" o \"abc\"");
    String texto = "";
    System.out.println("Escribe la cadena a evaluar");
    Scanner leer = new Scanner(System.in);
    texto = leer.nextLine();
        Pattern patron = Pattern.compile("^[Aa]bc.*");
    Matcher mat = patron.matcher(texto);
    if (mat.matches()) {
      System.out.println("SI coincide");
    } else {
      System.out.println("NO coincide");
    }
  }


  public static void Teams_5(){//Comprobar si la cadena esta formada por un minimo de 5 letras mayusculas o minusculas y un maximo de diez
    System.out.println("Comprobar si la cadena esta formada por un minimo de 5 letras mayusculas o minusculas y un maximo de diez");
    String texto = "";
    System.out.println("Escribe la cadena a evaluar");
    Scanner leer = new Scanner(System.in);
    texto = leer.nextLine();
        Pattern patron = Pattern.compile("[a-zA-Z]{5,10}");
    Matcher mat = patron.matcher(texto);
    if (mat.matches()) {
      System.out.println("SI coincide");
    } else {
      System.out.println("NO coincide");
    }
  }


  public static void Teams_6(){//Comprueba que la cadena no empiece con un digito
    System.out.println("Comprueba que la cadena no empiece con un digito");
    String texto = "";
    System.out.println("Escribe la cadena a evaluar");
    Scanner leer = new Scanner(System.in);
    texto = leer.nextLine();
        Pattern patron = Pattern.compile("^[^\\d].*");
    Matcher mat = patron.matcher(texto);
    if (mat.matches()) {
      System.out.println("SI coincide");
    } else {
      System.out.println("NO coincide");
    }
    /*[^...]: Esto es una clase de caracteres negada. Significa que coincidirá con cualquier carácter que no esté dentro de los corchetes cuadrados. En este caso, los corchetes contienen \d, que 
    significa cualquier dígito (0-9). Entonces, [^\\d] coincide con cualquier carácter que no sea un dígito. */
  }


  public static void Teams_7(){//Comprueba que la cadena no acabe con un digito
    System.out.println("Comprueba que la cadena no acabe con un digito");
    String texto = "";
    System.out.println("Escribe la cadena a evaluar");
    Scanner leer = new Scanner(System.in);
    texto = leer.nextLine();
        Pattern patron = Pattern.compile(".*[^\\d]$");
    Matcher mat = patron.matcher(texto);
    if (mat.matches()) {
      System.out.println("SI coincide");
    } else {
      System.out.println("NO coincide");
    }
    
  }


  public static void Teams_8(){//Comprueba que la cadena solo contenga los caracteres "a"  o  "b"
  System.out.println("Comprueba que la cadena solo contenga los caracteres \"a\"  o  \"b\"");
    String texto = "";
    System.out.println("Escribe la cadena a evaluar");
    Scanner leer = new Scanner(System.in);
    texto = leer.nextLine();
        Pattern patron = Pattern.compile("(a|b)+");
    Matcher mat = patron.matcher(texto);
    if (mat.matches()) {
      System.out.println("SI coincide");
    } else {
      System.out.println("NO coincide");
    }
    
  }


  public static void Teams_9(){//Comprueba si la cadena contiene un "1" y  ese uno no esta seguido por un "2"
  System.out.println("Comprueba si la cadena contiene un \"1\" y  ese uno no esta seguido por un \"2\"");
    String texto = "";
    System.out.println("Escribe la cadena a evaluar");
    Scanner leer = new Scanner(System.in);
    texto = leer.nextLine();
        Pattern patron = Pattern.compile(".*1(?!2).*");
    Matcher mat = patron.matcher(texto);
    if (mat.matches()) {
      System.out.println("SI coincide");
    } else {
      System.out.println("NO coincide");
    }
    
  }
  /*  Cuantificadores comunes:
  
  * (Asterisco): Coincide con cero o más repeticiones del elemento anterior. Por ejemplo, a* coincidirá con "a", "aa", "aaa", y así sucesivamente.

    + (Más): Coincide con una o más repeticiones del elemento anterior. Por ejemplo, a+ coincidirá con "a", "aa", "aaa", pero no con una cadena vacía.

    ? (Signo de interrogación): Coincide con cero o una repetición del elemento anterior. Por ejemplo, colou?r coincidirá con "color" o "colour".

    {n} (Llaves): Coincide exactamente con n repeticiones del elemento anterior. Por ejemplo, a{3} coincidirá con "aaa".

    {n,} (Llaves con coma): Coincide con al menos n repeticiones del elemento anterior. Por ejemplo, a{2,} coincidirá con "aa", "aaa", "aaaa", etc.

    {n,m} (Llaves con coma y valor máximo): Coincide con al menos n pero no más de m repeticiones del elemento anterior. Por ejemplo, a{2,4} coincidirá con 
    
    "aa", "aaa", o "aaaa", pero no con "a" ni con "aaaaa". */

  
  
  
    public static void main(String[] args) {
        int op = 0;
        Scanner leer = new Scanner(System.in);
        while(op!=18){
          System.out.println("___MENU DE OPCIONES___\n "+
          "         \"1.-Pattern matches\"+\r\n" + //
              "          \"2.-Pattern compile \"+\r\n" + //
                  "          \"3.-checkMatch \"+\r\n" + //
                      "          \"4.-Pattern split \"+\r\n" + //
                          "          \"5.-Metodo find \"+\r\n" + //
                              "          \"6.-looking At \"+\r\n" + //
                                  "          \"7.-start_end \"+\r\n" + //
                                      "          \"8.-Practica simple\"+\r\n" + //
                                          "          \"9.- Teams_1\n"+ 
                                                       "          \"10.-Teams_2\r\n" + //
                                                       "          \"11.-Teams_3\r\n" + //
                                                       "          \"12.-Teams_4\r\n" + //
                                                       "          \"13.-Teams_5\r\n" + //
                                                       "          \"14.-Teams_6\r\n" + //
                                                       "          \"15.-Teams_7\r\n" + //
                                                       "          \"16.-Teams_8\r\n" + //
                                                       "          \"17.-Teams_9\r\n" + //
                                                       "          \"18.-Salir\r");
                                          System.out.println("Que opcion deseas");
                                          boolean valido = false;
                                          do {
                                            try {
                                              op = leer.nextInt();
                                              valido = true;
                                            } catch (InputMismatchException e) {
                                              System.out.println("Entrada no valida ponga atencion en el menu y note que solo puede introducir numeros entre 1 y 18");
                                              leer.nextLine();
                                            }
                                          } while (!valido);
switch(op){
  case 1:{
Pattern_matches();
  }break;
  case 2:{
Pattern_compile();
  }break;
  case 3:{
checkMatch();
  }break;
  case 4:{
Pattern_split();
  }break;
  case 5:{
Metodo_find_();
  }break;
  case 6:{
looking_At();
  }break;
  case 7:{
start_end();
  }break;
  case 8:{
practica_Simple();
  }break;
  case 9:{
Teams_1();
  }break;
  case 10:{
Teams_2();
  }break;
  case 11:{
Teams_3();
  }break;
  case 12:{
Teams_4();
  }break;
  case 13:{
Teams_5();
  }break;
  case 14:{
Teams_6();
  }break;
  case 15:{
Teams_7();
  }break;
  case 16:{
Teams_8();
  }break;
  case 17:{
Teams_9();
  }break;
  case 18:{
System.out.println("Fin de la ejecucion");
  }break;
  default:{
System.out.println("Solo numeros entre 1 y 18");
  }break;
}


        }
    }
}
