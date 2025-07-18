class conversation:
	def greet_user(self):
		while True :
		    self.meet_user = input("Hello, what's your name?:")
		    if not "stop" in self.meet_user :
		    	print(f"Nice to meet you {self.meet_user}!")
		    elif "stop" in self.meet_user :
		    	print("See you soon!")
		    	break

start_conversation = conversation()
start_conversation.greet_user()