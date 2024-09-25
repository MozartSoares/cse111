from random import choice

def make_sentence(quantity, tense):
  determiner = get_determiner(quantity)
  adjective = get_adjective()
  noun = get_noun(quantity)
  verb = get_verb(quantity, tense)
  
  
  sentence = f"{determiner} {adjective} {noun} {verb}"
  prepositional_sentence = get_prepositional_phrase(quantity)
  complete_sentence = f"{sentence} {prepositional_sentence}"
  
  return complete_sentence.capitalize()

def get_determiner(quantity):
  """Return a randomly chosen determiner. A determiner is
  a word like "the", "a", "one", "some", "many".
  If quantity is 1, this function will return either "a",
  "one", or "the". Otherwise this function will return
  either "some", "many", or "the".
  Parameter
      quantity: an integer.
          If quantity is 1, this function will return a
          determiner for a single noun. Otherwise this
          function will return a determiner for a plural
          noun.
  Return: a randomly chosen determiner.
  """
  if quantity == 1:
      words = ["a", "one", "the"]
  else:
      words = ["some", "many", "the"]
  # Randomly choose and return a determiner.
  word = choice(words)
  return word

def get_noun(quantity):
  if (quantity == 1 ):
    words = ["bird", "boy", "car", "cat", "child",]
  else:
    words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
  return choice(words)

def get_verb(quantity, tense):
  if tense == "past":
    words = ["drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"]
    
  elif tense == "present":
    if quantity == 1:
      words = ["drinks", "eats", "grows", "laughs", "thinks",
              "runs", "sleeps", "talks", "walks", "writes"]
    else:
      words = ["drink", "eat", "grow", "laugh", "think",
              "run", "sleep", "talk", "walk", "write"]
      
  elif tense == "future":
    words = ["will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"]
  else:
    raise ValueError("Invalid tense. Choose from 'past', 'present', or 'future'.")
  
  return choice(words)
  
def get_adjective():
  words = ["big", "bright", "colorful", "dark", "fuzzy",
          "happy", "jolly", "loud", "quiet", "shiny"]
  return choice(words)

def get_preposition(): 
  words = ["about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"]
  return choice(words)

def get_prepositional_phrase(quantity):
  
  preposition = get_preposition()
  determiner = get_determiner(quantity)
  adjective = get_adjective()
  noun = get_noun(quantity)
  
  sentence = f"{preposition} {determiner} {adjective} {noun}"
  return sentence

def main():
  print(make_sentence(1, "past"))
  print(make_sentence(1, "present"))
  print(make_sentence(1, "future"))
  print(make_sentence(2, "past"))
  print(make_sentence(3, "present"))
  print(make_sentence(4, "future"))

main()