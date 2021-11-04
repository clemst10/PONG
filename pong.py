x_joueur1=100
y_joueur1=150
x_joueur2=600
y_joueur2=150
position_balle_x=350
position_balle_y=200
diametre_balle=20
largeur_raquette=10
longeur_raquette=90
vitesse_balle_x=0
vitesse_balle_y=0
vitesseIA=5
score_joueur1=0
score_joueur2=0
secondes=0
minutes=0
image_par_seconde=30
choix_start=0
choix_multi=0
choix_solo=0
choix_quit=0
largeur_carre=70
x_carre=int(random(250,400))
y_carre=int(random(0,350))


def setup():
    size(700,400)

def draw():
    
    if choix_start == False:
        menu()
    
    if choix_start == True:
        menu2()
   
    if choix_multi == True:
        jeu_multi()
    
    if choix_solo == True:
        jeu_solo()     
    
    if choix_quit == True:
        menu()

def menu():
    background (0)
    menu=loadImage("menu.png")
    menu.get(0,100,200,300)
    image(menu,0,0)
    
    textSize(25)
    fill(255)
    rect(300,225,100,30)

    rect(0,0,3,700)
    rect(0,0,700,3)
    rect(0,397,700,3)
    rect(697,0,3,400)
    noStroke()
    fill(0)
    text("START",310,225,200,200)
    
def menu2():
    background (0)
    menu=loadImage("menu.png")
    menu.get(0,100,200,300)
    image(menu,0,0)
    fill(255)
    rect(200,230,100,30)
    rect(400,230,100,30)
    rect(0,0,3,700)
    rect(0,0,700,3)
    rect(0,397,700,3)
    rect(697,0,3,400)
    noStroke()
    
    fill(0)
    text("SOLO",215,230,250,250)
    text("MULTI",415,230,150,200)

def jeu_solo():
    background(0)
    fill(255)
    deplacement_balle()
    rebond_raquette()
    deplacement_joueur_IA()
    rebond_joueur1()
    rebond_joueur2()    
    rebond_mur()
    but()
    direction_glace()
    acceleration_balle()
    chronometre()
    affichage_terrain()
    victoire()

def jeu_multi():

    background(0)
    fill(255)
    deplacement_balle()
    rebond_joueur1()
    rebond_joueur2()    
    rebond_mur()
    but()
    direction_glace()
    acceleration_balle()
    chronometre()
    affichage_terrain()
    victoire()

def rebond_raquette():
    global y_joueur1,longeur_raquette,vitesseIA
    if y_joueur1<0 or y_joueur1>400-longeur_raquette:
        vitesseIA=-vitesseIA
    return vitesseIA

def deplacement_joueur_IA():
    global y_joueur1,position_balle_y,vitesseIA,seconde,longeur_raquette
    
    if secondes<30:
        y_joueur1=position_balle_y-(longeur_raquette)/2
    else:
        y_joueur1=y_joueur1+vitesseIA
    
    if y_joueur1<0 and y_joueur1>400-longeur_raquette:
        vitesseIA=-vitesseIA
    return y_joueur1    
            
# deplacement de la balle    
def deplacement_balle():    
    global position_balle_x,position_balle_y,vitesse_balle_x,vitesse_balle_y

# on ajoute la vitesse a la position     
    position_balle_x=position_balle_x+vitesse_balle_x
    position_balle_y=position_balle_y+vitesse_balle_y
    return position_balle_x,position_balle_x

# collision raquette du joueur 1 et balle
def rebond_joueur1():    
    global vitesse_balle_y,vitesse_balle_x,position_balle_x,position_balle_y,y_joueur1,x_joueur1,diametre_balle,largeur_raquette
    
# si la balle vas vers le bas     
    if vitesse_balle_y>0:
        
# si la balle est au niveau de la raquette et que la balle tape sur le haut de la raquette     
        if position_balle_x == x_joueur1 + largeur_raquette + (diametre_balle)/2 and y_joueur1 - 10 < position_balle_y < y_joueur1 +(longeur_raquette)/3: 

