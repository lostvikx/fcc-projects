import math

class Category:

  def __init__(self, name):

    self.cate_name = name
    self.ledger = []

  def __str__(self):
    return self.print_budget()

  # Add transaction

  def deposit(self, amt, description=""):

    amt = self.conv_float(amt)

    self.ledger.append({
        "amount": amt,
        "description": description
    })

  # Deduct transaction

  def withdraw(self, amt, description=""):

    amt = self.conv_float(amt)

    if self.check_funds(amt):

      self.ledger.append({
          "amount": -amt,
          "description": description
      })

      return True
    else:
      return False

  # Show balance amount

  def get_balance(self):

    bal = float()

    for trans in self.ledger:

      bal += trans["amount"]

    return bal

  # Transfer funds to another category

  def transfer(self, amt, another_cate):

    amt = self.conv_float(amt)

    if self.check_funds(amt):

      self.withdraw(amt, f"Transfer to {another_cate.cate_name}")

      another_cate.deposit(amt, f"Transfer from {self.cate_name}")

      return True
    else:
      return False

  # Conditional for checking enough balance

  def check_funds(self, amt):

    if amt > self.get_balance():
      return False
    else:
      return True

  # Convert a int to float

  def conv_float(self, a):

    try:
      return float(a)
    except:
      print("couldn't convert to float")

  def print_budget(self):

    output = ""

    # The title line
    title_len = len(self.cate_name)

    line_len = 30

    half_star_len = (line_len - title_len) // 2

    star = "*"

    for i in range(1, half_star_len):

      star += "*"

    title = f"{star}{self.cate_name}{star}"

    if len(title) < line_len:
      title += "*"

    output += title + "\n"

    # The trans lines
    for trans in self.ledger:

      trans_desc = trans["description"]

      if len(trans_desc) > 23:
        trans_desc = trans_desc[:23]

      # For fixed two decimal places
      trans_amt = f"{trans['amount']:.2f}"

      space = ""

      space_len = line_len - len(trans_desc) - len(trans_amt)

      while len(space) < space_len:
        space += " "

      trans_line = trans_desc + space + trans_amt

      output += trans_line + "\n"

    # The total line
    total_line = f"Total: {self.get_balance():.2f}"
    output += total_line

    return output


def create_spend_chart(cate_list):

  # Array of (floor 10th place percentage, category_name)
  percent_arr = []
  # Sum of the total withdrawals
  total_withdrawals = 0
  # Withdrawals array
  withdrawal_arr = []

  for category in cate_list:

    cate_with = 0

    for trans in category.ledger:

      amt = trans["amount"]

      if amt < 0:
        cate_with += abs(amt)

    total_withdrawals += cate_with
    withdrawal_arr.append((cate_with, category.cate_name))

  # print(withdrawal_arr)

  for with_amt, cate_name in withdrawal_arr:

    # Floor nearest 10th place perc
    perc = with_amt / total_withdrawals * 100
    perc = round(perc)
    perc = perc / 10
    perc = math.floor(perc)
    perc = perc * 10

    percent_arr.append((perc, cate_name))

  # print(withdrawal_arr, total_withdrawals, percent_arr)

  graph = "Percentage spent by category\n"
  total_percent = 100
  space = " "
  bar = space + "o" + space

  while total_percent >= 0:

    line = ""

    if total_percent < 10:
      line = (2 * space) + line

    elif total_percent < 100:
      line = space + line

    line += f"{total_percent}|"

    i = 0
    bar_count = 0

    # Iter over array of tuples
    while i < len(percent_arr):

      # If perc >= current line perc
      if percent_arr[i][0] >= total_percent:

        # If this is the first bar in the chart for the line perc then add logical spaces {which iter column} + bar, else if it's not the first bar {perv bar exists} then just add the bar.
        if bar_count == 0:
         line = line + ((i*3) * space) + bar
         # Increment the bar_count, so that we know that a bar exists.
         bar_count += 1
        else:
          line = line + bar

      i += 1

    # if len(line) <= 4: 
    #   line += 10 * space

    while len(line) < 4 + (len(percent_arr) * 3) + 1:
      line += " "

    line += "\n"
    total_percent -= 10
    graph += line

  # print(graph)

  x_axis = "    "
  j = 0

  while j < len(percent_arr):
    x_axis += "---"
    j += 1

  graph += x_axis + "-\n"

  # graph += "    "

  # The longest lenght category
  longest_cate = ""

  # Find the longest cate
  for perc, cate in percent_arr:

    if len(longest_cate) < len(cate):
      longest_cate = cate

  i = 0

  

  while i < len(longest_cate):
    var_line = "    "

    for perc, cate in percent_arr:

      # If the word is complete, then add blank space
      if len(cate) <= i:
        var_line += "   "
        continue

      var_line = var_line + " " + cate[i] + " "

    while len(var_line) < 4 + (len(percent_arr) * 3) + 1:
      var_line += " "

    # If not last iter, then go to new line
    # If last, don't go to new line
    if not ((len(longest_cate) - i) == 1):

      var_line += "\n"

    i += 1

    graph += var_line

  return graph


# food = Category("Food")
# entertainment = Category("Entertainment")
# business = Category("Business")
# food.deposit(900, "deposit")
# entertainment.deposit(900, "deposit")
# business.deposit(900, "deposit")
# food.withdraw(105.55)
# entertainment.withdraw(33.40)
# business.withdraw(10.99)
# actual = create_spend_chart([business, food, entertainment])

# print(actual)

# print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
