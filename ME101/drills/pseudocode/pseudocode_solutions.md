# Question 1

#### What does the code do?

First, the user will enter a non-negative integer, and the program will enforce that the integer is positive.  Then, one of two things will happen:

1. If the number is divisible by 15 **but not 10** the quotient will be printed
2. For any other possibility, the user will be informed

#### Solution

    int n = -1;
    do{
      cin >> n; //we could prompt the user, but we weren't asked to
    }while(n < 0);

    if(n%15 == 0 && n%10 != 0)
    {
      cout << n/15;
    }
    else
    {
      cout << "Number is not divisible exclusively by 15."
      //Note: I had MANY options for how to "inform the user"
    }

# Question 2

#### What does the program do?

This program has the user enter integers into an array, then finds the largest element of the array, and prints it to the screen.

#### Solution

    int AR[10] = {0};
    for(int i = 0; i < 10; i++)
    {
      cin >> AR[i]; //again, I didn't need to prompt, but I could have
    }
    int maxElement = AR[0]; //always initialize inside the array, to avoid
    //guessing at a good initialvalue
    for(int i = 0; i < 10; i++)
    {
      if(maxElement < AR[i])
      {
        maxElement = AR[i];
      }
    }
    cout << maxElement;

# Question 3

#### What does the program do?

This program has the user enter integers into an array, then computes and displays their average.

#### Solution

    int AR[10] = {0};
    //The pseudocode just specified "a loop", but I chose a for loop
    for(int i = 0; i < 10; i++)
    {
      cin >> AR[i]; //again, I didn't need to prompt, but I could have
    }
    double avg = 0;
    //the next part of the pseucode is again informing me that I should be
    //using a for loop.  "Every element of AR" means loop from AR[0] to AR[9]
    for(int i = 0; i < 10; i++)
    {
      avg += AR[i];
    }
    avg = avg/10.0;
    cout << avg;

# Question 4

This program's pseudocode is a little less structured than the ones above.  It was designed to give you a decent, but not necessarily complete, idea of what the code should do.

#### What does this program do?

It's going to give the user a message based on their grade in calculus, or just tell them to ignore us if the user is not a student.

#### Solution

    //the pseudocode doesn't describe the variables, but we need at least the
    //grade and the person's status
    int grade = 0;
    bool isStudent = false;
    cout << "Are you a student at UW?";
    cin >> isStudent;
    if(isStudent)
    {
      cout << "What is your grade in calculus?"
      cin >> grade;
      if(grade > 90)
      {
        cout << "Well done!";
      }
      else if(grade > 60)
      {
        cout << "Doing good!"; //doing well?
      }
      else
      {
        cout << "You should talk to your WEEF TA." //they're really nice people!
      }
    }
    else
    {
      cout << "Nevermind";
    }

# Question 5

This program is even less structured.  This is the kind of pseudocode that you should become comfortable writing for an exam.  It's quick, is based primarily on English, and lets you get your thoughts down and organized.  It needs quite a bit of unpacking before we can use it.

#### What does this program do?

This program determines whether a user is qualified for a loan or not based on whether they have an account and, if so, if that account has a positive balance or if they get a manager's approval.

#### Solution

    //we need a bunch of variables.  First, does the user have an account?
    bool hasAccount = false;
    //next, their balance (we could also ask them if they have a positive
    //balance, the pseudocode does not specify
    int balance = 0;
    //Finally, whether or not they have manager approval (we could declare this
    //when we need it, but I like to declare at the top
    bool hasApproval = false;

    //we need to ask the user if they have an account
    cout << "Do you have an account?";
    cin >> hasAccount;
    if(hasAccount == true)
    {
      cout << "Do you have a positive account balance?"
      cin >> balance;
      if(balance < 0)
      {
        cout << "Do you have manager approval?"
        cin >> hasApproval;
        if(hasApproval)
        {
          cout << "Loan approved."
        }
        else
        {
          cout << "Loan rejected."
        }
      }
      else
      {
        cout << "Loan approved.";
      }
    }
    else
    {
      cout << "Loan rejected."
    }

Did you notice, in this question, how much code we had to write to get it going?  Hopefully, the pseudocode was clear enough that you understood broadly what you were supposed to do.  However, if it wasn't, try to convert it into a more clear form for yourself.  Although there are lots of formal ways to write pseudocode, you can develop your own style, especially for exams.
