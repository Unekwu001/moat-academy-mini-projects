results = {
            "Bola Tinubu":[0, 200, 120, 0, 450, 670 ],
            "Yemi Osinbajo":[0,0, 0,56, 10,0],
            "Rochas Okorocha":[0,0,0,0,0,0],
            "Rotimi Amaechi":[20,13,2,1,29,0]
           }

#---------------------------------------------------------------------------------

combined_results = {candidate:sum(votes) for candidate,votes in results.items()}
b = []
for x,y in combined_results.items():
    b.append(y)
    if max(b) == y:
        print(f"{x} won the election with {y} votes")
#--------------------------------------------------------------------------------


























