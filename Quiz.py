#Write a quiz program that asks the user a multiple-choice question. After the user answers the question, the program
# should display either "correct" or "incorrect".
# Modify your program to include three questions instead of one.
# Modify your program again to include a message at the end of the quiz that tells the user how many
# questions were answered correctly.

question_1 = input("What is the capital of United Kingdom? Options, London, Paris, Madrid, Stockholm")
if question_1 == "London" or question_1 == "london":
     print("1 point")
     score_1 = 1
else:
    print("0 points")
    score_1 = 0
question_2 = input("What is the most common currency in Europe? Options, Euro, Pound, Krone, Zloty")
if question_2 == "Euro" or question_2 == "euro":
    print("1 point")
    score_2 = 1
else:
    print("0 points")
    score_2 = 0
question_3 = input("Which country won the World Cup in 1966? Options Brazil, England, France, Spain")
if question_3 == "England" or question_3 == "england":
   print("1 point")
   score_3 = 1
else:
    print("0 points")
    score_3 = 0
total_score = score_1 + score_2 + score_3
print("Score is:", total_score, "/3")


Question_1 = input("Q1: What is the capital of the United Kingdom. Options London, Paris, Washington, or Madrid?")
if Question_1 == "London" or Question_1 == "london":
    print("1 point")
    score_1 = 1
else:
    print("0 points")
    score_1 = 0
Question_2 = input("Q2: What is the most widely used currency in the European continent? Pound, Euro, Dollar, or Rand?")
if Question_2 == "Euro" or Question_2=="euro":
    print("1 point")
    score_2 = 1
else:
    print("0 points")
    score_2 = 0
Question_3 = input("Q3: Which country won the football world champion in 1966? Options: England, Germany, Spain, Portugal? ")
if Question_3 == "England" or Question_3 == "england":
    print("1 point")
    score_3 = 1
else:
    print("0 points")
    score_3 = 0
Question_4 = input("Q4: Which country won the European championships in 2016? Options: England, Portugal, France, Italy?")
if Question_4 == "Portugal" or Question_4 == "portugal":
    print("1 point")
    score_4 = 1
else:
    print("0 points")
    score_4 = 0
print(score_1+score_2+score_3+score_4,"/4")



