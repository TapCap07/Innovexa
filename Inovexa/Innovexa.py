# import pyttsx3
# import speech_recognition as speech
# import pygame, sys
# import time
# import keywords as keys

# screen =[]
# words=''
# state="wait"
# imagePath=""
# key_flag = 'z'

# def UI_init(g):
#     width=904
#     height=750
#     global screen
#     screen=pygame.display.set_mode( ( width, height) )
    
#     #Set a Title of Screen
#     pygame.display.set_caption('Innovexa')
#     g=pygame.image.load("images/"+ g +".png").convert_alpha()
#     screen.blit(g,(0,0))
#     pygame.display.update()
    
# def show_image(img):
#     if img!= '':        
#         image=pygame.image.load("images/"+ img +".png")
#         image=pygame.transform.scale(image, (900,350))
#         screen.blit(image,(45,145))
            
# def start_listening():
            
#     r = speech.Recognizer() 
#     with speech.Microphone() as source:
#             r.adjust_for_ambient_noise(source) 
#             print("Speak:")
#             audio = r.listen(source)
#     command=r.recognize_google(audio)
#     print("You said " + command)
#     return command 


# def parseInput(keyword):
    
#     __path =''
#     __imgpath=''
#     __state=''
#     time.sleep(0.1)
#     for i in keys.keywords:
        
#         if i in keyword :
            
#             if keys.keywords[i][0]=="img":
#                __state="showImg"
#                __imgpath=keys.keywords[i][1]
               
#             if keys.keywords[i][0]=="imgSpch":
#                __state="ImgSpch"
#                __imgpath=keys.keywords[i][2]
#                __path = keys.keywords[i][1]             
            
               
#             if keys.keywords[i][0]=="Spch":
#                __state="speak"
#                __path = keys.keywords[i][1]
               
#             if keys.keywords[i][0]=="exit":
#                __state="exit"
#                __path = keys.keywords[i][1] 
               
#     return __state,__path,__imgpath

# engine = pyttsx3.init()
# pygame.init()
# UI_init('g1')
# pygame.display.update()

# while True: 
    
    
#     try:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
# #                movie.stop()
#                 break
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_c:
#                     key_flag = 'c'
#                     print("C pressed")
                    
#                     if state=="wait":             
#                         if key_flag == 'c':
#                             UI_init('g2')
#                 pygame.display.update()
                
#                 state="listen"
                
#         if state=="listen":            
#             words = start_listening().lower()
#             parsed = parseInput(words)
                        
#             if parsed[0] == "showImg":
#                 UI_init('g1')
                
#                 show_image(parsed[2])
#                 state="reset"
                
#             elif parsed[0]=="speak":
#                 UI_init('g1')
                
#                 engine.say(parsed[1])
#                 engine.runAndWait() 
#                 state="reset"
                
#             elif parsed[0]=="ImgSpch":
#                 UI_init('g1')
                
#                 show_image(parsed[2])
#                 pygame.display.update()
                
#                 engine.say(parsed[1])
#                 engine.runAndWait()
#                 state="reset"
                
#             elif parsed[0]=="exit":
                            
#                 engine.say(parsed[1])
#                 engine.runAndWait()
#                 break
#             else:
#                 UI_init('g1')
#                 state ="reset"
            
#         if state=="reset":
#             key_flag='z'
#             state="wait" 
   
#         pygame.display.update()
#         time.sleep(0.1)
        
   
#     except speech.UnknownValueError:
#         print("Could not understand audio")
#     except speech.RequestError as e:
#         print("Could not request results; {0}".format(e))
#     except KeyboardInterrupt:
#         break



import speech_recognition as speech
import pyttsx3
import pygame
import time
import keywords as keys

#Initialize the Speech Generation Library
engine=pyttsx3.init()
engine.setProperty('rate',200)

#Initialize Pygame
pygame.init()

#Create Screen with size 900x600
width=900
height= 600
screen=pygame.display.set_mode( ( width, height) )

pygame.display.set_caption('Innovexa')

