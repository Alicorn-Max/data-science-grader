import ast 

seconds_in_a_decade = 315532800
def grade_question(question):
    with open("tests.txt", "r") as tests:
        for test in tests.readlines():
            test = ast.literal_eval(test)
            if test[0] == question:
                test_check = test[1]
                if "true"  in test_check[1] or "false" in test_check[1]:
                    if eval(test_check[0].strip(),globals()) == bool(test_check[1].replace("true","True").replace("false","False")):
                        print("You passed :)")
                    else:
                        print("whoops, try again!")
                else:
                    if eval(test_check[0].strip(),globals()) == int(test_check[1]):
                        print("You passed :)")
                    else:
                        print("whoops, try again!")


grade_question("q3_1_2")