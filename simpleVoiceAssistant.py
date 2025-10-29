# here i am importing pyttsx3
import pyttsx3

# here looping starts for chat bot
while True:

    # here i am storing pyttsx3.init() as variable friend
    friend = pyttsx3.init()

# here is the user input qustion
    user_input_question = input("What do you want to know? Type here: ")

# here is the answer for invalid question
    invalid_question_answer = "will you repeat again. i have not got it"

# here is the first greating
    greating01 = ("hello")
    greating01reply = ("hey there")

# here is the first qna
    question01 = "who are you"
    question01reply = "i am a simple bot created by ibrahim mustafa opu"

# here is the first qna
    ending01 = "bye"
    ending01reply = "bye. meet you again"

# here is the function for qna
    if user_input_question == greating01:
        print(greating01reply)
        friend.say(greating01reply)
    elif user_input_question == question01:
        print(question01reply)
        friend.say(question01reply)
    elif user_input_question == ending01:
        print(ending01reply)
        friend.say(ending01reply)
    else:
        print(invalid_question_answer)
        friend.say(invalid_question_answer)

# here i am returning variable friend
    friend.runAndWait()

# here is the user permission for the next qna
    user_permission_for_next_qna = input(
        "do you have any other question? (yes/no) ")
    if user_permission_for_next_qna == "yes":
        continue
    elif user_permission_for_next_qna == "no":
        break
    else:
        friend.say("invalid input. returning to the qna section")

# here i am returning variable friend
    friend.runAndWait()
