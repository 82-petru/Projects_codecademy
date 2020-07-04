# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 18:20:56 2019

@author: petru
"""

print("Hello", "how are you?", sep="\n")

print("")
string_one = "manhattan"
string_two = "san francisco"
count = []
for i in string_one:
  if i in string_two:
    if i not in count:
      print(i)
      count.append(i)  
print(count)

def username_generator(first_name, last_name):
    username =  first_name[:3] + last_name[:4]
    if len(first_name) < 3:
        username = first_name + last_name[:4]
    elif len(last_name) < 4:
        username = first_name[:3] + last_name
    return username

def password_generator(username):
  password = " "
  for item in range(len(username)):
    password = username[-1] + username[: len(username) -1]
  print(password)#return can be used, too 
user = username_generator('Petru', 'Apachitei')
password_generator(user)

print("")
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(',')
highlighted_poems_stripped = []
for poems in highlighted_poems_list:
  poems.strip()
  highlighted_poems_stripped.append(poems.strip())
highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  poem.split(':')
  highlighted_poems_details.append(poem.split(':'))
print(highlighted_poems_details)
titles = []
poets = []
dates = []
for line in highlighted_poems_details:
  titles.append(line[0])
  poets.append(line[1])
  dates.append(line[2])
for i in range(len(titles)):
  print("The {} was published by {} in {}.".format(titles[i], poets[i], dates[i]))
 
 