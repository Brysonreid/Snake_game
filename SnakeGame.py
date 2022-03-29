import pygame
import random




pygame.init()    #this top section is used to set all our variables that will come into play later 
pygame.display.init()
snakesize=20
growth = snakesize
height = 800
width = 1500
screen= pygame.display.set_mode((width,height))
pygame.font.init()
calibri=pygame.font.SysFont("calibri", 30)
impact=pygame.font.SysFont("impact", 60)
fourth=int(width/4)
sixth = int(width/6)
foodnumber=1
Ofoodnumber=1
speed=10
p1colour=(0,255,0)
p2colour=(0,0,255)
eaten = 0
foodincreasing=False
clock=pygame.time.Clock()
foodsize=20
Ogrowth=10
speedincreasing = False
foodincreasing = False
again="yes"
again1="yes"
choose="none"
players="none"
player1score = 0
player2score=0

speed1=speed
speed2=speed

'''function to register clicks in a certain area'''
def click(x,y,width,height):
    exitgame()
    
    if pygame.mouse.get_pos()[0] > x and pygame.mouse.get_pos()[0]<(x+width) and pygame.mouse.get_pos()[1]>y and pygame.mouse.get_pos()[1] <(y+height):
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.rect(screen,(255,255,255),(x,y,width,height))
            pygame.display.update()
            return True 

'''This makes adding text a lot easier'''
def smalltext(text,x,y):
    words= calibri.render(text,2,(255,255,255))
    screen.blit(words,(x,y))    


'''this function takes in the list of snake parts and adds a certain ammount of extra parts to the end of the snake list '''
def growsnake(tail,growth):   
    for i in range(growth):
        tail.append([-100,-100]) 
    return tail


'''this function prints out each part of the snake  '''
def showsnake(tail,colour):
    for idx,part in enumerate(tail):
        pygame.draw.rect(screen,(colour),(part[0],part[1],snakesize,snakesize))
        

'''this function looks to see if either snake hits itself or the wall for the single player version of the game. To do so it takes the position of the head and tests if it is out of the bounds of the screen or if the head overlaps with the rest of the body'''
def crash1(tail,height,width):
    
    front=tail[0]
    snake=tail[1:]
    
    for idx, parts in enumerate(snake):    #looks for when it overlaps with itself
        tailx=parts[0]
        taily=parts[1]
        headx=front[0]
        heady=front[1]
        if (headx>=tailx and headx <=(tailx)) or (tailx>=headx and tailx<=(headx)):
            if (heady>=taily and heady <=(taily)) or (taily>=heady and taily <=(heady)):
                return True

    if front[0] >= width:
        return True
    if front[0] <= 0:
        return True
    if front[1] <= 0:
        return True
    if front[1] >= height:
        return True
    
'''This function looks to see if the head overlaps with any of the onscreen food'''
def getfood(head,foodlist):

    headx=head[0]
    heady=head[1]
    for idx,foods in enumerate(foodlist):
    
        foodx=foods[0]
        foody=foods[1]
        if (headx>=foodx and headx <=(foodx+snakesize)) or (foodx>=headx and foodx<=(headx+snakesize)):
            if (heady>=foody and heady <=(foody+snakesize)) or (foody>=heady and foody <=(heady+snakesize)):
                print("food Got")
                foodlist.pop(idx)
                return True

'''This function moves the head of the snake in whichever direction the player has put it in and then updates the rest of the snake replacing each body part to make it follow itself'''
def movesnake(tail,direction,speed):
    for part in range(len(tail)-1,0,-1):
        tail[part]=tail[part-1]
    head=tail[0]
    xpos=head[0]
    ypos=head[1]
    if direction == "Up":
        ypos-=speed
    
    elif direction == "Down":
        ypos+=speed
    
    elif direction == "Left":
        xpos-=speed
    
    elif direction == "Right":
        xpos+=speed
    tail[0]=[xpos,ypos]

    return tail 


