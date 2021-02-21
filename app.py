from flask import Flask, redirect, url_for, render_template, request
import random
import sys

app = Flask(__name__)

matrix = [[['do 10 jumping jacks', False, 'grey.png'], ['find a dog', False, 'grey.png'], ['find a watch', False, 'black.png'], ['find an old coin', False, 'black.png'], ['budget your money', False, 'black.png'], ['do a quick jog', False, 'black.png'], ['take a deep breathe', False, 'black.png'], ['eat some snacks', False, 'grey.png'], ['find a green vegetable', False, 'grey.png']], 
          [['draw a stickman', False, 'grey.png'], ['listen to music', False, 'black.png'], ['watch a streamer', False, 'white.png'], ['search for a Leonardo DiCaprio movie', False, 'red.png'], ['play a game of chess', False, 'red.png'], ['talk with your family', False, 'white.png'], ['play a family game', False, 'white.png'], ['find some cards', False, 'black.png'], ["solve a rubik's cube", False, 'grey.png']], 
          [['learn a new skill', False, 'black.png'], ['experiment with different spices', False, 'red.png'], ['drink a cup of water', False, 'white.png'], ['write down your dreams', False, 'red.png'], ['eat a piece of chocolate', False, 'red.png'], ['make a toothpick figure', False, 'white.png'], ['read a book', False, 'red.png'], ['find a log', False, 'white.png'], ['make a snowball', False, 'black.png']], 
          [['read about igloos', False, 'black.png'], ['watch an NBA game', False, 'red.png'], ['message a friend', False, 'red.png'], ['get some sun light', False, 'white.png'], ['jump up and down 5 times', False, 'white.png'], ['join a type racer game', False, 'red.png'], ['write a cursive letter', False, 'red.png'], ['what is 11 + 16', False, 'white.png'], ['find a nutrition label', False, 'black.png']], 
          [['complete a jigsaw puzzle', False, 'grey.png'], ['play a brain teaser', False, 'black.png'], ['write down gift ideas', False, 'black.png'], ['learn about wellness', False, 'black.png'], ['wash your hands', False, 'black.png'], ['do something creative', False, 'black.png'], ['watch a PewDiePie YouTube video', False, 'black.png'], ['message your shoulders', False, 'black.png'], ['relax your toes', False, 'grey.png']], 
          [['run up and down some stairs', False, 'grey.png'], ['find medicine or supplements', False, 'grey.png'], ['watch a documentary', False, 'black.png'], ['find cooking oil', False, 'white.png'], ['make salt water', False, 'white.png'], ['find a single sock', False, 'white.png'], ['turn on some lights', False, 'black.png'], ['find a ball', False, 'grey.png'], ['roll your eyes', False, 'grey.png']], 
          [['get a bottle of red.png bull', False, 'grey.png'], ['search up bitcoin', False, 'grey.png'], ['take a shower', False, 'black.png'], ['write something on a calendar', False, 'white.png'], ['get a stuffed animal', False, 'white.png'], ['sanitize your hands', False, 'white.png'], ['put a book into a back pack', False, 'black.png'], ['find a phone', False, 'grey.png'], ['put a coin into a wallet', False, 'grey.png']], 
          [['touch a figurine', False, 'grey.png'], ['fill a bottle up with water', False, 'grey.png'], ['play a note on a piano', False, 'black.png'], ['draw a digital art', False, 'white.png'], ['fold a paper air plane', False, 'white.png'], ['bounce a basketball', False, 'white.png'], ['spin your ankles 10 times', False, 'black.png'], ["find the nearest McDonald's", False, 'grey.png'], ['print a blank page', False, 'grey.png']], 
          [['find an electricity outlet', False, 'grey.png'], ['write a sentence', False, 'grey.png'], ['look at the clouds', False, 'grey.png'], ['find a dead tree branch', False, 'black.png'], ['touch soap', False, 'black.png'], ['find a reciept', False, 'black.png'], ['build some legos', False, 'grey.png'], ['read Harry Potter books', False, 'grey.png'], ['mop the floor', False, 'grey.png']]]

original = [['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', "qmark.png", "qmark.png"], 
          ['qmark.png', 'qmark.png', 'qmark.png', "qmark.png", "qmark.png", "qmark.png", "qmark.png", "qmark.png", "qmark.png"], 
          ['qmark.png', "qmark.png", 'qmark.png', "qmark.png", "qmark.png", "qmark.png", "qmark.png", "qmark.png", "qmark.png"], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png'], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png'], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png'], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png'], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png'], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png']]

