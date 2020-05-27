# Concepts

## Question 1

1. You **do not** need to create a file before you can write to it.  When you declare a new ofstream, the computer will check to see if the file already exists.  If it does, then it will open the file and overwrite whatever is already there.  If the file does  not exist, it will make a new one for you.
2. You **do** need to have an existing file to read from.  If you create a new ifstream but try to open a file that doesn't exist, then that input file stream will be NULL (empty) and cannot be read from.  Any attempts to read from the file stream will result in no changes being made to your variables, and **false** being returned.
3. This is correct.  An already opened file cannot be opened a second time.  You need to close it with the close() function, and then you can re-open it.  A side-effect of this is that you cannot have a file open for reading and writing at the same time.
4. Although there are many different reasons that a file might fail to open, one of the most common ones is that a file with the provided file name does not exist.  For instance, if I have a file called myFile.txt but I use the following code: `ifstream fin("Myfile.text");` the computer will not be able to find the file that I "meant" to open, and therefore fin will be NULL.  In order for an input file stream to open, it must exist **in the same folder as the executable**, or you need to tell the computer exactly where to look for it.

## Question 2

### Part a

The issue here is that we are not using quotes for the file name.  File names are strings of characters, and should be treated as such.  So:

    ifstream fin("myFile.txt");

is appropriate.  If you're wondering if you can do something like this:

    string fName = "myFile.txt";
    ifstream fin(fName);

You can't.  In fact, you get a rather scary error message:

    [Error] no matching function for call to 'std::basic_ofstream<char>::basic_ofstream(std::string&)'

strings aren't quite the same as string **literals**, which is what we have been passing in as a file name.  There are ways to use a variable as a file name, but we won't be using them in this course.  However, if you're very curious:

    char fName[] = "myFile.txt";
    ifstream(fName);

The above code WILL work, but it's not ideal.

### Part b

The issue is that we are trying to open a file for both reading and writing, which the computer does not allow us to do.  Unfortunately, the fix it to pick one and stick with it - we can either read or we can write, but we can't do both.  However, once we open the file for writing we are erasing its contents anyway, so we would never really want to do this.  Most likely we can create a new file to write to, and leave the old one for reading.

### Part c

The issue is actually fairly subtle.  The code will run, and it will not have any errors at compile-time.  In fact, it won't even have any errors at run-time that cause it to crash.  If you didn't check on the values in the array and verify them somehow, you wouldn't know that there was a problem.

The issue is that myFile.txt contains 6 entries, but we are  trying to read 10 things into the array.  What will happen is this:

1. The first 6 entries will be read without error.  The array will store the values `{5, 1, 2, 3, 4, 3, ?, ?, ?, ?}`, where I've used the "?" to indicate that it is a random value already stored in memory when  the array was initialized.
2. When we try to read the 7th value, the file read will fail.  The behaviour of the input file stream at this point is to **not change the value of the variable**, so whatever was already in the array will remain there without change.  Importantly, it will **not** just put in 3, which is the last entry of the file.  That entry has already been read and won't be read again until the file is closed and re-opened.

So, how do we get around this?  Well, first we need to define what it was that we intended to do.  For instance, if we meant to fill up the entire array, then we might be using the wrong file to do so - there simply aren't enough entries - or we might be using too large an array.  However, there are many applications where we might specify a maximum file size.  For instance, if there can be at most 10 attendees at a workshop, then we would store **at most** 10 things in our file, but we might store less.  In this case, it makes sense to make an array of size 10, but we need to make sure that when we read the file we keep track of how big it is.  To do so, we'll read the file in a while loop:

    ifstream fin("myFile.txt");
    int newIntAr[numEntries];
    int numEntries = 0;
    while(fin >> newIntAr[numEntries])
    {
      numEntries++;
    }

