class invalid_option_error(Exception):
    pass
class Quiz:
    def __init__(self):
        self.ques=["1.which is the Largest country?\nA.India\nB.Canada\nC.Russia","2.5+3=?\nA.4\nB.8\nC.10"]
        self.ans=["C","B"]
        self.score=0
    def start_quiz(self):
        for i in range (len(self.ques)):
            try:
                print(self.ques[i])
                user_ans=input("Enter option(A/B/C):")
                if user_ans not in ["A","B","C"]:
                    raise invalid_option_error("Invalid option")
                if user_ans==self.ans[i]:
                    self.score+=1
            except invalid_option_error as e:
                print(e)
    def display_score(self):
        print("Final score",self.score)
q=Quiz()
q.start_quiz()
q.display_score()
