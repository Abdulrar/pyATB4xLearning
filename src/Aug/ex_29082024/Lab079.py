t = tuple()
print(t)

# Conversion List to Tuple
t1 = tuple(["pramod","amit","manisha"])  # this is like 'tuple(my_list)'
print(t1)

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
new_tuple = (hero1,hero2)   # Tuple within tuple  (0,0) (('Batman', 'Bruce Wayne'), ('Wonder Woman', 'Diana Prince'))
print(new_tuple)
print(new_tuple[0]) # ("Batman", "Bruce Wayne")
print(new_tuple[0][0]) # "Batman"
print(new_tuple[1][1]) # "Diana Prince"

new_tuple = hero1+hero2
print(new_tuple)
