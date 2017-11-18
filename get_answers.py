def get_answer(question,answer):
	question=question.lower()
	return answer[question]
answer={"привет":"И тебе привет!", "как дела":"Лучше всех", "пока":"Увидимся"}
question=input('привет? ')
print(get_answer(question,answer)) 