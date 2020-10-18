from sys import argv
from csv import DictReader

if len(argv) != 3:
    print("Usage: ordered_dict.py csv file")
    exit(1)

csv_file = open(argv[1]) # open csv file
reader = DictReader(csv_file) # use DictReader to make a list of the dictionary
f = open(argv[2], 'r')

temp_person = None

# iterate through all dictionaries in list
for dic in reader:

    # iterate through all pairs of keys and values in each dictionary
    for key, value in dic.items():

        # if we reach a name and we don't have a person that passes the tests, then set temp_person to new person
        if (key == 'name' and temp_person == None):
            temp_person = value

        # we are at a DNA sequence
        elif (key != 'name'):
            dna_str = key * int(value) # create a Short Tandem Repeat of DNA of individual
            false_str = key * (int(value) + 1) # a test to see if the STR found is actually longer
            
            # if dna_str is in f.read(), check to see if false_str is in there, too
            if dna_str in f.read():
                f.seek(0) # go to beginning of file to go through it

                # if false_str is in, then this does not belong to person
                if false_str in f.read():
                    temp_person = None
                
                f.seek(0)   # go to beginning of file

            # else, if dna_str is not in f.read, then this is not the person and go back to beginning of file
            else:
                temp_person = None
                f.seek(0)
        
    # outside of loop, if temp_person passed all tests, then that is the person
    if (temp_person != None):
        print(temp_person)

f.close() # close file to avoid memory leakage
