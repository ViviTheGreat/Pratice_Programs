//1.Write a program to print duplicate character of the string
import java.util.Scanner;
class PraticeProgram1{
    public static void main(String[] args){
         Scanner input = new Scanner(System.in);
        System.out.println("Enter the string");
         String s=input.nextLine();
        System.out.println("You have entered " + s);
         char[] eachChar=s.toCharArray();
        for (int i=0; i < s.length(); i++) {
            for(int j=i+1;j<s.length();j++){
                    if(eachChar[i]==eachChar[j]){
                    System.out.println("Duplicate Character: "+eachChar[j]);
                }
                //System.out.println(eachChar[i]);        
            }
            
        }
    }
}