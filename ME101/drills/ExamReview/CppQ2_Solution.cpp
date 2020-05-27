#include <iostream>
#include <fstream>

using namespace std;

int gradeQuestion(char student, char ans)
{
	if(student == ans)
	{
		//got it right!
		return 5;
	}
	else if(student != 'Z')
	{
		//got it wrong :(
		return -2;
	}
	
	//I don't need an else statement here, since this is the only option left
	return 0;
}

/*
	For this function, we don't know how many total marks are possible on the
	test until we read the file, so we have to send it in.
*/
float percGrade(int studentMark, int totalMarks)
{
	return 100.0*studentMark/totalMarks; //it's the percentage they got
}

int main()
{
	//we need to open two input files, so we need to call them different things
	ifstream answers("answers.txt");
	ifstream students("students.txt");
	
	//verify that they opened
	if(!answers || !students)
	{
		cout << "Error opening file!";
		return 0;
	}
	
	//the array is at most 30 characters
	char correct[30] = {0};
	int numAnswers = 0;
	while(answers >> correct[numAnswers])
	{
		numAnswers++;
	}
	
	//now read in the number of students
	int numStudents = 0;
	students >> numStudents;
	
	/*
		Now here's the tricky part.  I need to read each student's answers,
		compute their individual scores, and then move on to the next student.
		I actually need a double loop here.  Interestingly, I do NOT require
		any more arrays.  I can mark the questions one by one.   In fact,
		it would be very hard to make a second array - how big should it be?
	*/
	
	//we need to know what the test is out of.  Max marks is 5*numAnswers;
	float maxMarks = 5.0*numAnswers;
	
	float avg = 0; //we also need to compute the average
	for(int i = 0; i < numStudents; i++)
	{
		float studentGrade = 0;
		for(int j = 0; j < numAnswers; j++)
		{
			char c = 0;
			students >> c;
			studentGrade += gradeQuestion(c,correct[j]);
		}
		
		//compute their percent grade, output, and add to the class average
		float studentPercent = percGrade(studentGrade, maxMarks);
		avg += studentPercent;
		cout << "Student " << i << " got: " << studentPercent << endl; 
	}
	
	//output the class average
	cout << "Class average: " << avg/numStudents;
}
