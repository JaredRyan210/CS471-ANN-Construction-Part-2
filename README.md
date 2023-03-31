Assignment Goal
Create a working ANN Classifier
Work with Mbytes of data
Experience statistical learning using ANN
Experience Hyperparameters tuning 
Notes:
https://sqlite.org/cli.htmlLinks to an external site.

Python to create css header:

columns = []

for i in range(784):

    columns.append(f"a{i}")

print(f"letter,{','.join(columns)}")

 brew install sqlite3

sqlite3

.separator ,

.mode csv

.import "/Users/cjardin/Desktop/A_Z Handwritten Data.csv" hw_data

 

create index hw_data_letter on hw_data(letter);

select * from hw_data hw_data where letter = 0 order by random();

select * from hw_data hw_data where letter = 0 order by random() limit 10;

select letter, count(*) from hw_data group by letter;

https://www.tutorialspoint.com/sqlite/sqlite_c_cpp.htmLinks to an external site.

https://stackoverflow.com/questions/1525444/how-to-connect-sqlite-with-javaLinks to an external site.

https://stackoverflow.com/questions/13192643/is-it-possible-to-access-an-sqlite-database-from-javascriptLinks to an external site.

http://www.newlisp.org/code/modules/sqlite3.lsp.htmlLinks to an external site.

 

The Assignment 
Our-Digits-task-requires-recognition-of-handwritten-digits-Participants-collect-data.png

You will be working with this dataset:

https://www.nist.gov/srd/nist-special-database-19Links to an external site.

CSV Provided here:

A_X_Handwritten_Data.csvLinks to an external site.

http://clubharry-client-prod.s3.amazonaws.com/A_Z%20Handwritten%20Data.csv

The CSV has 785 columns. The first column is an integer between 0 and 25 representing A - Z 

A = 0

B = 1

...

The remainder of the 784 columns represents a flattened 28x28 gray scale image of a hand written character. That is columns 2 through 785 contain a decimal value of 0 to 255 where 0 would be the absence of color, and 255 would be the color black.

c.png

Your assignment will be to use your last assignment to correctly classify the letters between A and Z. 

Steps that need to be achieved:

Intake the provided CSV
Create the following training and testing datasets 
A-Z Single model
Training Data
(80% Randomly Selected)
Test Data
(What is not in the training data)
Individual Character Data Sets
'A'
Testing data only for the letter 'A' 
 (80% Randomly Selected)
Training Data only for the letter 'A'
Create, train, and test A-Z Model
Single Network Model
Document the results of 5 separate hyperparameter configurations with results
Each hyperparameter configuration needs to be run 100x(number of examples in the test data)
If you have 10 'A' test cases, you need to train for 10x10 interactions
Create, train, and test 5 individual 'A' - 'Z' Models
Randomly choose 5 characters between. 'A' and 'Z' 
For each character 
Document the results of 5 separate hyperparameter configurations with results
Each hyperparameter configuration needs to be run 100x(number of examples in the test data)
If you have 10 'A' test cases, you need to train for 10x10 interactions
YOU MUST USE YOUR ANN you created in Assignment 2
You are not allowed to:

Copy from anyone else's code
Copy form any online resource
Use any "ML/AI" libraries 
Vectors in C++ is fine
Use any code generation services, facilities, or people
In short, you need to do this assignment by yourself.

Time Expectations:
3 unit courses require up to 6 hours per week of non-lecture time. 

How You Will Be Graded
F 
Not handed in
Does not work as specified by this assignment
D though A Grades will be awarded individually based on the amount of effort put into the assignment represented in Github commits. A single commit of the working assignment will be investigated as cheating. 
Taking a picture of my code examples from class, then typing them in for your submission would be considered plagiarism and an F. That is why I am not releasing my code. You need to code this on your own, in your own style, in your own language of choice, in your own way.
What You Need to Submit

Your assignment MUST be submitted as a PRIVATE GitHub repository that ONLY contains this assignment. YOU MUST ADD CJARDIN as a contributor to your PRIVATE repository to receive a grade greater than an F.

Upload to canvas the following information:

Data for each run model for each of the 6 models run:
1 A-Z model + 5 single character models 
Hyperparameters used
Iterations trained
Achieved training accuracy
Observed testing accuracy
Submitted in textual or "grid" form on canvas
Your GitHub user account name
Your GitHub repository name
Due Monday April 17th by 11:59pm
 No late work will be accepted and will be given a 0.
