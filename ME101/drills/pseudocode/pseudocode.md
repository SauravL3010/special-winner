# Translating pseudocode

If you don't know how to read or translate pseudocode, the section at the end of this document entitled "How to translate pseudocode" should be your first step.  Otherwise, please jump in!

#The drill problems

For every drill problem below, put your code into the following skeleton program:

    #include <iostream>
    #include <cmath>
    using namespace std;
    int main()
    {
      //put all your code here
    }

The drills in this document will focus on having you translate different types of pseudocode into actual code.  To make things harder, I won't tell you what the code is supposed to do - you need to figure that out by the pseudocode itself.  I suggest that you begin by first reading the pseudocode and determine what it should do, then write the code itself and test to see if it worked.

## Question 1

    Declare an integer, n
    loop until n > 0
      Get the user to enter n
    end loop
    if n is divisible by 15 but not by 10
      print n / 15
    otherwise
      inform the user

## Question 2

    Declare an array of integers, AR, of size 10
    for i = 0; i < 10; i++
      have the user enter AR[i]
    end for
    Declare an integer, maxInt
    Set maxInt equal to AR[0]
    for i = 0; i < 10; i++
      if maxInt is less than AR[i]
        Set maxInt equal to AR[i]
      end if
    end for
    print maxInt

## Question 3

      Declare an array of integers, AR, of size 10
      Have the user enter all of the values of AR, using a loop
      Declare a double, avg
      Set avg equal to 0
      For every element of AR
        add that element to avg
      end for
      Set avg equal to avg divided by 10
      print avg

## Question 4

    Ask the user if they are a student at UW
    If the user is a student
      Ask the user for their grade in calculus
      If their grade is above 90
        Output "Well done!"
      If their grade is above 60
        Output "Doing good!"
      Otherwise
        Output "You should talk to your WEEF TA"
      end if
    If the user is not a student
      Output "Nevermind"
    end if

## Question 5 (adapted from en.wikipedia.org/wiki/Structured_English)

    If the user has an account at the bank
      If the user's account balance is positive
        Inform the user that their loan is approved
      Else if the user has received a manager's approval
        Inform the user that their loan is approved
      Else
        Inform the user that their loan is rejected
      end if
    Else
      Inform the user that their loan is rejected
    end if


# How to translate pseudocode

A *huge* part of learning how to write programs is learning how to break the problem into manageable steps.  Ideally, your design should be detailed enough that you can turn each piece of it into code without doing further design to understand what needs to be done.  In reality, you won't always be able to produce such a detailed design all at once.  In this set of drill exercises, you are going to be writing code from "pseudocode".  Pseudocode is one way of designing code that lists the steps in a more formal way than just writing it out or drawing a diagram.  Here is an example:

## Print the integers from 0 to 100

The program we wish to write will print the integers from 0 to 100.  Let's turn this into a type of pseudocode first.

        declare an integer, i
        set i to 0
        loop until i equals 101
          print i
          increment i by 1
        end of loop

This type of pseudocode is pretty close to an English description of what the code should do.  Let's start by converting it into actual code, then I'll show you some other, more compact ways of writing pseudocode that are closer to C++.  To begin with, I'm going to write my code very closely to my pseudocode:

        int i; //declare an integer, i
        i = 0; //set i to 0
        while(i <= 100) //loop until i equals 101
        {
          cout << i << " "; //print i
          i = i + 1; //increment i by 1
        } //end of loop

You may be wondering if there were any other ways to do this, and in fact there are.  One other possible implementation uses for loops.  The code below is more compact, but it's less obvious how it translates back to the pseudocode.  Try to see if you can identify all of the parts of the pseudocode in the next code snippet:

        for(int i = 0; i <= 100; i++)
        {
          cout << i << " ";
        }

## A more "C++ like" version of pseudocode

The example above was fairly verbose, and it's not clear how to turn it into code (what do I mean by "loop until...", for example?)  So the next thing we are going to do is write with a more C++ like syntax.  This version of pseudocode is nice in that it's a lot easier to turn into code.  The downside is that you have to have a pretty strong idea of what you want your code to look like in the first place.  

The example we are going to use is called "fizzbuzz": loop over the integers from 0 to 100.  If the number is divisible by 3, output "fizz", if it is divisible by 5, output "buzz" (see en.wikipedia.org/wiki/Pseudocode for a more detailed version of this).  

Here is my C++ like pseudocode:

        for(i = 0; i <= 100; i++)
        {
          if i is divisible by 3
            print "fizz"
          if i is divisible by 5
            print "buzz"
        }

You may notice a few things.  I'm missing some relatively important details:

- I don't mention that i should be an integer
- I don't specify what I mean when I say "i is divisible by 3"
- I don't specify *how* to print i, I just say that it has to happen

Writing pseudocode like this is great when you're stuck on a certain step and just want to make sure you have a grasp of the whole algorithm before diving into the specific things you're skipping over (like what it means to be divisible).  Let's turn this into code:

        for(int i = 0; i <= 100; i++)
        {
          if(i%3 == 0)
          {
            cout << "fizz";
          }
          if(i%5 == 0)
          {
            cout << "buzz";
          }
        }

When writing code, even on an exam, starting with pseudocode will help you a lot to understand what you're trying to do.  
