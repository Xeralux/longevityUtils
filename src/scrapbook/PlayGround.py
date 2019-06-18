# # # Checking braces are balanced
# #
# # # Using STACK
# # '''
# # One approach to check balanced parentheses is to use stack. Each time, when an open parentheses is encountered push it
# # in the stack, and when closed parenthesis is encountered, match it with the top of stack and pop it. If stack is empty
# # at the end, return Balanced otherwise, Unbalanced.
# # '''
# #
# # # open_list = ["[", "{", "("]
# # # close_list = ["]", "}", ")"]
# # #
# # # # Function to check parentheses
# # # def checkBanalnceStack(myStr):
# # #     stack = []
# # #     for i in myStr:
# # #         if i in open_list:
# # #             stack.append(i)
# # #         elif i in close_list:
# # #             position = close_list.index(i)
# # #             if((len(stack) > 0) and (open_list[position] == stack[len(stack)-1])):
# # #                 stack.pop()
# # #             else:
# # #                 return "Unbalanced"
# # #
# # #     if len(stack) == 0:
# # #         return "Balanced"
# # #
# # # # test /driver code
# # # strings = "{[{()}}"
# # # print (strings, "-", checkBanalnceStack(strings))
# #
# #
# #
# #
# #
# #
# # # Using queue
# # #First Map opening parentheses to respective closing parentheses. Iterate through the given expression using i, if i
# # #is an open parentheses, append in queue, if i is close parentheses, Check whether queue is empty or i is the top
# # #element of queue, if yes, return Unbalanced, otherwise Balanced.
# #
# # #
# # # def checkExpression(expression):
# # #     open_tup = tuple('({[')
# # #     close_tup = tuple(')}]')
# # #
# # #     map = dict(zip(open_tup, close_tup))
# # #     queue = []
# # #
# # #     for i in expression:
# # #         if i in open_tup:
# # #             queue.append(map[i])
# # #             print (map[i])
# # #         elif i in close_tup:
# # #             if not queue or i != queue.pop():
# # #                 return "Unbalanced"
# # #     return "Balanced"
# # #
# # # # Test / Driver code
# # # testString = "{[]{()}}"
# # # print (testString,  "-", checkExpression(testString))
# #
# #
# # # Count CAPITAL latter
# #
# # # with open("SOME_LARGE_FILE") as fh:
# # #     count = 0
# # #     text = fh.read()
# # #
# # #     for character in text:
# # #         if character.isupper():
# # #             count += 1
# #
# #
# # # with open("SOME_LARGE_FILE") as fh:
# # #     count = 0
# # #      for line in fh:
# # #          for
# #
# #
# #
# # thisdict = {
# #     "brand" : "Ford",
# #     "model" : "Mustang",
# #     "year" : 1964
# # }
# #
# # print (thisdict["brand"])
# #
# # print (thisdict.get("model"))
# #
# # thisdict["year"] = 2018
# #
# # print (thisdict.get("year"))
# #
# #
# # # Keys
# # for x in thisdict:
# #     print (x)
# #
# # # values
# # for i in thisdict:
# #     print (thisdict[i])
# #
# #
# # # Alternative values
# # for j in thisdict.values():
# #     print (j)
# #
# #
# # # Both keys and values
# # for m, n in thisdict.items():
# #     print (m, n)
# #
# #
# # # IF value exist
# # for k in thisdict.values():
# #     if k == "Mustangsgdfsgsfgsfsg":
# #         print ("Yes the value exist in the dictionary ")
# #     else:
# #         print ("Value not found")
# #
# #
# #
# # # Add new element
# # thisdict.update({'color': 'read'})
# # for m, n in thisdict.items():
# #     print (m, n)
# #
# #
# # print (thisdict.items())
# #
# #
# #
# # # Shorte hand of if
# # # a = 2
# # # b = 3
# # #
# # # if a > b: print("a is greater thatn b")
# #
# #
# #
# # # print("A") if a > b else print("B")
# #
# #
# # # while loop
# h = 3
# while h > 6:
#     print (h)
#     if h == 3:
#         print("i is " + h)
#         continue
#     h +=1
#
#
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)
#
#
# thisStr = "hellow"
# for x in reversed(thisStr):
#     print x

# Increate by more than one
for x in range(2, 30, 3):
    print (x)



# Python Lambda
x = lambda a : a + 10
print (x(5))