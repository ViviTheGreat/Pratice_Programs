/*Repeatedly finding the minimum element (considering ascending order) from unsorted part 
and putting it at the beginning. The algorithm maintains two subarrays in a given array.
1) The subarray which is already sorted.
2) Remaining subarray which is unsorted. */
class InsertionSorting{
    public static void main(String [] args){
        int [] array = {20,1,3,-7,0,-20};
        for(int i=0;i<array.length;i++){
            int small=array[i];
            for(int j=i+1;j<array.length;j++){
                if(array[j]<array[i])
                {small=array[j];}
            }
        array[i]=small;
    }
    for (int i=0;i<array.length;i++){
        System.out.print(array[i]+ " ");
    }
    }
}

