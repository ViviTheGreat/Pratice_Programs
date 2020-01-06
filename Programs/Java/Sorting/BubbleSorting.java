//Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. 
class BubbleSorting {
    public static void main(String[] args){
    int arr[] = { 2 ,3, 1, 12 ,99 ,-1};
    for(int j=0;j<arr.length-1;j++){
        for (int i=0;i<arr.length-1-j;i++){
            if(arr[i]>arr[i+1]){
                int temp;
                temp=arr[i];
                arr[i]=arr[i+1];
                arr[i+1]=temp;
            }    
        }
    }
    for(int k=0;k<arr.length;k++){
        System.out.print(arr[k]+" ");
    }

    }
}
