import configparser
import requests

class HKBU_ChatGPT():

    def __init__(self, config_path = './config.ini'):
        # if type(config_path) == str:
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        # elif type(self.config) == configparser.ConfigParser:
        #     self.config = config_path

    def submit(self,message):
        print(self.config['CHATGPT']['MODELNAME'])
        conversation = [{"role": "user", "content": message}]
        url = (self.config['CHATGPT']['BASICURL']) + "/deployments/" + (self.config['CHATGPT']['MODELNAME']) + "/chat/completions/?api-version=" + (self.config['CHATGPT']['APIVERSION'])
        headers = { 'Content-Type': 'application/json', 'api-key': (self.config['CHATGPT']['ACCESS_TOKEN']) }
        payload = { 'messages': conversation }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            print(response.text)
            return 'Error:', response
if __name__ == '__main__':
    ChatGPT_test = HKBU_ChatGPT()
    while True:
        user_input = input("Typing anything to ChatGPT:\t")
        response = ChatGPT_test.submit(user_input)
        print(response)