answer = [['grey.png', 'grey.png', 'black.png', 'black.png', 'black.png', 'black.png', 'black.png', "grey.png", "grey.png"], 
           ['grey.png', 'black.png', 'white.png', "red.png", "red.png", "white.png", "white.png", "black.png", "grey.png"], 
           ['black.png', "red.png", 'white.png', "red.png", "red.png", "white.png", "red.png", "white.png", "black.png"], 
           ['black.png', 'red.png', 'red.png', 'white.png', 'white.png', 'red.png', 'red.png', 'white.png', 'black.png'], 
           ['grey.png', 'black.png', 'black.png', 'black.png', 'black.png', 'black.png', 'black.png', 'black.png', 'grey.png'], 
           ['grey.png', 'grey.png', 'black.png', 'white.png', 'white.png', 'white.png', 'black.png', 'grey.png', 'grey.png'], 
           ['grey.png', 'grey.png', 'black.png', 'white.png', 'white.png', 'white.png', 'black.png', 'grey.png', 'grey.png'], 
           ['grey.png', 'grey.png', 'black.png', 'white.png', 'white.png', 'white.png', 'black.png', 'grey.png', 'grey.png'], 
           ['grey.png', 'grey.png', 'grey.png', 'black.png', 'black.png', 'black.png', 'grey.png', 'grey.png', 'grey.png']]

colours = [['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', "qmark.png", "qmark.png"], 
          ['qmark.png', 'qmark.png', 'qmark.png', "qmark.png", "qmark.png", "qmark.png", "qmark.png", "qmark.png", "qmark.png"], 
          ['qmark.png', "qmark.png", 'qmark.png', "qmark.png", "qmark.png", "qmark.png", "qmark.png", "qmark.png", "qmark.png"], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png'], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png'], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png'], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png'], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png'], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png']]

def func(i, j, status):
  global matrix
  matrix[i][j][1] = status

  if matrix[i][j][1] == True:
    colours[i][j] = matrix[i][j][2]
    return matrix[i][j]
  else:
    colours[i][j] = "qmark.png"
    return [matrix[i][j][0], matrix[i][j][1], None]

def writeAnswer():
  for i in range(0, 9):
    for j in range(0,9):
      colours[i][j] = answer[i][j]

def resetAnswer():
  for i in range(0, 9):
    for j in range(0,9):
      colours[i][j] = original[i][j]

# @app.route('/', methods=['POST', 'GET'])
# def index():
    
#     if request.method == 'POST':
#         try:
#             pos = request.form["content"]
#             x = pos.split(" ")[0]
#             y = pos.split(" ")[1]
#             print(pos)
#             print(x)
#         except:
#             print("ERROR")
        
