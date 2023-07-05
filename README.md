# About
In this project, I explored the accuracy of the Python's Random function with the use of it's shuffle function. 

This project creates a Deck class that has list of 52 Card classes which represents each of the card in traditional playing card deck. I used `random.shuffle()` method to randomly organize the deck list and picked first five cards of the list as the poker hand. 

This shuffle occurred for every trial, which user specified how many or defaulted to 3. Each trial had user specified number of draws or default draw amount of million. There is no specific reason to making the default for trial and draws to 3 and 1,000,000 respectively except that I noticed a million draws for each trial produced royal flushes frequently. 

Each trial produced a dictionary of each poker hands with their respective odds (percentage) from the total draws. Dictionaries from each trial is averaged out and finally calculated against the theoretical odds (percentage) for each respective hand.

The project prints out each of the trial numbers as it calculates, and total average and average difference at the end along with total runtime. Each trial of 1,000,000 draws ran about 23 seconds on my machine, and the default values came out to a total of about a minute and 15 seconds. 

# Usage
in console, run `py main.py` and follow input instructions

# Work in progress
I am planning on exporting each trial results to a csv file as a deviation to the theoretical odds. This may require handling each trials differently and write a separate function that handles each trials and write to csv. The total average difference will still be printed out, but not saved in the csv file

# References

Referenced https://www.youtube.com/channel/UCCjnRY0aATv0jm0res8zuUQ for deck building

Reference https://en.wikipedia.org/wiki/Poker_probability 
