# CrosswordSolver

Solves [Multiplayer Crossword](https://multicrosser.chriszetter.com/) using Hit and Trial Method.

The code is adequately commented and will be easy to modify and make it work with other crossword puzzles too.

---

_Real Time Video, Not Sped Up:_
<br>
<img src="https://media.giphy.com/media/U4jM2Jyl300oypqrW8/giphy.gif" width="70%"/>

See Whole Video [Here](https://gfycat.com/forkededibleeasteuropeanshepherd)



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
`python3 dino.py`



## Extra:

Edit the `p.PAUSE=0` to edit the time between the clicks , I recommend you start with 0.25 and reduce it from there<br>

Edit the `monitor = {"top":270,"left":20,"width":20,"height":20}` to change the detection box for the first box of the crossword, try to make the detection box small and prevent the numbers on the crossword<br>

Change the `os.system('clear')` to `os.system('cls')` if you are on windows.<br>



## Thanks:

Special thanks to [Chris Zetter](https://github.com/zetter) for making an awesome multiplayer crossword game

If you like this Project don't forget to go and star his [repository](https://github.com/zetter/multicrosser) too.

