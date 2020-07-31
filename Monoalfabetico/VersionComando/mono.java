class encript {
  public static String plain = "abcdefghijklmnopqrstuvwxyz";

  public static void main(String[] args) {
    if(args.length == 1 && args[0].equals("help")){
      help();
    }
    System.out.println("Text: "+args[1]+"\nKey: "+args[0]+ "\nEncription: "+encripting(validator(args)));

  }

public static void help(){
  System.out.println("\tBIENVENIDO A ENCRIPT\n\n"
      + "Para ejecutar encript solo necesita correr el comando >java encript clave texto\n"
      + "\nla clave es la forma de encritacion, debe tener 26 caracteres\n"
      + "el texto es lo que vamos a encriptar\n\n"
      + "Ejemplo de ejecucion: \njava encript DKVQFIBJWPESCXHTMYAUOLRGZN ifwewishtoreplaceletters \n\nEl resultado de la encriptacion anterior es: WIRWAJUHTSDVFSFUUFYA");
      System.exit(0);
}

  public static String[] validator(String[] args){
    if(args.length < 2){
      System.err.println("Error! necesita al menos dos parametros para ejecutar la encriptacion. \n más informacion > encript help");
      System.exit(0);
    }
    if(args.length == 2){
      if(args[0].length() < 26){
        System.err.println("Error! el argumento de llaves necesita 26 caracteres");
        System.exit(0);
      }
    }
    return args;
  }

  public static String encripting(String[] args){
    String encripted = "";
    for(int i=0; i<args[1].length(); i++){
      for(int j=0; j<plain.length(); j++){
        if(args[1].charAt(i) == plain.charAt(j)){
          encripted += args[0].charAt(j);
        }
      }
    }
    return encripted;
  }
}


/*
Paso 1: capturar los argumentos [Listo]
Paso 2: Validar los argumentos [Listo]
Paso 3: Encriptar usando alfanumericos


javac mono.java
java encript DKVQFIBJWPESCXHTMYAUOLRGZN ifwewishtoreplaceletters 
*/

