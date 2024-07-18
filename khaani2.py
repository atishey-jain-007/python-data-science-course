kahani =""
while True:
    data = input('enter a story=>')
    if len(data) == 0:
        print("the end")
        break
    kahani += data + "/n"

    print("the real story:")
    print(kahani)

    with open('story.txt','w') as file:
        file.write(khaani)