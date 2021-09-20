import argparse

emojiDictionary = {
 0 :'0️⃣',
 1 :'1️⃣',
 2 :'2️⃣',
 3 :'3️⃣',
 4 :'4️⃣',
 5 :'5️⃣',
 6 :'6️⃣',
 7 :'7️⃣',
 8 :'8️⃣',
 9 :'9️⃣',
'.':'⏺️'
}

def split (sum):
    n = str(sum)
    listNum = [i for i in n]
    return listNum

def addition(num1,num2):
    sum = num1 + num2
    return sum

def division(num1,num2):
    sum = num1 / num2 
    return sum

def multiplication(num1,num2):
    sum = num1 * num2 
    return sum

def subtraction(num1,num2):
    sum = num1 - num2 
    return sum

def operator(operator,num1,num2):
    if operator == "add":
        return addition(num1,num2)
    elif operator  == "divide":
        return division(num1,num2)
    elif operator  == "multiply":
        return multiplication(num1,num2)
    elif operator  == "subtract":
        return subtraction(num1,num2)
    else:
        return "Insert your operator"
        

parser = argparse.ArgumentParser(description='The emoji calculator - sum of intergers emojified - how unorginal \U0001F606')
parser.add_argument('operator', 
    help="Choose your operator i.e add, divide, subtract or mulitiply")
parser.add_argument('num1', type=int, 
    help='pick your first number')
parser.add_argument('num2', type=int, 
    help="pick your second number")
args = parser.parse_args()

result = operator(args.operator,args.num1,args.num2)
resultSplit = split(result)

list = []
while resultSplit:
 if resultSplit != "." :
  single = float(resultSplit.pop(-1))
  emojifiedNumber = emojiDictionary[single]
  list.append(emojifiedNumber)
 else:
  single = float(resultSplit.pop(-1))
  emojifiedNumber = emojiDictionary[single]
  list.append(emojifiedNumber)
  
list.reverse()
str1 = ' '.join(str(e) for e in list)
print(str1)

# need to work on decimals
# need to work on negative numbers
