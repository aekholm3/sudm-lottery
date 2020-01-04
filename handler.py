import csv
import random as rand

ATTENDEES_FILE = 'attendees_20191109.csv'
RAFFLE_TICKES_FILE = 'raffle.csv'
FIRST_NAME_COLUMN = 2
LAST_NAME_COL = 3
TOTAL_RAISED_COL = 13
LINE_ZERO_SIGNIFIER= 'transId'

def handler():
    num_tickets = []
    with open(ATTENDEES_FILE) as attendees_file:
        attendees_file_reader = csv.reader(attendees_file)
        for line in attendees_file_reader:
            if line[0] == LINE_ZERO_SIGNIFIER:
                continue
            name = line[FIRST_NAME_COLUMN] + ' ' + line[LAST_NAME_COL]
            individual_tickets = int(float(line[TOTAL_RAISED_COL])) // 10
            num_tickets.extend([name] * individual_tickets)
    return num_tickets

if __name__ == '__main__':
    tickets = handler()
    print(rand.choice(tickets))
