import csv
import Deck
import pandas as pd
from os.path import exists
from datetime import datetime
reference = {'royal flush': 0.00000154, 
             'straight flush': .0000139, 
             'four of a kind': .0002401, 
             'full house': .001441, 
             'flush': .003925, 
             'straight': .003925, 
             'three of a kind': .021128, 
             'two pairs': .047539, 
             'pair': .422569, 
             'high card': .501177
             }

# Averages each trials and calculates the percent difference from the theroretical values
# returns dictionary with hands as keys and percentage as values
def run(draws):
    print("Running...")
    results = {}
    for x in range(draws):
        d = Deck.Deck()
        d.shuffle()
        hand = d.deal()
        if hand in results:
            results[hand] += 1
        else:
            results[hand] = 1
    print("Done!")
    return results

                    
def print_percentage(ratio):
    l = ['royal flush', 'straight flush', 'four of a kind', 'full house', 'flush', 'straight', 'three of a kind', 'two pairs', 'pair', 'high card']
    s = ""
    for x in l:
        print(x.upper() + ": " + f"{ratio[x]:.6%}")
        s += (x.upper() + ": " + f"{ratio[x]:.6%}\n")
    print()
    return s


# saves the run's average percent difference data into data as a csv
# ordered: date and start time, runtime, number of trials, number of draws per trial, royal flush, straight flush, four of a kind, full house, flush, straight, three of a kind, two pairs, pair, high card
# WIP
# def parse(start, runtime, percentDiff):

#     with open('data.txt', 'a') as f:
#         writer = csv.writer(f)

#         f.write(start + ",")
#         f.write()
#         f.write(percentDiff)
#         f.write("\n")
#         f.close()

def main():
    name = input("Enter your name: ")
    while name == "":
        name = input("Name cannot be empty. Enter your name: ")
    print("press 'q' to exit and save data\n*Warning! pressing Ctrl+C will not save data*\n")

    data = []
    while True: 
        draws = input("Enter the number of draws in range of 1 - 10 (millions): ")

        if(draws == "q"):
            break
        
        try: 
            int(draws)
            isInt = True
        except ValueError:
            isInt = False

        while (not isInt) or int(draws) < 1 or int(draws) > 10:
            draws = input("Invalid number of draws, enter in range of 1 - 10 (millions): ")
            try: 
                int(draws)
                isInt = True
            except ValueError:
                isInt = False
        
        draws =  int(draws) * 100

        start = datetime.now()
        temp = run(draws)
        print("Total Runtime: " + str(datetime.now()-start))

        temp['draws'] = draws
        data.append(temp)


    df = pd.DataFrame.from_dict(data)
    df.to_csv('./data/'+name+'.csv', mode='a', index=False, header=False)
    print(df)

if __name__ == "__main__":
    main()