'''This function tests to see if either snake overlaps with itself, the wall, or the other snake by testing if any of the squares of the snake overlaps with the domain and range of the other''' 
def crash(snake1,snake2,width,height,growthS1,growthS2):
    #test if snake 1 dies
    head1=snake1[0]
    head1x=head1[0]
    head1y=head1[1]    
    head2=snake2[0]
    head2x=head2[0]
    head2y=head2[1]     
    if (head1x>=head2x and head1x <=(head2x+snakesize)) or (head2x>=head1x and head2x<=(head1x+snakesize)):
        if (head1y>=head2y and head1y <=(head2y+snakesize)) or (head2y>=head1y and head2y <=(head1y+snakesize)):
            if growthS1>growthS2:
                return ["Player2 wins",1]
            elif growthS2>growthS1:
                return ["PLayer 1 Wins",2]
            elif random.randint(1,2)==1:
                return ["Player 2 wins",1]
            else:
                return ["Player 1 Wins",2]

    for idx, part in enumerate(snake2):
        tailx=part[0]
        taily=part[1]
        if (head1x>=tailx and head1x <=(tailx+snakesize)) or (tailx>=head1x and tailx<=(head1x+snakesize)):
            if (head1y>=taily and head1y <=(taily+snakesize)) or (taily>=head1y and taily <=(head1y+snakesize)):
                
                return ["Player 1 wins",2]
            
    for idx, part in enumerate(snake1):
        tailx=part[0]
        taily=part[1]
 
        if (head2x>=tailx and head2x <=(tailx+snakesize)) or (tailx>=head2x and tailx<=(head2x+snakesize)):
            if (head2y>=taily and head2y <=(taily+snakesize)) or (taily>=head2y and taily <=(head2y+snakesize)):
                
                return ["Player 2 wins",1]
            
        if head1x+snakesize >=width or head1x <=0 or head1y+snakesize >= height or head1y <=0:
            
            return ["Player 2 hit the wall so Player 1 wins",2]
        
        if head2x+snakesize >=width or head2x <=0 or head2y+snakesize >= height or head2y <=0:
            
            return ["Player 1 hit the wall so Player 2 wins",1]
        
        tail1=snake1[1:]
        head1=snake1[0]
        
        for idx, parts in enumerate(tail1):    #looks for when it overlaps with itself
            tail1x=parts[0]
            tail1y=parts[1]
            head1x=head1[0]
            head1y=head1[1]
            if (head1x>=tail1x and head1x <=(tail1x)) or (tail1x>=head1x and tail1x<=(head1x)):
                if (head1y>=tail1y and head1y <=(tail1y)) or (tail1y>=head1y and tail1y <=(head1y)):
                    return ["Player 2 hit itself",2]
                
        tail2=snake2[1:]
        head2=snake2[0]
        
        for idx, parts in enumerate(tail2):    #looks for when it overlaps with itself
            tail2x=parts[0]
            tail2y=parts[1]
            head2x=head2[0]
            head2y=head2[1]
            if (head2x>=tail2x and head2x <=(tail2x)) or (tail2x>=head2x and tail2x<=(head2x)):
                if (head2y>=tail2y and head2y <=(tail2y)) or (tail2y>=head2y and tail2y <=(head2y)):
                    return ["Player 1 hit self",1]
    return ["no one wins",0]



