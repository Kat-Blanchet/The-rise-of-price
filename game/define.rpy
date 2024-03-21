# all characters that are going that are in the game 
define kat = Character("Kat", color='7B0323')
define akira = Character("Akira", color='301934')
define kai =  Character('Kai', color='00008B')
define fumi = Character('Fumi', color='0000FF') #get bring back as rose  
define kate = Character('Kate', color='ADD8E6') #dead at mid way 
define pk = Character('Past Kat', color='7B0323')
define pk2 = Character('Past Kai', color='00008B')

# character based on a choice at the mid way point of the game 
define ckat = Character('"Cursed" Kat', color='560e2c')
define pkat = Character('"Prince" Kat', color='560e2c')
define pkai =  Character('Kai', color='00008B')
define akira = Character("Akira", color='301934')
define rose = Character("Rose")

# Characters that give more story or imformation to the player
define N = Character("Narrator", color='FFFFFF')
define S = Character("system", color='808080') 

transform smidge_left:
  xalign 0.3

transform smide_right:
  xalign 0.7


# Characters images 
# TODO make the charaters models using vroid  
# TODO add in the characters models 


# background imagee



# system
image splashy = Movie( play='splash_screen.webm' )
define config.has_autosave = False
define config.has_quicksave = False