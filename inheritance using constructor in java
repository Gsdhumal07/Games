package com.company;


class base1{
    public int x;
    base1(){
        System.out.println("this is the constructor of thr base class ");
    }
    base1(int a){
        System.out.println("i am the overloaded constructor of the base class "+a);
    }
    public int getX(){
        return x;
    }
    public void setX(){
        this.x=x;
    }

}

class derived1 extends base1{
    public int y;


    derived1(){
        // if i want to call the overloaded constructor of the base class then use
//        super(5);
        System.out.println("this it the constructor of the derived class");
    }
    derived1(int x, int y){
        super(x);
        System.out.println("i am the overloaded constructor of the derived class  "+ x+" "+ y);
    }
    public int getY(){
        return y;
    }
    public void setY(){
        this.y=y;
    }

}
class derived2 extends derived1{
    derived2(){
        System.out.println("i am the constructor of the deriver2 class");
    }
    derived2(int x,int y,int z){
        super(x,y);

        System.out.println("i am the overloaded constructoer of the derived2 class "+x+" "+y+" "+z);
    }
}

public class construster_in_inheritance {
    public static void main(String[] args) {
//        base1 bs=new base1();
//        first it invoke the base class constructor and then call the constructor of base class
//          derived1 dr=new derived1();
//          for calling the overloaded constructor of the derived class
//          derived1 drd= new derived1(16,45);
          derived2 dr2 = new derived2(12,15,78);
    }
}