# la balle rapars vers le haut et dans l'autre sens            
            vitesse_balle_y=-vitesse_balle_y
            vitesse_balle_x=vitesse_balle_x
    
        if position_balle_x == x_joueur1 + largeur_raquette + (diametre_balle)/2 and y_joueur1 + (longeur_raquette)/3 < position_balle_y < y_joueur1 + ((longeur_raquette)/3)*2:  
            vitesse_balle_y=0
            vitesse_balle_x=vitesse_balle_x
    
        if position_balle_x == x_joueur1 + largeur_raquette + (diametre_balle)/2 and y_joueur1 + ((longeur_raquette)/3)*2 < position_balle_y < y_joueur1 + longeur_raquette + 10:  
            vitesse_balle_y=vitesse_balle_y
            vitesse_balle_x=-vitesse_balle_x
    
    if vitesse_balle_y==0:
        
        if position_balle_x == x_joueur1 + largeur_raquette + (diametre_balle)/2 and y_joueur1 -10 < position_balle_y < y_joueur1+((longeur_raquette)/3):
            vitesse_balle_y=-4
            vitesse_balle_x=vitesse_balle_x
    
        if position_balle_x == x_joueur1 + largeur_raquette + (diametre_balle)/2 and y_joueur1 + ((longeur_raquette)/3) < position_balle_y < y_joueur1 + ((longeur_raquette)/3)*2 :  
            vitesse_balle_y=0
            vitesse_balle_x=-vitesse_balle_x
            
    
        if position_balle_x == x_joueur1 + largeur_raquette + (diametre_balle)/2 and y_joueur1 + ((longeur_raquette)/3)*2 < position_balle_y < y_joueur1 + longeur_raquette +10:  
            vitesse_balle_y=4
            vitesse_balle_x=-vitesse_balle_x
            
    
    if vitesse_balle_y<0:
        
        if position_balle_x == x_joueur1 + largeur_raquette + (diametre_balle)/2 and y_joueur1 - 10 < position_balle_y < y_joueur1 +((longeur_raquette)/3) : 
            vitesse_balle_y=vitesse_balle_y
            vitesse_balle_x=-vitesse_balle_x
            
    
        if position_balle_x == x_joueur1 + largeur_raquette + (diametre_balle)/2 and y_joueur1 + (longeur_raquette)/3 < position_balle_y < y_joueur1 + ((longeur_raquette)/3)*2 :  
            vitesse_balle_y=0
            vitesse_balle_x=-vitesse_balle_x
            
    
        if position_balle_x == x_joueur1 + largeur_raquette + (diametre_balle)/2 and y_joueur1 + ((longeur_raquette)/3)*2 < position_balle_y < y_joueur1 + longeur_raquette + 10:  
            vitesse_balle_y=-vitesse_balle_y
            vitesse_balle_x=-vitesse_balle_x

