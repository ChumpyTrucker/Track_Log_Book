import csv

def add_entry(track_log):
    date = input("Enter the date (YYYY-MM-DD): ")
    distance = float(input("Enter the distance (in kilometers): "))
    duration = float(input("Enter the duration (in minutes): "))
    average_speed = distance / (duration / 60)

    entry = [date, str(distance), str(duration), str(average_speed)]
    track_log.append(entry)

def save_log(track_log):
    filename = input("Enter the filename to save the logbook: ")
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(track_log)
    print("Track log book saved successfully.")

def load_log(filename):
    track_log = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            track_log = list(reader)
        print("Track log book loaded successfully.")
    except FileNotFoundError:
        print("File not found. Creating a new track log book.")
    return track_log

def display_log(track_log):
    print("Date\t\tDistance (km)\tDuration (min)\tAverage Speed (km/h)")
    for entry in track_log:
        print('\t'.join(entry))

def main():
    print("Track Log Book")
    print("1. Load log book")
    print("2. Add entry")
    print("3. Save log book")
    print("4. Display log book")
    print("5. Exit")

    track_log = []

    while True:
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            filename = input("Enter the filename to load the logbook: ")
            track_log = load_log(filename)
        elif choice == '2':
            add_entry(track_log)
        elif choice == '3':
            save_log(track_log)
        elif choice == '4':
            display_log(track_log)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()