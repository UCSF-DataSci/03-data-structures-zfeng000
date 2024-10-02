#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
    "What we call the beginning is often the end. And to make an end is to make a beginning. The end is where we start from. ― T.S. Eliot",
    "Half the harm that is done in this world is due to people who want to feel important. They don't mean to do harm; but the harm does not interest them. Or they do not see it, or they justify it because they are absorbed in the endless struggle to think well of themselves. ― T.S. Eliot",
    "Poetry is not a turning loose of emotion, but an escape from emotion; it is not the expression of personality but an escape from personality. But, of course, only those who have personality and emotion know what it means to want to escape from these. ― T.S. Eliot",
    "For us, there is only the trying. The rest is not our business. ― T.S. Eliot",
    "I learn a great deal by merely observing you, and letting you talk as long as you please, and taking note of what you do not say. ― T.S. Eliot",
    "Only those who will risk going too far can possibly find out how far one can go. ― T.S. Eliot",
    "To do the useful thing, to say the courageous thing, to contemplate the beautiful thing: that is enough for one man's life. ― T.S. Eliot"
]

def get_quote_of_the_day(quotes):
    todays_quote = None

    today = date.today()
    random.seed(today.toordinal())
    todays_quote = random.choice(quotes)
    
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt