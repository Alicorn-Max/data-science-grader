import ast 

def true_false_check(test_check, vars):
    if eval(test_check[0].strip(),vars) == bool(test_check[1].replace("true","True").replace("false","False")):
        print("Correct!")
    else:
        print("Whoops, there's a mistake.")
        print(test_check[0])
        return
    
def float_check(test_check, vars):
    if eval(test_check[0].strip(),vars) == float(test_check[1]):
        print("Correct!")
    else:
        print("whoops, try again.")
        print(test_check[0])
        return


def grade_question(question, vars):
    with open("/content/data_science_grader/tests.txt", "r") as tests:
        for test in tests.readlines():
            test = ast.literal_eval(test)
            if test[0] == question:
                test_check = test[1]
                if len(test_check) > 2:
                    for code in test_check[:-2]:
                        exec(code, vars)
                    if "true" in test_check[-1] or "false" in test_check[0][-1]:
                        true_false_check(test_check[-2:], vars)
                    else:
                        float_check(test_check[-2:], vars)
                elif "true"  in test_check[1] or "false" in test_check[1]:
                    true_false_check(test_check, vars)
                else:
                    float_check(test_check, vars)
                        