# collision raquette du joueur 2 et balle
def rebond_joueur2():   
    global vitesse_balle_y,vitesse_balle_x,position_balle_x,position_balle_y,y_joueur2,x_joueur2,diametre_balle,largeur_raquette
    
    if vitesse_balle_y>0:
        
        if position_balle_x == x_joueur2 - (diametre_balle)/2 and y_joueur2 - 10 < position_balle_y < y_joueur2 +(longeur_raquette)/3: 
            vitesse_balle_y=-vitesse_balle_y
            vitesse_balle_x=vitesse_balle_x
    
        if position_balle_x == x_joueur2 - (diametre_balle)/2 and y_joueur2 + (longeur_raquette)/3 < position_balle_y < y_joueur2 + ((longeur_raquette)/3)*2:  
            vitesse_balle_y=0
            vitesse_balle_x=vitesse_balle_x
    
        if position_balle_x == x_joueur2 - (diametre_balle)/2 and y_joueur2 + ((longeur_raquette)/3)*2 < position_balle_y < y_joueur2 + longeur_raquette + 10:  
            vitesse_balle_y=vitesse_balle_y
            vitesse_balle_x=-vitesse_balle_x
    
    if vitesse_balle_y==0:
        
        if position_balle_x == x_joueur2 - (diametre_balle)/2 and y_joueur2 -10 < position_balle_y < y_joueur2+((longeur_raquette)/3):
            vitesse_balle_y=-4
            vitesse_balle_x=vitesse_balle_x
    
        if position_balle_x == x_joueur2 - (diametre_balle)/2 and y_joueur2 + ((longeur_raquette)/3) < position_balle_y < y_joueur2 + ((longeur_raquette)/3)*2 :  
            vitesse_balle_y=0
            vitesse_balle_x=-vitesse_balle_x
            
    
        if position_balle_x == x_joueur2 - (diametre_balle)/2 and y_joueur2 + ((longeur_raquette)/3)*2 < position_balle_y < y_joueur2 + longeur_raquette +10:  
            vitesse_balle_y=4
            vitesse_balle_x=-vitesse_balle_x
            
    
    if vitesse_balle_y<0:
        
        if position_balle_x == x_joueur2 - (diametre_balle)/2 and y_joueur2 - 10 < position_balle_y < y_joueur2 +((longeur_raquette)/3) : 
            vitesse_balle_y=vitesse_balle_y
            vitesse_balle_x=-vitesse_balle_x
            
    
        if position_balle_x == x_joueur2 - (diametre_balle)/2 and y_joueur2 + (longeur_raquette)/3 < position_balle_y < y_joueur2 + ((longeur_raquette)/3)*2 :  
            vitesse_balle_y=0
            vitesse_balle_x=-vitesse_balle_x
            
    
        if position_balle_x == x_joueur2 - (diametre_balle)/2 and y_joueur2 + ((longeur_raquette)/3)*2 < position_balle_y < y_joueur2 + longeur_raquette + 10:  
            vitesse_balle_y=-vitesse_balle_y
            vitesse_balle_x=-vitesse_balle_x    

# rebond de la balle sur les murs
def rebond_mur():    
    global position_balle_y,position_balle_y,vitesse_balle_y
    if position_balle_y>385 or position_balle_y<15:
        vitesse_balle_y=-vitesse_balle_y
    return vitesse_balle_y

# score
def but():
    global position_balle_x,position_balle_y,vitesse_balle_x,vitesse_balle_y,y_joueur1,y_joueur2,score_joueur1,score_joueur2,secondes,image_par_seconde
# si la balle depasse le mur de droite
    if position_balle_x>800: 
# remet la balle au centre
        position_balle_x=350
        position_balle_y=200
# arrete la balle
        vitesse_balle_x=0
        vitesse_balle_y=0
# remet la raquette du joueur 1 au centre
        y_joueur1=150
        y_joueur2=150
# ajoute 1 au score du joueur 1
        score_joueur1+=1
        secondes=0
        image_par_seconde=30
# si la balle depasse le mur de gauche
    if position_balle_x<-100:
# remet la balle au centre        
        position_balle_x=350
        position_balle_y=200
# arrete la balle        
        vitesse_balle_x=0
        vitesse_balle_y=0
# remet la raquette du joueur 2 au centre      
        y_joueur1=150
        y_joueur2=150
# ajoute 1 au score du joueur 2          
        score_joueur2+=1
        secondes=0
        image_par_seconde=30
    return score_joueur1,score_joueur2

def acceleration_balle():
    global secondes,image_par_seconde
    if secondes!=0 and secondes%5==0:
        image_par_seconde+=1
    return image_par_seconde


    
def chronometre():    
    global secondes,minutes,image_par_seconde,vitesse_balle_x,couleur1,couleur2,couleur3
    frameRate (image_par_seconde)
    if frameCount %image_par_seconde==0 and vitesse_balle_x!=0:
        secondes+=1
        if secondes>59:
            minutes+=1
            secondes=0
    return secondes,minutes

