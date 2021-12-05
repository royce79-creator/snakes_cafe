print('hello world')
def opening():

  intro_menu = '''**************************************
  **    Welcome to the Snakes Cafe!   **
  **    Please see our menu below.    **
  **
  ** To quit at any time, type "quit" **
  **************************************

  Appetizers
  ----------
  Wings
  Cookies
  Spring Rolls

  Entrees
  -------
  Salmon
  Steak
  Meat Tornado
  A Literal Garden

  Desserts
  --------
  Ice Cream
  Cake
  Pie

  Drinks
  ------
  Coffee
  Tea
  Unicorn Tears

  ***********************************
  ** What would you like to order? **
  ***********************************

  '''

  print(f'{intro_menu}')

drinks = ['coffee', 'tea', 'unicorn tears']
desserts = ['ice cream', 'cake, pie']
entrees = ['salmon', 'steak', 'meat tornado', 'a literal garden']
appetizers = ['wings', 'cookies', 'spring rolls']

if __name__ == '__main__':
  opening()
  customer_order = ''
  number = 0
  orders = []
  while customer_order != 'quit':
    customer_order = input('> ')
    orders.append(customer_order)
    number = orders.count(customer_order)
    if customer_order == 'quit':
      break
    elif number <= 1:
      items = f'** 1 order of {customer_order} has been added to your meal **'
      print(items)
    elif number > 1: 
      items = f'** {number} orders of {customer_order} ahve been added to your meal **'
      print(items)

# Saw some code from Alex Payne that allowed me to get the final solution to this assignment! 
