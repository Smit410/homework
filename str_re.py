class reverse:
    def __init__(self, text=""):
        self.text = text

    def reverse_string(self):
        reversed_str = ""
        for char in self.text:
            reversed_str = char + reversed_str
        return reversed_str


user_input = input("Enter a word: ")
string_reverser = reverse(user_input)
result = string_reverser.reverse_string()
print("Reversed string:", result)
