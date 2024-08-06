import json
with open("ques.json", 'r') as file:
    content = file.read()

data = json.loads(content)
score = 0
for ques in data:
    print(ques["question"])
    for index, alternative in enumerate(ques["alternatives"]):
      print(index+1, "-", alternative)
    userchoice = int(input("enter your answer:"))
    ques["useranswer"] = userchoice
    if ques["useranswer"] == ques["answer"]:
        score = score + 1
print(score, "/", len(data))



