import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


challenge = int(input('Choose 0 for rock, 1 for paper, and 2 for scissors '))

computer_brain = int(random.randint(0, 2))

if challenge == 0 and computer_brain == 0:
  print(
    'draw \n'
    'Computer choosed rock too'
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
)
elif challenge == 1 and computer_brain == 1:
  print('draw \n'
        'Computer choosed paper too'
        '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
       )
elif challenge == 2 and computer_brain == 2:
  print('draw \n'
        'Computer choosed scissors too'
        '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
       )

elif challenge == 0 and computer_brain == 1:
  print('You lose 😔\n'
       'Computer choose paper'
       '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
       )
elif challenge == 0 and computer_brain == 2:
  print(
    'You win 😃\n'
  'Congratulate 😊\n'
  'Computer choose scissors'
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
  
elif challenge == 1 and computer_brain == 0:
  print( 'You win 😃\n'
  'Congratulate 😊\n'
  'Computer choose rock'
      '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''' )
  
elif challenge == 1 and computer_brain == 2:
  print('You lose😔\n'
  'Computer choose scissors\n'
       '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')  
elif challenge == 2 and computer_brain == 0:
  print('You lose😔\n'
  'Computer choose rock'
       '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''' )
  
if challenge == 2 and computer_brain == 1:
  print( 'You win 😃\n'
  'Congratulate 😊\n'
  'Computer choose paper'
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
#Write your code below this line 👇


