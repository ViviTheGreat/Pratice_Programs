//write a program to print star using loop
class StarProgram{
    public static void main(String[] args){
        Star s = new Star();
        s.normalStar(5);
        s.pyramidStar(5);
        s.pyramidNumber(5);

    }
}

class Star{
    void normalStar(int n){
        for(int i=0;i<n;i++){
            for(int j=0;j<i+1;j++){
                System.out.print("* ");
            }
        System.out.println("");
        }
    }

    void pyramidStar(int n){
        for(int i=0;i<n;i++){
            for(int j=n;j>i;j--){
                System.out.print(" ");
            }
        for(int k=0;k<i+1;k++){
            System.out.print("*  ");
        }
        System.out.println("");
        }
    }
    void pyramidNumber(int n){
        for(int i=0;i<n;i++){
            for(int j=n;j>i;j--){
                System.out.print(" ");
            }
        for(int k=0;k<i+1;k++){
            System.out.print((k+1) + "  ");
        }
        System.out.println("");
        }
    }


}