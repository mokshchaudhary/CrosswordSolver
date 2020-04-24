# CrosswordSolver

Solves [Multiplayer Crossword](https://multicrosser.chriszetter.com/) using Hit and Trial Method.

The code is adequately commented and will be easy to modify and make it work with other crossword puzzles too.

---

_Real Time Video, Not Sped Up:_
<br>
<img src="https://media.giphy.com/media/U4jM2Jyl300oypqrW8/giphy.gif" width="70%"/>

See Full Video [Here](https://gfycat.com/forkededibleeasteuropeanshepherd)



## How it Works

![working](https://i.imgur.com/49sJnRH.jpg)

1. Takes the screenshot of the first box of the crossword
2. Does Image processing on it and then checks if it is black, filled or empty. (using `np.mean`)
3. If the box is empty it fills it with the first letter according to the frequency of alphabet in English language
4. It then clicks the `Check All` button and moves forward to next box.
5. This is repeated for all the alphabets for all the empty boxes until no box remains empty.

**Note:** Yes I know that it can just click the `Check All` button once after all the boxes are filled with the alphabet and it will make the program faster.  I just found this approach a bit more pretty : )   Fell free to change it , in my testing it was about 4 sec faster.

Got more Ideas ? Feel free to dive into the code.



## Perquisite:

 - ### Python:
     ##### Numpy
     `pip install numpy`
     
     ##### Pyautogui
     `pip install pyautogui`
     ##### OpenCV
     `pip install opencv-python`
     ##### Mss
     `pip install mss`



## Usage:

Open the [Crossword](https://multicrosser.chriszetter.com/) Game<br>
Start the python program by typing this in command prompt:<br>
`python3 cross.py`



## Extra:

Edit the `p.PAUSE=0` to edit the time between the clicks , I recommend you start with 0.25 and reduce it from there<br>

Edit the `monitor = {"top":270,"left":20,"width":20,"height":20}` to change the detection box for the first box of the crossword, try to make the detection box small and prevent the numbers on the crossword<br>

Change the `os.system('clear')` to `os.system('cls')` if you are on windows.<br>



## Thanks:

Special thanks to [Chris Zetter](https://github.com/zetter) for making an awesome multiplayer crossword game

If you like this Project don't forget to go and star his [repository](https://github.com/zetter/multicrosser) too.

