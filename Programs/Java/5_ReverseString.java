//5.Write a program to reverse a string.
//Using Reverse String Method of StringBuilder
import java. util. Scanner;
class PracticeProgram5{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the String: ");
        String str=input.nextLine();
        //StringBuilder strBuilder=new StringBuilder();
        //strBuilder.append(str);
        //strBuilder=strBuilder.reverse();
        //System.out.println(strBuilder);
        char[] ch = str.toCharArray();
        for(int i=(str.length()-1);i>=0;i--){
            System.out.println(ch[i]);
        }
    }
}