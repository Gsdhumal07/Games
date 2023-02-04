package com.company;
import java.util.Random;
import java.util.Scanner;


public class Rock_papere_scciser {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);

        System.out.println("00.Rock\n"+"01.Paper\n"+"02.Scissor");
        Random ran=new Random();
        int n=3;
        int computerchoice=ran.nextInt(n);
        System.out.println("Enter your choice : ");
        int ch=sc.nextInt();
        System.out.println("the computer choice is "+computerchoice);
        if(ch==computerchoice){
            System.out.println("you both have same choice : ");
        }
        else if(ch==0 && computerchoice==2 || ch== 1 && computerchoice==0 ||
                ch==2 && computerchoice==1){
            System.out.println("**YOU WIN** ");
        }
        else{
            System.out.println("**Computer WIN** ");
        }


    }
}
