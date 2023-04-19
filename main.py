import requests
import json
import random
import string
import os
import time

def gmail_username_is_valid(username):
    useragents = random.choice(open("user-agents.txt").readlines())
    uas = useragents.strip()
    headers = {
        'Host': 'accounts.google.com',
        'Sec-Ch-Ua': '";Not A Brand";v="99", "Chromium";v="94"',
        'X-Same-Domain': '1',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Google-Accounts-Xsrf': '1',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': uas,
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept': '*/*',
        'Origin': 'https://accounts.google.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    params = (('hl', 'en'))
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowEntry=SignUp&flowName=GlifWebSignIn&service=mail&f.req=%5B%22AEThLlz0ie2eUdQidITxZNPKyWo9F5CHezhV4m5iJFb6Y0fXxhEeIqcqkJyzi9iLnqqM_5nbXYCjdPivsYu8GjCs3AntdmSWeazb070mWDXAAP0AxacM6X2yIOwSMsEUZ6VvUFvUJGndaMrFyvXa98xb3KEfhEQnd3JQHN0Yxqg0KKeClozPPEEh5vCwwSglfu7kDtYqZ04Zk_enDoXgzgDx_8P9fSvBkw%22%2C%22%22%2C%22%22%2C%22{username}%22%2Ctrue%2C%22S1158501710%3A1634620721349897%22%2C1%5D&azt=AFoagUX07RTYvixRfsvPo1DuUMXJvEl4bw%3A1634620721364&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22IQ%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cfalse%2C1%2C%22%22%5D'.format(username = username)
    response = requests.post('https://accounts.google.com/_/signup/webusernameavailability', headers=headers, params=params, data=data)
    response_text = response.text.splitlines()[-1]
    response_text = "".join(response_text.split())
    parsed_res = json.loads(response_text)
    isValid = True if parsed_res[0][1] == 1 else False
    sugestions = parsed_res[0][2]
    return isValid, sugestions

def random_char(num):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(num))

available_file = open('gmail.txt', 'w')

i = 0
with open("username.txt", "r") as f:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Generate gmail username from username.txt")
    qty = input("How many: ")
    print(" ")

    for j in range(int(qty)):
        username = f.readline().strip()
        if not username:
            print("\nDone! All usernames have been processed.")
            break

        isValid, sugestions = gmail_username_is_valid(username)

        if isValid == True:
            stats = "\033[1;32;40mAvailable\033[0m"
            print(username, file=available_file)
            i += 1
        else:
            stats = "\033[1;35;40mUnavailable\033[0m"

        print(f"{j+1}| {username}@gmail.com:  {stats}")
        time.sleep(10)
print(f"\n{i} usernames were processed and saved in gmail.txt")