'''This function adds another food in a random spot that isnt already taken by the tails of either snake or another piece of food'''
def addfood(snake1,snake2):
    
    fakefood=True
    while fakefood:
        fakefood = False
        foodx=(random.randint(0,width-foodsize))
        foody=(random.randint(0,height-foodsize))    
    
        print("food could be", [foodx,foody])
      
        for idx, part in enumerate(snake1):

            if getfood(part,[[foodx,foody]]):
                print("snake 1 at",[foodx,foody],part)
                fakefood= True 
            
    
        for idx, part in enumerate(snake2):
            if getfood(part,[[foodx,foody]]):
                print("snake 2 at",[foodx,foody],part) 

                fakefood= True
        for idx, foods in enumerate(foodlist):
            if (foodx>=foods[0] and foodx <=(foods[0]+foodsize)) or (foods[0]>=foodx and foods[0]<=(foodx+foodsize)):
                if (foody>=foods[1] and foody <=(foods[1]+foodsize)) or (foods[1]>=foody and foods[1] <=(foody+foodsize)):
                    fakefood=True
    print("final food is",foodx,foody)

    foodlist.append((foodx,foody))
    
    for idx, foodthing in enumerate(foodlist):
        pygame.draw.rect(screen,(255,0,0),(foodthing[0],foodthing[1],foodsize,foodsize))
    




