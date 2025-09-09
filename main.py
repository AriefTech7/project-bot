start_bot = True
chatbot = "bot: "

while start_bot:
    user = input("user: ").lower()
    if user == "hello":
        print("{}hai juga".format(chatbot))
    elif user == "bye":
        print("{}sampai jumpa".format(chatbot))
        start_bot = False
    else:
        print("{}saya tidak mengerti".format(chatbot))