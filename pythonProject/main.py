print("Quiz System(Demo) developed by Sourav Ghosh")

print()

print("Enter your name")
name = input()
print("Name:",name)

print()

print("Enter Roll No")
Enter_Roll_No = int(input())
print("Roll:",Enter_Roll_No)

print()

i = 0

print("""Q-1) What is the  full form of A.C.?
    a) Alternating current b) Direct current c) none of this""")
answer_1 = input("Answer: ")
if answer_1 == "a" or answer_1 == "A":
    print("Your answer 1 is Correct")
    i = i + 1
else:
    print("You have enter a wrong answer")

print()

print("""Q-2) Who invented computer?
    a) Charles Babbage b) Larry Page c) Sergey Brin d) Mark Zuckerberg""")
answer_1 = input("Answer: ")
if answer_1 == "a" or answer_1 == "A":
    print("Your answer 2 is Correct")
    i = i + 1
else:
    print("You have enter a wrong answer")

print()

print("""Q-3) What is he full form of NASA?
    a) Indian Space Research Organisation b) National Aeronautics and Space Administration c) none of this """)
answer_1 = input("Answer: ")
if answer_1 == "b" or answer_1 == "B":
    print("Your answer 3 is Correct")
    i = i + 1
else:
    print("You have enter a wrong answer")

print()

print("""Q-4) What is he full form of ISRO?
    a) Japan Aerospace Exploration Agency b) National Aeronautics and Space Administration c) Indian Space Research Organisation """)
answer_1 = input("Answer: ")
if answer_1 == "c" or answer_1 == "C":
    print("Your answer 4 is Correct")
    i = i + 1
else:
    print("You have enter a wrong answer")

print()

print("Your score is ", i)
print("Name -", name,"Roll No.:", Enter_Roll_No, "Score:",)