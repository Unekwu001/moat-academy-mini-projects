result = {"Ayo":34,"Kunle":35,"Daniel":30,"Ema":29,"Mike":19,"Ada":37}

def check_result(name):
    if name in result.keys():
        for a,b in result.items():
            if a == name:
                print(f"{name}, your score is {b}")
    else:
        print('Name not found')
