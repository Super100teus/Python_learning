bool1 = 4 < 5 and 5 > 6
bool2 = 10 == 10 or 7 < 3
tex = '''Fue un miembro poderoso del Concilio Blanco, tanto, que incluso Galadriel le propuso como líder del 
mismo, cosa que Saruman rechazó, ya que él era el Jefe del Concilio y tenía sus propios intereses. Gandalf también lo 
rechazaría ya que no quería estar atado a otros excepto a quienes lo enviaron a la Tierra Media.'''
bool3 = ('saruman' in tex) or ('estar' in tex)
bool4 = not 'a' == 'a'
print(f' 1.-{bool1}, 2.-{bool2}, 3.-{bool3}, 4.-{bool4}')
