import os.path
import pandas as pd

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

def main():
    name = input("Enter your name: ")
    path = "./data/" + name + ".csv"
    if os.path.isfile(path):
        colname = ['royal flush', 'straight flush', 'four of a kind', 'full house', 'flush', 'straight', 'three of a kind', 'two pairs', 'pair', 'high card','draws']
        df = pd.read_csv(path, names=colname, header=None)
        sum = df.sum()
        draws = sum["draws"]
        print("Out of " + str(draws) + " number of draws, ")
        for x in sum.keys():
            if x != "draws":
                odds = sum[x]/draws
                percentage = f"{odds:.6%}"
                difference = f"{(reference[x] - odds):.6%}"
                print(x.upper() + ": " + str(percentage) + "% | difference from theoretical: " + str(difference))
    else:
        print("no file exists with the name " + name + ". Please check the name or run simulation to populate data in ./data/" + name + ".csv.")



if __name__ == "__main__":
    main()