#         return render_template('index.html')
#     return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def check():
    
    if request.method == "POST":
        result = ["HEYY", False, "qmark.png"]
        try:
          pos = request.form["content"].split(" ")
          print(pos)
          x = int(pos[0])
          y = int(pos[1])
          state = pos[2]
          if(state == "True"):
            result = func(x,y,True)
          elif(state == "False"):
            result = func(x,y,False)
          elif(state == "Complete"):
            writeAnswer()
          else:
            resetAnswer()
          print(result[2])
        except:
          print("ERROR")
        
        return render_template("index.html", colour00 = colours[0][0], colour01 = colours[0][1], colour02 = colours[0][2], colour03 = colours[0][3], colour04 = colours[0][4], colour05 = colours[0][5], colour06 = colours[0][6], colour07 = colours[0][7], colour08 = colours[0][8],
        colour10 = colours[1][0], colour11 = colours[1][1], colour12 = colours[1][2], colour13 = colours[1][3], colour14 = colours[1][4], colour15 = colours[1][5], colour16 = colours[1][6], colour17 = colours[1][7], colour18 = colours[1][8], 
        colour20 = colours[2][0], colour21 = colours[2][1], colour22 = colours[2][2], colour23 = colours[2][3], colour24 = colours[2][4], colour25 = colours[2][5], colour26 = colours[2][6], colour27 = colours[2][7], colour28 = colours[2][8],
        colour30 = colours[3][0], colour31 = colours[3][1], colour32 = colours[3][2], colour33 = colours[3][3], colour34 = colours[3][4], colour35 = colours[3][5], colour36 = colours[3][6], colour37 = colours[3][7], colour38 = colours[3][8],
        colour40 = colours[4][0], colour41 = colours[4][1], colour42 = colours[4][2], colour43 = colours[4][3], colour44 = colours[4][4], colour45 = colours[4][5], colour46 = colours[4][6], colour47 = colours[4][7], colour48 = colours[4][8],
        colour50 = colours[5][0], colour51 = colours[5][1], colour52 = colours[5][2], colour53 = colours[5][3], colour54 = colours[5][4], colour55 = colours[5][5], colour56 = colours[5][6], colour57 = colours[5][7], colour58 = colours[5][8],
        colour60 = colours[6][0], colour61 = colours[6][1], colour62 = colours[6][2], colour63 = colours[6][3], colour64 = colours[6][4], colour65 = colours[6][5], colour66 = colours[6][6], colour67 = colours[6][7], colour68 = colours[6][8],
        colour70 = colours[7][0], colour71 = colours[7][1], colour72 = colours[7][2], colour73 = colours[7][3], colour74 = colours[7][4], colour75 = colours[7][5], colour76 = colours[7][6], colour77 = colours[7][7], colour78 = colours[7][8],
        colour80 = colours[8][0], colour81 = colours[8][1], colour82 = colours[8][2], colour83 = colours[8][3], colour84 = colours[8][4], colour85 = colours[8][5], colour86 = colours[8][6], colour87 = colours[8][7], colour88 = colours[8][8], description=result[0])

    return render_template("index.html", colour00 = colours[0][0], colour01 = colours[0][1], colour02 = colours[0][2], colour03 = colours[0][3], colour04 = colours[0][4], colour05 = colours[0][5], colour06 = colours[0][6], colour07 = colours[0][7], colour08 = colours[0][8],
        colour10 = colours[1][0], colour11 = colours[1][1], colour12 = colours[1][2], colour13 = colours[1][3], colour14 = colours[1][4], colour15 = colours[1][5], colour16 = colours[1][6], colour17 = colours[1][7], colour18 = colours[1][8], 
        colour20 = colours[2][0], colour21 = colours[2][1], colour22 = colours[2][2], colour23 = colours[2][3], colour24 = colours[2][4], colour25 = colours[2][5], colour26 = colours[2][6], colour27 = colours[2][7], colour28 = colours[2][8],
        colour30 = colours[3][0], colour31 = colours[3][1], colour32 = colours[3][2], colour33 = colours[3][3], colour34 = colours[3][4], colour35 = colours[3][5], colour36 = colours[3][6], colour37 = colours[3][7], colour38 = colours[3][8],
        colour40 = colours[4][0], colour41 = colours[4][1], colour42 = colours[4][2], colour43 = colours[4][3], colour44 = colours[4][4], colour45 = colours[4][5], colour46 = colours[4][6], colour47 = colours[4][7], colour48 = colours[4][8],
        colour50 = colours[5][0], colour51 = colours[5][1], colour52 = colours[5][2], colour53 = colours[5][3], colour54 = colours[5][4], colour55 = colours[5][5], colour56 = colours[5][6], colour57 = colours[5][7], colour58 = colours[5][8],
        colour60 = colours[6][0], colour61 = colours[6][1], colour62 = colours[6][2], colour63 = colours[6][3], colour64 = colours[6][4], colour65 = colours[6][5], colour66 = colours[6][6], colour67 = colours[6][7], colour68 = colours[6][8],
        colour70 = colours[7][0], colour71 = colours[7][1], colour72 = colours[7][2], colour73 = colours[7][3], colour74 = colours[7][4], colour75 = colours[7][5], colour76 = colours[7][6], colour77 = colours[7][7], colour78 = colours[7][8],
        colour80 = colours[8][0], colour81 = colours[8][1], colour82 = colours[8][2], colour83 = colours[8][3], colour84 = colours[8][4], colour85 = colours[8][5], colour86 = colours[8][6], colour87 = colours[8][7], colour88 = colours[8][8])


if __name__ == "__main__":
    app.run(debug=True, port=8080)

#pip3 install virtualenv
#virtualenv env
#source env/bin/activate
#pip3 install flask 
# TO kill as port -> sudo lsof -iTCP:8080 -sTCP:LISTEN