Once the while loop is done, we will know how many entries were in the file (it's numEntries + 1, since numEntries started at 0), and we will not try to read beyond the end of the file.  This is the appropriate way to read a file when you don't know how many entries it contains.

Did it bother you that we had the statement `fin >> newIntAr[numEntries]` in the while loop's condition?  C++ allows us to simultaneously read files and check if the read was successful.   What actually happens in that condition is the following:

1. First, the read is attempted.  As long as there is an integer that can be read from the file, the array will be updated appropriately.
2. The input file stream is then checked to see if the read was successful:
  - If the read was successful, the file stream returns true, and the while loop continues
  - Otherwise, the file stream returns false, and the while loop exits

So what  we have above is a **simultaneous** read-and-check.   We **do not** have to re-read.

# File Input

## Question 1

We don't need to store anything in arrays, since we're just reading and printing.   We'll need a single integer that gets overwritten each time.  Since we know how many entries are in the file we can use a for loop:

    ifstream fin("file1.txt");
    int incoming = 0; //always initialize, even if you are overwriting it!
    for(int i = 0; i < 10; i++)
    {
      fin >> incoming;
      cout << incoming << endl;
    }


## Question 2

When we don't know how many entries are in the file, we use a while loop.

    ifstream fin("file1.txt");
    int incoming = 0; //always initialize, even if you are overwriting it!
    while(fin >> incoming)
    {
      cout << incoming << endl;
    }

## Question 3

We need to use a nested loop to read this file.  A while loop will be used to read the number of entries in each record, then a for loop will be used to read that many entries from the file, and add each one to a running sum.

    ifstream fin("file2.txt");
    int numEntries = 0;
    while(fin >> numEntries)
    {
    int temp = 0;
    int sum = 0; //initialize INSIDE the while loop!
    for(int i = 0; i < numEntries; i++)
    {
      fin >> temp;
      sum += temp;
    }

      cout << sum << endl;
      i++;
    }

If your code works, you'll see that the first record has a sum of 5154.

## Question 4

In order to do this, we need to keep track of the robot's current orientation with respect to the x axis, which means that we have to use fmod to ensure that it lies within 0 and 360.  After that, it's pure trigonometry!

    
    ifstream fin("file3.txt");
    double theta = 0, totTheta = 0, x = 0, y = 0, dist = 0, totDist = 0;
    while(fin >> theta >> dist)
    {
    	//we want to make sure we are within 0 to 360
    	totTheta = fmod(totTheta + theta, 360.0);
      //don't forget to convert to radians!
    	double radTheta = totTheta * M_PI / 180.0;

      //trig
    	x = x + dist*cos(radTheta);
    	y = y + dist*sin(radTheta);

    	totDist += dist;
    }

    cout << "Total distance: " << totDist << "m" <<  endl;
    cout << "(x,y) = (" << x << "," << y << ")" << endl;
    cout << "Orientation: " << totTheta << " Degrees";

# File Input/Output

## Question 1
I'm going to be sneaky here and ask the user to enter only one string at a time.  That way, I can have at least a little bit of control over what the user gives me.

    string answer = ""; //I only need one, since it will be overwritten
    ofstream fout("nameFile.txt");
    cout << "What's your first name ";
    cin >> answer;
    fout << answer << endl;
    cout << "What's your last name? ";
    cin >> answer;
    fout << answer << endl;
    cout << "What is your street name? ";
    cin >> answer;
    fout << answer << endl;
    cout << "What is your phone number? Enter without spaces, like this: ";
    cout << "555-555-5555: ";
    cin >> answer;
    fout << answer << endl;

## Question 2 and Question 3

I'm going to solve Question 2 in the generic way, with the assumption that I don't know how many lines there are in the file. In general, unless the file itself contains that information, you should **always** assume that you don't know how big the file is.  That way, you can run your code using different files of the same format and it will still work.

    ifstream fin("file4.txt");
  	ofstream fout("salesFile.txt");
  	string prodName = "";
  	double cost = 0, preTaxTotal = 0, savings = 0;
  	bool isSale = 0;
  	int discount = 0;
  	while(fin >> prodName >> cost >> isSale)
  	{
  		discount = 0; //I need to reset this, since it gets set if the
  		//previous product is on sale
  		double price = cost; //this is adjusted if there is a discount
  		if(isSale == 1)
  		{
  			fin >> discount; //obtain the discount
  		}
  		price = price * (1-discount/100.0); //apply the discount
  		savings += cost*(discount/100.0); //compute the savings
  		preTaxTotal += price;
  	}
  	fout << fixed << setprecision(2); //this works in an output file stream, too
  	fout << "The pre-tax total is: $" << preTaxTotal << endl;
  	//I didn't give you an amount for tax, so you can make it up if you want
  	fout << "The post-tax total is: $" << preTaxTotal*1.13 << endl;
  	fout << "You saved: $" << savings << endl;
