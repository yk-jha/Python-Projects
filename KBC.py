print("WELCOME TO KBC GAME")
print("15 QUESTION WILL BE THERE NO LIFELINES AND YOU CAN QUIT ANYTIME")
print("LET'S PLAY")
questions = [
    [
        "who gives the Python language:", "dennis ritchie", "guido van rossum", "Anders hejsberg", "james gosling", 2
    ], [
        "In which year Python was created", "2001", "1991", "1998", "1990", 4
    ], [

        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ], [
        "what is #define in coding", "pre-procesor", "variable", "constant", "data type", 1
    ], [
        "what is time complexity of selection sorting", "O(n)", "O(1)", "O(n^2)", "none", 3
    ], [
        "what is name of this operator %", "modulo", "addition", "percentage", "division", 1
    ], [
        "how much bytes double data type stores", "4", "1", "2", "8", 4
    ], [
        "whwn PEP8 introduced in Python", "2001", "2005", "1990", "1991", 1
    ], [
        "secondary memory is also known as", "storage memory", "external memory", "only b", "both a and b ", 1
    ], [
        "which special character is use for comments in Python", "@", "$", "%", "#", 4
    ], [
        "which special character is use for comments in C", "/", "?", "()", "\\", 4
    ], [
        "which of them is use to relocate execution program to the main memory during exexcution", "linker", "compiler", "interpreter", "loader", 4
    ], [
        "who is prime minister  of India", "amit shah", "mai", "modi ji", "dhoni", 3
    ], [
        "full form of RAM", "radnom acsess memory", "roll arm memory", "none", "all", 1
    ], [
        "who is winner of IPL 2022", "GT", "CSK", "RCB", "RR", 1
    ]
]
level = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000,
         320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]
money = 0
for i in range(0, len(questions)):

    question = questions[i]
    print(f"\n\nQuestion for Rs. {level[i]}")
    print(f"{question[0]}")
    print(f"a. {question[1]}          b. {question[2]} ")
    print(f"c. {question[3]}          d. {question[4]} ")
    reply = int(input("Enter your answer (1-4) or  0 to quit:\n"))
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {level[i]}")
        if (reply == 0):
            print("THANK YOU FOR PLAYING")
            break
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 70000000
    else:
        print("Wrong answer!")
        break


print(f"Your take home money is {money}")
