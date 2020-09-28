# yes, this is basically the sample question but i'm currently remodelling it.
# closing the tab of the code of which i was working on was not the best choice.

print("Title of program: MCQ revision program")
print()

question = 0
totalQn = 3
score = 0



if question == 0:
  
  print("Question "+str(question+1)+") "+ "If the base and height of a triangle is 3 and 6 respectively, what is the area of the triangle?")
  print("   a) 6")
  print("   b) 18")
  print("   c) 9")
  print("   d) 8")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Try to recall the formula for the area of a triangle."
  elif answer == "b":
    output = "Wrong. Remember to multiply it by half."
  elif answer == "c":
    output = "Yes, that's right!"
    score +=1
  elif answer == "d":
    output = "Wrong. I don't even know how you got this answer."
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(score) + "/" str(totalQn))
  print()
  print()
  


question += 1

if question == 1:
  
  print("Question "+str(question + 1)+") "+ "What does 'amiable' mean?")
  print("   a) friendly and pleasant")
  print("   b) shiningly brilliant and clever")
  print("   c) harmful and evil")
  print("   d) fear and anxiety")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    score +=1
  elif answer == "b":
    output = "Wrong. That is the definition for 'scintillating'."
  elif answer == "c":
    output = "Wrong. Clearly the number 2 in the formulae must mean something?"
  elif answer == "d":
    output = "Wrong. What's the difference between a molecule and an atom?"
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Which represents the electronic configuration of a non-metal?")
  print("   a) 2,1")
  print("   b) 2,8,3")
  print("   c) 2,8,8,2")
  print("   d) 2,7")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Think again - how many electron shells are filled, and which group is this in?"
    score -=1
  elif answer == "b":
    output = "Wrong.  Think again - how many electron shells are filled, and which group is this in?"
    score -=1
  elif answer == "c":
    output = "Wrong.  Think again - how many electron shells are filled, and which group is this in?"
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz!")
  