'''register pressing the exit button, used when in a seperate loop'''
def exitgame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return pygame.quit()    
    
    
gameleave=False
while not gameleave:    #This is the loop for the working game, all of what players do and interact with is in this big loop
    foodlist=[]
    exitgame()
  
    #this is where the main menu will be displayed
    screen.fill((0,0,0))
    if choose=="none":
        title=impact.render(("Generic Snake Game"),2,(255,255,255))
        screen.blit(title,(title.get_rect(center=(width/2,height/3))))
    

        smalltext("play",fourth,365)
        smalltext("Options",fourth*2,365)
        smalltext("Quit",fourth*3,365)
    

        pygame.draw.rect(screen,(255,0,0), (fourth,400,50,30)) #play
        pygame.draw.rect(screen,(0,255,0), (fourth*2,400,50,30)) #options
        pygame.draw.rect(screen,(0,0,255), (fourth*3,400,50,30)) #quit
        pygame.display.update()
        #loop for choosing an option, it stops the user here until an option is picked
    while choose== "none": 
        exitgame()
        for event in pygame.event.get():
            if click(fourth,400,50,30):
                choose="play"
            if click(fourth*2,400,50,30):
                choose = "options"
                print("options")
            if click(fourth*3,400,50,30):
                choose="quit"
                pygame.quit()
    
    if choose == "play":  #if you chose to play it changes the screen to ask what version you'd like to play or leave and go back to the main menu
        speed1=speed
        speed2=speed
        Ofoodnumber=foodnumber
        growthS1=Ogrowth
        growthS2=Ogrowth
        print("PLay")
        screen.fill((0,0,0))
        
        title=impact.render(("Play Options"),2,(255,255,255))
        screen.blit(title,(title.get_rect(center=(width/2,height/3))))        
    
        smalltext("One Player",fourth,465)
        smalltext("Back",fourth*2,465)
        smalltext("Two Player",fourth*3,465)
        
        pygame.draw.rect(screen,(255,0,0), (fourth,500,50,30))  #one player
        pygame.draw.rect(screen,(255,255,255),(fourth*2,500,50,30))  #back
        pygame.draw.rect(screen,(0,0,255), (fourth*3,500,50,30))  #two player
        pygame.display.update()
        print("HI")
        while players == "none":   #This loop stops the player till they choose an option
            exitgame()
            for event in pygame.event.get():
                if click(fourth,500,50,30):
                    players = "one"
                elif click(fourth*3,500,50,30):
                    players = "two"
                    
                elif click(fourth*2,500,50,30):
                    print("back")
                    choose="back"
                    break
            if choose=="back":
                choose= "none"
                break
                    
        if players == "one":   #plays the game with one player
            score=0
            snake=[[fourth*2,int(height*(2/3))]]
            screen.fill((0,0,0))
            title=impact.render(("Press anything to start"),2,(255,255,255))
            screen.blit(title,(title.get_rect(center=(width/2,height/3))))  
            pygame.draw.rect(screen,(p1colour), (750,533,20,20))
            pygame.display.update()
            gamestart=False
            while not gamestart:   #keeps the player from playing till it registers movement 
                exitgame()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        gameover=False
                        gamestart=True            
            
            
            
            screen.fill((0,0,0))
            pygame.display.update()
            direction="Up"
            while not gameover:  #This is where the one player game is played 
                
                for event in pygame.event.get():    
                    if event.type == pygame.QUIT:
                        pygame.quit()                    
                    
                    if event.type==pygame.KEYDOWN:    #gets player inputs
                        if (event.key == pygame.K_LEFT or event.key == pygame. K_a) and direction != "Right":
                            direction= "Left"
            
                        elif (event.key == pygame.K_RIGHT or event.key == pygame. K_d) and direction != "Left":
                            direction= "Right"
            
                        elif (event.key == pygame.K_UP or event.key == pygame. K_w) and direction != "Down":
                            direction= "Up"
            
                        elif (event.key == pygame.K_DOWN or event.key == pygame. K_s) and direction != "Up":
                            direction= "Down"\
                                
                        if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:   #this will trigger the pause 
                            pygame.draw.rect(screen,(255,0,0), (fourth*2-100,height/2-50,200,100))
                            smalltext("pause",fourth*2-35,height/2-20)
                            smalltext("click to unpause",fourth*2-100,height/2+10)
                            pygame.draw.rect(screen,(255,0,0), (50,50,50,30))
                            smalltext("Leave",50,15)
                            
                            pygame.display.update()
                            pause= True
                            while pause:  #loop for pause
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE or event.key==pygame.K_SPACE:
                                            pause = False
                                    if event.type == pygame.QUIT:
                                        pygame.quit() 
                                if click(fourth*2-100,height/2-50,200,100):
                                    pause = False
                                elif click(50,50,50,30):
                                    pause = False
                                    gameover=True
                                
                                
            
                while len(foodlist) < foodnumber:   #adds new food when needed
                    addfood(snake,[[0,0]])
                            
                screen.fill((0,0,0))
                snake= movesnake(snake,direction,speed1)
                showsnake(snake,p1colour)
                
                for idx, foodthing in enumerate(foodlist): #draws food
                    pygame.draw.rect(screen,(255,0,0),(foodthing[0],foodthing[1],foodsize,foodsize))    
                    
                if crash1(snake,height,width):   #calls the crash function
                    gameover=True
                
                if getfood(snake[0],foodlist):  #calls get food and sets things for later on if returns true
                    print("got food")
                    snake = growsnake(snake,growthS1)
                    growth+=1
                    score+=1
                    again="yes"
                    again1="yes"
                if speedincreasing and score%5==0 and again=="yes" and score !=0:  #increases speed if its supposed to
                    speed1+=1
                    again="no"
                    print(speed)
                if foodincreasing and score%5 == 0 and again1=="yes" and score !=0:  #increases food if supposed to
                    foodnumber+=1 
                    again1="no"
                    print(foodnumber)
                scorebord= "Score: "+str(score)  #updates score board
                smalltext(scorebord,width-150,10) 

                
                pygame.display.update()
                clock.tick(20)
            deathscreen=True  #stops player on death screen
            while deathscreen:
                foodnumber=Ofoodnumber #reset food number
                title=impact.render(("You Have Crashed!!"),2,(255,255,255))
                screen.blit(title,(title.get_rect(center=(width/2,height/3))))
                
                smalltext("Would you like to play again? ",fourth,600)
                pygame.draw.rect(screen,(0,0,255), (sixth*3,600,50,30))
                smalltext("leave",50,15)
                pygame.draw.rect(screen,(0,0,255), (50,50,50,30))
                
                pygame.display.update()
                
                
                if click(sixth*3,600,50,30):
                    deathscreen= False
                    choose = "play"
                    players="one"                           
                
                if click(50,50,50,30):
                    deathscreen = False
                    choose="none"
                    players="none"
                    
                
                

        elif players == "two":    # plays the game with two players
            score=0
            snake1=[[int(fourth*3),int(height/2)]]
            snake2=[[int(fourth),int(height/2)]]
            directionS1="Up"
            directionS2="Up"
            screen.fill((0,0,0))
            title=impact.render(("Press anything to start"),2,(255,255,255))
            screen.blit(title,(title.get_rect(center=(width/2,height/3))))            
            
            smalltext("player one",fourth-50,height/3)
            smalltext("player two",fourth*3-50,height/3)
            pygame.draw.rect(screen,p1colour,(fourth*3,height/2,snakesize,snakesize)) 
            pygame.draw.rect(screen,p2colour,(fourth,height/2,snakesize,snakesize)) 
            pygame.display.update()
            
            gamestart=False
            while not gamestart:   #pauses game till they start moving
                exitgame()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        gameover=False
                        gamestart=True
            
            
            screen.fill((0,0,0))
            pygame.display.update()
            while not gameover:  #This is where the two player game is played 
               
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type==pygame.KEYDOWN:  #takes inputs
                        if (event.key == pygame.K_LEFT) and directionS1 != "Right":
                            directionS1= "Left"
                
                        elif (event.key == pygame.K_RIGHT) and directionS1 != "Left":
                            directionS1= "Right"
                
                        elif (event.key == pygame.K_UP ) and directionS1 != "Down":
                            directionS1= "Up"
                
                        elif (event.key == pygame.K_DOWN) and directionS1 != "Up":
                            directionS1= "Down"
                                
                        if (event.key == pygame. K_a) and directionS2 != "Right":
                            directionS2= "Left"
                
                        elif (event.key == pygame. K_d) and directionS2 != "Left":
                            directionS2= "Right"
                
                        elif (event.key == pygame. K_w) and directionS2 != "Down":
                            directionS2= "Up"
                
                        elif (event.key == pygame. K_s) and directionS2 != "Up":
                            directionS2= "Down"    
                            
                        if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:   #registers pauses
                            pygame.draw.rect(screen,(255,0,0), (fourth*2-100,height/2-50,200,100))
                            smalltext("pause",fourth*2-35,height/2-20)
                            smalltext("click to unpause",fourth*2-100,height/2+10)
                            pygame.draw.rect(screen,(255,0,0), (50,50,50,30))
                            smalltext("Leave",50,15)
                            
                            pygame.display.update()
                            pause= True
                            while pause: #keeps the game paused
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE or event.key==pygame.K_SPACE:
                                            pause = False
                                    if event.type == pygame.QUIT:
                                        pygame.quit() 
                                if click(fourth*2-100,height/2-50,200,100):
                                    pause = False
                                elif click(50,50,50,30):
                                    pause = False
                                    gameover=True
                        else:
                    
                            if event.key==pygame.K_m and len(snake1)>5:  #speedboost for player 2
                                speed1=int(speed*1.50)
                            
                            if event.key == pygame.K_q and len(snake2)>5:
                                speed2=int(speed*1.50)
                            
                    if event.type==pygame.KEYUP:
                        if event.key==pygame.K_m:
                                speed1=speed
                        if event.key==pygame.K_q:
                                speed2=speed
                                
                                
                    if len(snake1)<=5:
                            speed1=speed
                    if len(snake2)<=5:
                            speed2=speed
                    
                if speed1>speed and len(snake1)>5:
                    snake1.pop()
                if speed2>speed and len(snake2)>5:
                    snake2.pop()
                    
                while len(foodlist) < foodnumber:  #adds more food 
                    addfood(snake1,snake2)
                
                screen.fill((0,0,0))
                
                snake1= movesnake(snake1,directionS1,speed1)
                snake2= movesnake(snake2,directionS2,speed2)
                showsnake(snake1,p1colour)                
                showsnake(snake2,p2colour)
                
                for idx, foodthing in enumerate(foodlist):
                    pygame.draw.rect(screen,(255,0,0),(foodthing[0],foodthing[1],foodsize,foodsize))                
                
                death=crash(snake1,snake2,width,height,growthS1,growthS2)   #registers crash
                if death[0] != "no one wins":
                    gameover=True
                    if death[1]==1:
                        player1score+=1
                    elif death[1] == 2:
                        player2score+=1
                if getfood(snake1[0],foodlist):  #gets food
                    snake1=growsnake(snake1,growthS1)
                    score+=1
                    growthS1+=1
                    again1="yes"
                    again="yes"
                if getfood(snake2[0],foodlist):   #gets food
                    snake2=growsnake(snake2,growthS2)
                    score+=1
                    growthS2+=1
                    again1="yes"
                    again="yes"
                if foodincreasing and score%5 == 0 and again1=="yes" and score !=0:
                    foodnumber+=1
                    again1="no"
                if speedincreasing and score%5==0 and again=="yes" and score !=0:
                    speed+=1
                    speed1+=1
                    speed2+=1
                    again="no"
                    print(speed)
               
                pygame.display.update()
                clock.tick(20)
            deathscreen=True  #keeps player on death screen till they do something
            while deathscreen:
                
                title=impact.render((death[0]),2,(255,255,255))
                screen.blit(title,(title.get_rect(center=(width/2,height/3))))
                
                smalltext("Would you like to play again? ",fourth,600)
                pygame.draw.rect(screen,(0,0,255), (fourth*2,600,50,30))
                smalltext("leave",50,15)
                pygame.draw.rect(screen,(255,0,0), (50,50,50,30))
                
                smalltext("win/loss",fourth*3,height/2)
                
                player1wins= "Player One:"+str(player2score)
                player2wins="Player Two:"+str(player1score)
                smalltext(player1wins,fourth*3,height/2+50)
                smalltext(player2wins,fourth*3,height/2+100)
                
                pygame.display.update()
                
                if click(fourth*2,600,50,30):
                    deathscreen= False
                    choose = "play"
                    players="two"
                
                if click(50,50,50,30):
                    deathscreen = False
                    choose="none"
                    players="none"   
     
    elif choose == "options":     #displays the options as labeled buttons
        print("hi")
        screen.fill((0,0,0))
        title=impact.render(("Game Options"),2,(255,255,255))
        screen.blit(title,(title.get_rect(center=(width/2,100))))              

        smalltext("back",50,15)
        pygame.draw.rect(screen,(255,0,0), (50,50,50,30))
        
        smalltext("player 1 colour",sixth+50,300)
        smalltext("player 2 colour",sixth*4+50,300)
        
        smalltext("Blue",sixth,365)
        smalltext("Green",sixth*2,365)
        smalltext("Blue",sixth*4,365)
        smalltext("Green",sixth*5,365)
        pygame.draw.rect(screen,(0,0,255), (sixth,400,50,30))   #player 1 colour=blue
        pygame.draw.rect(screen,(0,255,0), (sixth*2,400,50,30)) #player 1 colour=green 
        pygame.draw.rect(screen,(0,0,255), (sixth*4,400,50,30)) #player 2 colour=blue
        pygame.draw.rect(screen,(0,255,0), (sixth*5,400,50,30)) #player 1 colour=green
        
        smalltext("Speed: ",sixth,550)
        smalltext(" 10",sixth*3,515)
        smalltext(" 25",sixth*4,515)
        smalltext("increasing",sixth*5,515)
        pygame.draw.rect(screen,(255,0,0), (sixth*3,550,50,30)) #speed =10
        pygame.draw.rect(screen,(255,0,0), (sixth*4,550,50,30)) #speed = 25
        pygame.draw.rect(screen,(255,0,0), (sixth*5,550,50,30)) #speed = growing
        
        smalltext("food: ",sixth,700)
        smalltext("  1",sixth*2,665)
        smalltext("  5",sixth*3,665)
        smalltext("  10",sixth*4,665)
        smalltext("infinite",sixth*5,665)
        pygame.draw.rect(screen,(255,0,0), (sixth*2,700,50,30)) # food = 1
        pygame.draw.rect(screen,(255,0,0), (sixth*3,700,50,30)) # food = 5
        pygame.draw.rect(screen,(255,0,0), (sixth*4,700,50,30)) # food = 10
        pygame.draw.rect(screen,(255,0,0), (sixth*5,700,50,30)) # food = infinite 
        pygame.display.update()        
        
        options="unpicked"
        while options== "unpicked":        #loops until the players exits and saves their choices
            exitgame()
            for event in pygame.event.get(): #registers if any of the things are click
                if click(50,50,50,30):
                    print("leave")
                    options="picked"
                    choose="none"
                if click(sixth,400,50,30):
                    p1colour=(0,0,255)
                    print("p1blue")
                    pygame.draw.rect(screen,(0,255,0), (sixth*2,400,50,30))
                elif click(sixth*2,400,50,30):
                    p1colour=(0,255,0)
                    print("p1green")
                    pygame.draw.rect(screen,(0,0,255), (sixth,400,50,30))
                pygame.display.update()
                if click(sixth*4,400,50,30):
                    p2colour=(0,0,255)
                    print("p2blue")
                    pygame.draw.rect(screen,(0,255,0), (sixth*5,400,50,30))
                elif click(sixth*5,400,50,30):
                    p2colour=(0,255,0)
                    print("p2green")
                    pygame.draw.rect(screen,(0,0,255), (sixth*4,400,50,30))
                pygame.display.update()
                if click(sixth*3,550,50,30):
                    speed = 10
                    print("speed20")
                    pygame.draw.rect(screen,(255,0,0), (sixth*4,550,50,30))
                    pygame.draw.rect(screen,(255,0,0), (sixth*5,550,50,30))                    
                elif click(sixth*4,550,50,30):
                    speed = 25
                    print("speed30")
                    pygame.draw.rect(screen,(255,0,0), (sixth*3,550,50,30))
                    pygame.draw.rect(screen,(255,0,0), (sixth*5,550,50,30))                    
                elif click(sixth*5,550,50,30):
                    print("speedup")
                    pygame.draw.rect(screen,(255,0,0), (sixth*3,550,50,30))
                    pygame.draw.rect(screen,(255,0,0), (sixth*4,550,50,30))
                    speedincreasing=True
                    speed=10
                pygame.display.update()
                if click(sixth*2,700,50,30):
                    foodnumber = 1
                    print("food1")
                    pygame.draw.rect(screen,(255,0,0), (sixth*3,700,50,30))
                    pygame.draw.rect(screen,(255,0,0), (sixth*4,700,50,30)) 
                    pygame.draw.rect(screen,(255,0,0), (sixth*5,700,50,30))                    
                elif click(sixth*3,700,50,30):
                    foodnumber = 5
                    print("food5")
                    pygame.draw.rect(screen,(255,0,0), (sixth*2,700,50,30))

                    pygame.draw.rect(screen,(255,0,0), (sixth*4,700,50,30)) 
                    pygame.draw.rect(screen,(255,0,0), (sixth*5,700,50,30))                    
                elif click(sixth*4,700,50,30):
                    foodnumber = 10
                    print("food10")
                    pygame.draw.rect(screen,(255,0,0), (sixth*2,700,50,30))
                    pygame.draw.rect(screen,(255,0,0), (sixth*3,700,50,30)) 

                    pygame.draw.rect(screen,(255,0,0), (sixth*5,700,50,30))                    
                elif click(sixth*5,700,50,30):
                    print("foodup")
                    pygame.draw.rect(screen,(255,0,0), (sixth*2,700,50,30)) 
                    pygame.draw.rect(screen,(255,0,0), (sixth*3,700,50,30))
                    pygame.draw.rect(screen,(255,0,0), (sixth*4,700,50,30))
                    foodnumber=1
                    foodincreasing=True
                pygame.display.update()
        print("left options loop")
        print(foodnumber,speed,p1colour,p2colour)
pygame.quit()
print("thank you for playing my game")
