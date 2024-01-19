import csv
programming = [["Python", "cop1000", 3],

               ["Java", "cop1020", 3],

               ["HTML5", "cop1040", 3]]
with open('prog.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(programming)