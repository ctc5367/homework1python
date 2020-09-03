# Author: Cole Carter ctc5367@psu.edu

course1letter = input("Enter your course 1 letter grade: ");
course1credit = input(" Enter your course 1 credit: ");
course1credit = float(course1credit);

if course1letter == "A" or course1letter == "a":
  gp1 = float (4.0);
  print(" Grade point for course 1 is: 4.0");
elif course1letter == "A-" or course1letter == "a-":
  gp1 = float (3.67);
  print(" Grade point for course 1 is: 3.67");
elif course1letter == "B+" or course1letter == "b+":
  gp1 = float (3.33);
  print(" Grade point for course 1 is: 3.33");
elif course1letter == "B" or course1letter == "b":
  gp1 = float (3.0);
  print(" Grade point for course 1 is: 3.0");
elif course1letter == "B-" or course1letter == "b-":
  gp1 = float (2.67);
  print(" Grade point for course 1 is: 2.67");
elif course1letter == "C+" or course1letter == "c+":
  gp1 = float (2.33);
  print(" Grade point for course 1 is: 2.33");
elif course1letter == "C" or course1letter == "c":
  gp1 = float (2.0);
  print(" Grade point for course 1 is: 2.0");
elif course1letter == "D" or course1letter == "d":
  gp1 = float (1.0);
  print(" Grade point for course 1 is: 1.0");
else:
  gp1 = float (0.0);
  print(" Grade point for course 1 is: 0.0");

course2letter = input(" Enter your course 2 letter grade:");
course2credit = input(" Enter your course 2 credit:");
course2credit = float (course2credit);

if course2letter == "A" or course2letter == "a":
  gp2 = float (4.0);
  print(" Grade point for course 2 is: 4.0");
elif course2letter == "A-" or course2letter == "a-":
  gp2 = float (3.67);
  print(" Grade point for course 2 is: 3.67");
elif course2letter == "B+" or course2letter == "b+":
  gp2 = float (3.33);
  print(" Grade point for course 2 is: 3.33");
elif course2letter == "B" or course2letter == "b":
  gp2 = float (3.0);
  print(" Grade point for course 2 is: 3.0");
elif course2letter == "B-" or course2letter == "b-":
  gp2 = float (2.67);
  print(" Grade point for course 2 is: 2.67");
elif course2letter == "C+" or course2letter == "c+":
  gp2 = float (2.33);
  print(" Grade point for course 2 is: 2.33");
elif course2letter == "C" or course2letter == "c":
  gp2 = float (2.0);
  print(" Grade point for course 2 is: 2.0");
elif course2letter == "D" or course2letter == "d":
  gp2 = float (1.0);
  print(" Grade point for course 2 is: 1.0");
else:
  gp2 = float (0.0);
  print(" Grade point for course 2 is: 0.0");

course3letter = input(" Enter your course 3 letter grade:");
course3credit = input(" Enter your course 3 credit:");
course3credit = float (course3credit);

if course3letter == "A" or course3letter == "a":
  gp3 = float (4.0);
  print(" Grade point for course 3 is: 4.0");
elif course3letter == "A-" or course3letter == "a-":
  gp3 = float (3.67);
  print(" Grade point for course 3 is: 3.67");
elif course3letter == "B+" or course3letter == "b+":
  gp3 = float (3.33);
  print(" Grade point for course 3 is: 3.33");
elif course3letter == "B" or course3letter == "b":
  gp3 = float (3.0);
  print(" Grade point for course 3 is: 3.0");
elif course3letter == "B-" or course3letter == "b-":
  gp3 = float (2.67);
  print(" Grade point for course 3 is: 2.67");
elif course3letter == "C+" or course3letter == "c+":
  gp3 = float (2.33);
  print(" Grade point for course 3 is: 2.33");
elif course3letter == "C" or course3letter == "c":
  gp3 = float (2.0);
  print(" Grade point for course 3 is: 2.0");
elif course3letter == "D" or course3letter == "d":
  gp3 = float (1.0);
  print(" Grade point for course 3 is: 1.0");
else:
  gp3 = float (0.0);
  print(" Grade point for course 3 is: 0.0");

gpa = float ((gp1*course1credit+ gp2*course2credit+ gp3*course3credit)/(course1credit+course2credit+course3credit));

print(f"Your GPA is: {gpa}");