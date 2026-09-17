import ast 

def true_false_check(test_check, vars):
    if eval(test_check[0][-1].strip(),vars) == bool(test_check[1][0]):
        print("Correct!")
    else:
        print("Whoops, there's a mistake.")
        return
    
def float_check(test_check, vars):
    if eval(test_check[0][-1].strip(),vars) == float(test_check[1][0]):
        print("Correct!")
    else:
        print("whoops, try again.")
        return

def table_check(test_check, vars):
    if str(eval(test_check[0][-1].strip(),vars)) == test_check[1].join("\n"):
        print("Correct!")
    else:
        print("whoops, try again.")
        return

def grade_question(question, vars):
    with open("/content/data_science_grader/tests.txt", "r") as tests: 
        for test in tests.readlines():
            test = ast.literal_eval(test)
            identifier = test[0].split('-')
            if identifier[0] == vars['assignment'] and identifier[1] == question:
                test_check = test[1]
                if len(test_check[0]) > 1:
                    for code in test_check[0]:
                        exec(code, vars)
                    if len(test_check[1]) > 1:
                        table_check(test_check, vars)
                    elif "True" in test_check[1][0] or "False" in test_check[1][0]:
                        true_false_check(test_check, vars)
                    else:
                        float_check(test_check, vars)
                elif len(test_check[1]) > 1:
                    table_check(test_check, vars)
                elif "True" in test_check[1][0] or "False" in test_check[1][0]:
                    true_false_check(test_check, vars)
                else:
                    float_check(test_check, vars)
