import requests

url = "http://localhost"  # nginx url

while True:
    number = input("Input Number: ")

    # checking if number consists of digits and doesn't begin with 0 (if it's not 0 itself)
    if number.isdigit() and (len(number) == 1 or len(number) > 1 and number[0] != '0'):
        
        # forming json string and posting it
        post_json = '{"number":"' + str(number) + '"}'
        req = requests.post(url, json=post_json)

        # printing obtained data
        print(req.status_code)
        print(req.json())
    else:
        print("Error: Input a valid number")
