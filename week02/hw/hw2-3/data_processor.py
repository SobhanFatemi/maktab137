import csv

def process_and_save(users_data, output_path):
    users_data_processed = []

    for user in users_data:
        if user["completed"] == True and user["userId"] == 5:
            users_data_processed.append(user)

    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "userId", "title"]) 
        for user in users_data_processed:
            writer.writerow([user["id"], user["userId"], user["title"]])