#Display the Background Image
bg=pygame.image.load("images/bg1.jpg")
image1=pygame.transform.scale(bg, (900,600))
screen.blit(image1,(0,0))
pygame.display.update()

# sport={"cricket":["Spch","Cricket is the most popular game in the world"],
#        "football":["Img","football"],
#        "badminton":["ImgSpch","It is one of the games in olympics","badminton"],
#        "tennis":["consoleText","Tennis can be played on different types of grounds"],
#        "basketball":["Spch","Each team of basketball has 5 players"],
#        "hockey":["ImgSpch","Hockey is a national sport of India","hockey"],
#        "swimming":["ImgSpch","Swimming is a fun sport","swimming"],
#        "squash":["Video","videos/AyushSpandan.mp4"],
#        "athletics":["Video","videos/Aneesh & Yash.mp4"],
#        "stop":["stop"],
#        "exit":["exit","Thanks for Interaction"]}

activate="none"
exitstatus="no"

while True:
    try:
        pygame.display.update()
        for event in pygame.event.get():
            #Event to Quit Pygame Window
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            #To Read whether 'c' key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    activate = 'c'
                    print("C pressed")
                    
                    
        #If 'c' key is pressed
        if activate=='c':
            #Change the background image to Listening Image
            listenImg=pygame.image.load("images/bg2.jpg").convert_alpha()
            image1=pygame.transform.scale(listenImg, (900,600))
            screen.blit(image1,(0,0))
            pygame.display.update()
            
            #Start Listening the User Voice Input
            r=speech.Recognizer()
            
            with speech.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Speak:")
                    audio=r.listen(source)
                #Convert Voice Commands to Text
            command=r.recognize_google(audio).lower()
                
            print("You said: "+command)
            
            #Search each keyword in the dictionary one-by-one
            for keyword in keywords:
                
                #if one of the keyword in the dictionary is in 
                #User Input
                if keyword in command:
                    
                    #Check the response type for that keyword
                    
                    #Speech Response Type
                    if keywords[keyword][0]=="Spch":
                        engine.say(keywords[keyword][1])
                        engine.runAndWait()
                        
                    #Console Text Response Type
                    if keywords[keyword][0]=="consoleText":
                        print(keywords[keyword][1])
                    
                    #Image Response type
                    if keywords[keyword][0]=="Img":
                        image=pygame.image.load("images/"+sport[keyword][1]+".jpg").convert_alpha()
                        image1=pygame.transform.scale(image, (813,375))
                        screen.blit(image1,(45,145))
                        
                        pygame.display.update()
                        time.sleep(15)
                        
                    #Image & Speech Response type
                    if keywords[keyword][0]=="ImgSpch":
                        #Showing Image
                        image=pygame.image.load("images/"+keywords[keyword][2]+".jpg").convert_alpha()
                        image1=pygame.transform.scale(image, (813,375))
                        screen.blit(image1,(45,145))
                      
                        pygame.display.update()
                        
                        #Saying Text
                        engine.say(keywords[keyword][1])
                        engine.runAndWait()
                        
                    if keywords[keyword][0]=="Video":
#                       
                        # creating vlc media player object
                        media = vlc.MediaPlayer(keywords[keyword][1])
#                        media = vlc.MediaPlayer("videos/AyushSpandan.mp4")
 
                        # start playing video
                        media.play()
                        
                    if keywords[keyword][0]=="stop":
                        media.stop()
                        
                     
                    if sport[keyword][0]=="exit":
                        engine.say(keywords[keyword][1])
                        engine.runAndWait()
                        exitstatus="yes"
                        break
            #if 'exit' in command then break from while loop        
            if exitstatus=="yes":
                    pygame.quit()
                    break
            #Reset the UI to get further inputs    
            activate="none" 
            bg=pygame.image.load("images/bg1.jpg").convert_alpha()
            image1=pygame.transform.scale(bg, (900,600))
            screen.blit(image1,(0,0))
        
    #Stop Taking Voice Commands
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break
    

           
                



