import requests
import time

def load_potential_codes(filename):
    codes = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            # Skip comments and blank lines
            if line and not line.startswith('#'):
                codes.append(line)
    return codes

url = "https://codes.thisisnotawebsitedotcom.com/"

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

def log_result(code, status):
    with open('code_results.log', 'a') as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Code: {code}, Status: {status}\n")

def check_code(code):
    files = {
        'code': (None, code),
    }
    try:
        response = requests.post(url, headers=headers, files=files)
        if response.status_code == 200:
            log_result(code, "Valid")
            print(f"Code {code}: Valid")
            print(response.text)
            if code == 'stan':
                with open("stan.txt", 'w', encoding='utf-8') as f:
                    f.write(response.text)
        elif response.status_code == 404:
            log_result(code, "Not Found")
            print(f"Code {code}: Not Found")
        elif response.status_code == 429:
            log_result(code, "Rate Limited - Retrying")
            print(f"Rate limit hit. Waiting to retry...")
            time.sleep(30)
            return check_code(code)
        else:
            log_result(code, f"Unexpected Status: {response.status_code}")
            print(f"Code {code}: Unexpected status {response.status_code}")
    except requests.RequestException as e:
        log_result(code, f"Error: {str(e)}")
        print(f"Code {code}: Error {str(e)}")


def check_all_codes(codes):
    for code in codes:
        check_code(code.lower())
        time.sleep(1)

if __name__ == "__main__":
    potential_codes = load_potential_codes('possible_codes.txt')
    check_all_codes(potential_codes)
