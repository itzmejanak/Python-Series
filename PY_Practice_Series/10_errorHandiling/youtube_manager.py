import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(vedios):
    with open('youtube.txt', 'w') as file:
        json.dump(vedios, file)


def list_all_vedios(vedios):
    print("\n")
    print("*"*70)
    for index, video in enumerate(vedios, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")


def add_vedio(vedios):  
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    vedios.append({'name': name, 'time': time})
    save_data_helper(vedios)


def update_vedio(vedios):  
    list_all_vedios(vedios)
    index = input("Enter the number vedio to update")
    if 1<= 1<= len(vedios):
        name = input("Enter video name: ")
        time = input("Enter video time: ") 
        vedios[index-1] = {'name': name, 'time': time}
        save_data_helper(vedios)
    else:
        print("invalid index")



def delete_vedio(vedios): 
    list_all_vedios(vedios)
    index = int(input("Enter the video number to be deleted"))
    
    if 1 <= index <= len(vedios):
        del vedios[index-1]
        save_data_helper(vedios)
    else:
        print("Invalid video index selected")



def main():
    vedios = load_data()

    while True:
        print("\nYouTube manager for Python project")
        print("\t1. List all Favourite videos")
        print("\t2. Add a YouTube video")
        print("\t3. Update a YouTube video details")
        print("\t4. Delete a YouTube video")
        print("\t5. Exit YouTube")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_vedios(vedios)
        elif choice == '2':
            add_vedio(vedios)
        elif choice == '3':
            update_vedio(vedios)
        elif choice == '4':
            delete_vedio(vedios)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
