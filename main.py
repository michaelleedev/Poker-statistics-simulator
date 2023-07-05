import csv
import Deck
from os.path import exists
from datetime import datetime

# function that handles the trial of the experiment. 
# takes in user inputed number of draws for each trial
# returns dictionary with hands as keys and percentage as values
def trial(draws):
    results = {}
    for x in range(draws):
        d = Deck.Deck()
        d.shuffle()
        hand = d.deal()
        if hand in results:
            results[hand] += 1
        else:
            results[hand] = 1

    ratio = {}
    for x in results:
        ratio[x] = results[x]/draws
    return ratio

# Averages each trials and calculates the percent difference from the theroretical values
# returns dictionary with hands as keys and percentage as values
def run(trials, draws):
    total = {'royal flush': 0, 'straight flush': 0, 'four of a kind': 0, 'full house': 0, 'flush': 0, 
        'straight': 0, 'three of a kind': 0, 'two pairs': 0, 'pair': 0, 'high card': 0}

    n = 1
    for x in range(trials):
        print("Runinng trial: " + str(n) + "...")
        t = trial(draws)
        for x in t:
            total[x] += t[x]
        n += 1
        print("done!")

    average = {} #decimals
    for x in total:
        average[x] = total[x]/trials

    diff = {}
    reference = {'royal flush': 0.00000154, 'straight flush': .0000139, 'four of a kind': .0002401, 'full house': .001441, 'flush': .003925, 
        'straight': .003925, 'three of a kind': .021128, 'two pairs': .047539, 'pair': .422569, 'high card': .501177}
    for x in reference:
        diff[x] = average[x] - reference[x]

    print("Total average percentage:")
    print_percentage(average)
    print("Average percentage difference: ")
    data = print_percentage(diff)

    return diff
                    
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
    
    draws = input("Number of draws per trial (press 'enter' for default value of 1,000,000): ")
    if draws == "":
        draws = 1000000
    else:
        draws = int(draws)

    trials = input("Number of trials (press 'enter' for default value of 3): ")
    if trials == "":
        trials = 3
    else:
        trials = int(trials)

    print(str(draws) + " draws per trial for " + str(trials) + " trials.")

    start = datetime.now()
    data = run(trials, draws)

    print("Total Runtime: " + str(datetime.now()-start))

if __name__ == "__main__":
    main()
