result = {"Ayo":34,"Kunle":35,"Daniel":30,"Ema":29,"Mike":19,"Ada":37}

def check_result():
    print("{:<13} {:<13}".format('Names','Scores'))
    for x,y in result.items():
        print("{:<15} {:<15}".format(x,y))



