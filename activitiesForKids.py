# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.

# For example, Jay ran like a fool! or Chantelle slid down the slide!.

# The following lists of children should be iterated, and the names sent to the appropriate functions.

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

def run(name):
    print(f'{name} just felt like running!')

def swing(name):
    print(f'{name} likes to swing at recess.')

def slide(name):
    print(f'{name} is done been slidin\' on that there slide')

def hide_and_seek(name):
    print(f'Have you seen {name}? {name} is really good at hide and seek!')

for kid in running_kids:
    run(kid)

for kid in swinging_kids:
    swing(kid)

for kid in sliding_kids:
    slide(kid)

for kid in hiding_kids:
    hide_and_seek(kid)