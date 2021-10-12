package com.company;

class A{
    int a=100;
    public int getA(){
       return 4;
    }

    public void method(){
        System.out.println("i am method of class A : "+a);
    }
}

class B extends A{
    int b=500;
    @Override
    public int getA(){
        return 110;
    }
    public void method(){
        System.out.println("this is overrindin method function of class B : "+b);
    }

}

public class Overriding {
    public static void main(String[] args) {
    A a=new A();
    a.method();
    B b = new B();
    b.method();
    }
}
