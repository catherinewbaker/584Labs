# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING CODE WRITTEN BY OTHER STUDENTS OR LARGE LANGUAGE MODELS LIKE CHATGPT. Catherine Baker
#I have completed this homework without collaborating with any classmates.

def decode_cipher(text, replacements):
    # Replace each letter in the text based on the replacements dictionary
    decoded_text = ""
    for char in text:
        if char in replacements:
            decoded_text += replacements[char]
        else:
            decoded_text += char  # Leave the character as is if not in replacements
    return decoded_text

# Replacements
replacements = {'t': 'e', 'q': 'a', 'f': 'n', 'r': 'd', 'z': 't', 'i': 'h', 'l': 's', 'o': 'i', 'v': 'w', 'g': 'o', 'k': 'r', 'a': 'k', 'h': 'p', 'o': 'i', 'c': 'v', 'u': 'g', 'w': 'b', 'y': 'f', 'i': 'h', 's': 'l', 'n': 'y', 'W': 'B', 'O': 'I', 'e': 'c', 'm':'z', 'x': 'u', 'd':'m', 'I': 'H', 'b':'x'}

cipher_text = "Wsgeaeiqof ol q rtetfzkqsomtr qfr rolzkowxztr rouozqs strutk zteifgsgun ziqz tfqwstl ltexkt, zkqflhqktfz, qfr zqdhtk ktlolzqfz ktegkr atthofu gy zkqflqezogfl qekgll q ftzvgka gy egdhxztkl Oz ltkctl ql zit xfrtksnofu zteifgsgun ygk cqkogxl eknhzgexkktfeotl vozi Wozegof wtofu zit yoklz qfr dglz vtssafgvf qhhsoeqzogf Igvtctk, zit hgztfzoqs qhhsoeqzogfl gy wsgeaeiqof tbztfr yqk wtngfr eknhzgexkktfeotl odhqezofu cqkogxl ofrxlzkotl"

# Decode the cipher text
decoded_text = decode_cipher(cipher_text, replacements)

print(decoded_text)
