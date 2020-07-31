import java.util.Scanner;
class MainP {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    String cipher = "DKVQFIBJWPESCXHTMYAUOLRGZN";
    String plain = "abcdefghijklmnopqrstuvwxyz";
    
    String msg, ciphermsg ="";
    System.out.println("Ingrese el mensaje a encriptar: ");
    msg = scan.next();
    
    for (int i=0; i<msg.length(); i++){
      int ascii = (97 - msg.charAt(i));
      ciphermsg += cipher.charAt(ascii);
    }
    
    System.out.println("Mensaje Cifrado: "+ciphermsg);
    scan.close();
  }
}