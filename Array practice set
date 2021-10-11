package com.company;
import java.util.Scanner;

import java.util.Scanner;

public class array_practice_set {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n;
//        creation of array displaying and the sum of array elements
        System.out.println(" enter the number you want to add in array : ");
        n=sc.nextInt();
        float []arr=new float[n];
        System.out.println("enter the elements in array : ");
        for(int i=0; i<n ; i++){
            arr[i]=sc.nextFloat();

        }

        float sum=0;
        System.out.println("the array elements are ");
        for(int i=0; i<n ;i++){
            System.out.print(arr[i]+" ");
            sum=sum+arr[i];
        }
        System.out.println("\nthe sum of elements in array : "+sum);

        System.out.println("### printing array in the reverse order : #####");
        int l=arr.length;
        int p=Math.floorDiv(l,2);
        for(int i = 0 ; i < p ;i++){
            float temp=arr[i];
            arr[i]=arr[l-i-1];
            arr[l-i-1]=temp;
        }
        for(float elements:arr){
            System.out.print(elements + " ");
        }

////        find the element is in array or not
//        int isInarray;
//        System.out.println("\nenter the element to find element in array : ");
//        isInarray=sc.nextInt();
//        for(int i =0 ;i <n ;i++){
//            if (arr[i]==isInarray){
//                System.out.println(" True ");
//            }
//
//        }
//
//        System.out.println("the maximun and minimun element in the array : ");
//        float max =0;
//        float min=0;
//        for(float e:arr) {
//            if (e > max) {
//                max = e;
//
//            }
//            if (e < min) {
//                min = e;
//            }
//
//        }
//        System.out.println("the maximum element in array is : "+max);
//        System.out.println("the minimum element in array is : "+min);

        System.out.println("\n To find array is sorted or not : ");
        boolean issorted=true;
        for (int i=0;i<arr.length;i++){
            if(arr[i]>arr[i+1]){
                issorted=false;
                break;
            }
        }
        System.out.println(issorted);
        System.out.println("the sorted array is : ");
        for (int i=0;i<arr.length;i++){
            for(int j =i+1;j<arr.length;j++){
                if (arr[j]<arr[i]){
                    float pass=arr[i];
                    arr[i]=arr[j];
                    arr[j]=pass;

                }


            }
        }
//        System.out.println("sorted array is " );
//        System.out.println("the array elements are ");
        for(int i=0; i<n ;i++) {
            System.out.print(arr[i] + " ");
        }


//        2-D array creation :
        float add=0;
        float [][]marks=new float[2][3];
        System.out.println("enter the elements in array : ");
        for(int i =0; i<marks.length;i++){
//            marks[i][0]=sc.nextInt();
            for (int j=0;j<marks[i].length;j++){
                marks[i][j]=sc.nextInt();
                System.out.print(marks[i][j]+" ");
                add=add+marks[i][j];
            }
            System.out.println(" ");

        }
        System.out.println(" the sum of the elements : "+add);






    }
}
