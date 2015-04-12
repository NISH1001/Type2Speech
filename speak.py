import subprocess
import re

offensive_word = ['shit', 'fuck', 'f**k', 's**t', 'nigga']

class Espeak(object):
    def __init__(self, input_text):
        self.text = self.Validate(input_text)
        self.command = "espeak '%s' " % self.text

    def ExecuteCommand(self):
        p = subprocess.Popen(self.command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        return output

    def Validate(self, text):
        words = re.split(r'\s', text)
        for word in words:
            if word in offensive_word:
                return "i find '%s' very offensive"%word
        return text



def executeUnix(inputcommand):
    p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    return output

def main():
    input_text = input("Enter your shit here : ")
    espeak = Espeak(input_text)
    print(espeak.text)
    espeak.ExecuteCommand()

if __name__=="__main__":
    main()