# affichage du terrain des raquettes de la balle et du score
def affichage_terrain():
    
    global x_joueur1,y_joueur1,largeur_raquette,longeur_raquette,x_joueur2,y_joueur2,position_balle_x,position_balle_y,diametre_balle,score_joueur1,score_joueur2

    glace()
    fill(255)
    textSize(40)
    text(str(score_joueur1),250,80)
    text(str(score_joueur2),425,80)
    textSize(35)
    
    text(":",344,25)
    textSize(25)
    text(str(secondes),360,25)
    text(str(minutes),320,25)
    

    rect(x_joueur1,y_joueur1,largeur_raquette,longeur_raquette)
    rect(x_joueur2,y_joueur2,largeur_raquette,longeur_raquette)
    
    rect(300,30,100,2)
    rect(300,0,2,30)
    rect(398,0,2,30)

    
    rect(349,30,2,400)
    rect(0,0,3,700)
    rect(0,0,700,3)
    rect(0,397,700,3)
    rect(697,0,3,400)

    ellipse(position_balle_x,position_balle_y,diametre_balle,diametre_balle)
    noStroke()
    
# direction de la balle au depart
def vitesse_aleatoire():
    global vitesse_aleatoire_x,vitesse_aleatoire_y,vitesse_balle_x,vitesse_balle_y,vitesse
    
    vitesse_aleatoire_x=int(random(0,10))
    vitesse_aleatoire_y=int(random(0,10))
    
    if vitesse_aleatoire_x<5:
        vitesse_balle_x=-10
    else:
        vitesse_balle_x=10

    if vitesse_aleatoire_y<5:
        vitesse_balle_y=-3
    else:
        vitesse_balle_y=3
    
    return vitesse_balle_x,vitesse_balle_y

def victoire():
    global score_joueur1,score_joueur2
    if score_joueur1==5:
        background(0)
        text("VICTOIRE DU JOUEUR DE GAUCHE",130,150,700,400)
        rect(298,300,70,27)
        textSize(25)
        fill(0)
        text("QUIT",300,300,700,400)
    if score_joueur2==5:
        background(0)
        text("VICTOIRE DU JOUEUR DE DROITE",130,150,700,400)
        rect(298,300,70,27)
        textSize(25)
        fill(0)
        text("QUIT",300,300,700,400)

def direction_glace():
    global position_balle_x,x_carre,position_balle_y,y_carre,largeur_carre,vitesse_balle_y
   
    if (score_joueur1>2 or score_joueur2>2) and secondes>0 and secondes!=0 and x_carre<position_balle_x<x_carre+largeur_carre and y_carre - 10 < position_balle_y <y_carre+largeur_carre+10:
        vitesse_balle_y=-vitesse_balle_y 
        x_carre=int(random(250,400))
        y_carre=int(random(0,350))
        
    
    return vitesse_balle_y
    

def glace():
    global x_carre,y_carre,largeur_carre,score_joueur1,score_joueur2
    
    if score_joueur1>2 or score_joueur2>2 and secondes>0 and secondes!=0:
        
        fill(0,200,255)
        rect(x_carre,y_carre,largeur_carre,largeur_carre)

# deplacement des raquettes
def keyPressed():
    global x_joueur1,y_joueur1,x_joueur2,y_joueur2,vitesse_balle_x,vitesse_balle_y
    if key==CODED:
        if keyCode==SHIFT and y_joueur1>0:
            y_joueur1=y_joueur1-30
        if keyCode==CONTROL and y_joueur1+longeur_raquette<400:
            y_joueur1=y_joueur1+30
        if keyCode==UP and y_joueur2>0:
            y_joueur2=y_joueur2-30
        if keyCode==DOWN and y_joueur2+longeur_raquette<400:
            y_joueur2=y_joueur2+30
        if keyCode==LEFT and vitesse_balle_x==0 and vitesse_balle_y==0:
            vitesse_aleatoire()

# choix des menus
def mouseReleased():
    global choix_start,choix_multi,choix_solo,choix_quit
    if 300<mouseX<400 and 225<mouseY<255:
        choix_start = True
    
    if 400<mouseX<500 and 230<mouseY<255:
        choix_multi = True

    if 200<mouseX<300 and 230<mouseY<255:
        choix_solo = True

    if 298<mouseX<368 and 300<mouseY<327:
        choix_quit = True