def subtract(total, num):
  return total - num


def loopy(list_of_arrays, which_line):

  result = ""

  for arr in list_of_arrays:

    # These are strings
    num1 = arr[0]
    num2 = arr[2]
    operator = arr[1]
    space1 = " "
    space2 = " "

    dash = "-"

    line_len = 0

    if len(num1) >= len(num2):
      line_len = len(num1) + 2
    else:
      line_len = len(num2) + 2

    while len(dash) < line_len:
      dash += "-"

    # Add space for right-align numbers
    space1_num = subtract(line_len, len(num1))
    space2_num = subtract(line_len, len(num2)) - 1

    while len(space1) < space1_num:
      space1 += " "

    while len(space2) < space2_num:
      space2 += " "

    if which_line == 1:
      line1 = space1 + num1
      result += f"{line1}    "

    elif which_line == 2:
      line2 = operator + space2 + num2
      result += f"{line2}    "

    elif which_line == 3:
      line3 = dash
      result += f"{line3}    "

  return result.rstrip()


def arithmetic_arranger(problems, ans=False):

  new_prob_arr = []
  ans_of_prob = int()

  if len(problems) > 5:
    return "Error: Too many problems."

  for prob in problems:

    problem_div = prob.split(" ")

    if len(problem_div) != 3:
      return "Error: Numbers or operator entered in wrong format."
    else:
      new_prob_arr.append(problem_div)

  result1 = loopy(new_prob_arr, 1)
  result2 = loopy(new_prob_arr, 2)
  result3 = loopy(new_prob_arr, 3)
  result4 = ""

  for single_prob_arr in new_prob_arr:

    # These are strings
    num1 = single_prob_arr[0]
    num2 = single_prob_arr[2]
    operator = single_prob_arr[1]
    line_len = 0

    if len(num1) >= len(num2):
      line_len = len(num1) + 2
    else:
      line_len = len(num2) + 2

    space3 = " "

    try:
      num1 = int(num1)
      num2 = int(num2)
    except:
      return "Error: Numbers must only contain digits."

    if num1 > 9999 or num2 > 9999:
      return "Error: Numbers cannot be more than four digits."

    if operator == "+":
      ans_of_prob = num1 + num2
    elif operator == "-":
      ans_of_prob = num1 - num2
    else:
      return "Error: Operator must be '+' or '-'."

    num3 = str(ans_of_prob)

    space3_num = subtract(line_len, len(num3))

    while len(space3) < space3_num:
      space3 += " "

    result4 += f"{space3 + str(ans_of_prob)}    "

  result4 = result4.rstrip()

  if ans == True:
    arranged_problems = f"{result1}\n{result2}\n{result3}\n{result4}"
  else:
    arranged_problems = f"{result1}\n{result2}\n{result3}"

  return arranged_problems


# print(arithmetic_arranger(['3801 - 2', '123 + 49']))
