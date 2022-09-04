import sys
import pickle
import re
from person_class import Person

def file_processing (path):
    persons_dict = {}

    with open(path) as file:
        # Get rid of the first line which is just the heading line
        lines = file.read().splitlines()[1:]
        for line in lines:
            # Split on comma to get the feilds as text variables
            last, first, mi, id, phone = line.split(',')

            # Modify last name and first name to be in Capital Case, if necessary
            if not last.isupper():
                last = last.upper()
            if not first.isupper():
                first = first.upper()

            # Modify middle initial to be a single upper case letter, if necessary. Use ‘X’ as a middle initial if one is missing.
            if not mi:
                mi = 'X'
            elif not mi.isupper():
                mi = mi.upper()

            # Modify id using regex
            id_regex = re.search('[a-zA-Z]{2}\d{4}', id)
            if not id_regex:
                print('ID invalid:', id)
                print('ID is two letters followed by 4 digits')
                id = input('Please enter a valid id: ')

            # Modify phone using regex
            phone_regex = re.search('^\d{3}-\d{3}-\d{4}$', id)
            if not phone_regex == 0:
                print('Phone ', phone, ' is invalid')
                print('Enter phone number in form 123-456-7890')
                phone = input('Enter phone number: ')

            # Create a person object
            person = Person(last, first, mi, id, phone)

            # Add the person object to the persons dict by the id
            if person.id in persons_dict.keys():
                print('ERROR: duplicate id')
            else:
                persons_dict[person.id] = person

    return persons_dict

if __name__ == '__main__':
    # Path error hanlding
    if len(sys.argv) == 1:
        print('Error, no path specified')
        exit(0)
    else:
        path = sys.argv[1]
        # Save persons dict as pickle file
        persons_dict = file_processing(path)
        with open('persons.pickle', 'wb') as handle:
            pickle.dump(persons_dict, handle)

        # Load pickled persons data
        with open('persons.pickle', 'rb') as handle:
            persons_unpickled = pickle.load(handle)

            # Display the people
            print('Employee list:')
            for id in persons_unpickled.keys():
                persons_unpickled[id].display()
