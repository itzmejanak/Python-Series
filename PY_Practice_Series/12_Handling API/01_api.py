import requests
def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user = data["data"]
        username= user["login"]["username"]
        contry = user["location"]["country"]
        return username, contry
    else:
        raise Exception("faild to fetch user data")
    
def main():
    try:
        username, country = fetch_random_user()
        print(f"\tUsername: {username} \n \tCountry: {country}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()