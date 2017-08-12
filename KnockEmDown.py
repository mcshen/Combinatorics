from random import *

TOTAL_PROBABILITY = 100


class Gameboard:

    def __init__(self):
        """initializes the gameboard class
        """
        self.probabilityVector = []
        self.players = []

    def __repr__(self):
        """makes a visual representation for the gameboard
        """

        boardImage = ''

        for x in range(len(self.players)):
            boardImage += self.players[x]
            boardImage += '\n'

        return boardImage

    def roll(self):
        """ chooses a random row to delete a token from
            probability based on the probability vector
        """
        rollChoices = []
        for i in range(len(self.probabilityVector)):
            rollChoices += [i]*int(self.probabilityVector[i])
        index = choice(rollChoices)

        return index


    def playGame(self, numPlayers, numTokens, probabilityVector):
        """ plays a game of Knock 'em Down, taking play parameters as inputs
            numPlayers is an int specifying the number of players
            numTokens is an int specifying the number of Tokens to be used
            probabilityVector is the list of probabilites to be used
        """
        numPlayers = numPlayers
        #user choose a probability distribution and numTokens
        self.numTokens = numTokens
        self.probabilityVector = probabilityVector
        while sum(self.probabilityVector) != TOTAL_PROBABILITY:
            print 'the probabilites must sum to ', TOTAL_PROBABILITY
            self.probabilityVector = input('please input a probability vector ')


        #create players
        for i in range(numPlayers):
            printThis = 'name Player' +str(i) + ' '
            playerName = raw_input(printThis)
            print playerName
            tokenAllocation = input('enter an allocation for your tokens ')
            while sum(tokenAllocation) != self.numTokens\
                or len(tokenAllocation) != len(probabilityVector):
                tokenAllocation = 
                    input('allocate '+ str(self.numTokens) +' tokens ')
            self.players += [Player(playerName, tokenAllocation)]
            print self.players[i]

        #play the game
        wins = ''
        while(wins == ''):
            token = self.roll()
            print token, ' was rolled'
            for player in self.players:
                player.removeToken(token)
                if player.hasWon():
                    wins += player.name + ' '
                    print player.name + ' wins!'
                    break
        if len(wins) > 1:
            print "it's a tie! these", len(wins), "players are the winners:"
            print wins
        print "congratulations!"


        

class Player:
    """the player for the KnockEmDown game
    """

    def __init__(self, name, tokenAllocation):
        """initializes the program class
        """
        self.tokenAllocation = tokenAllocation
        self.tokenCount = sum(tokenAllocation)
        self.name = name

    def __repr__(self):
        """makes a visual representation for the player's board
        """

        boardImage = self.name + '\n'

        for x in range(len(self.tokenAllocation)):
            boardImage += str(x) + ': ' + 'x'* self.tokenAllocation[x]
            boardImage += '\n'
        boardImage+=self.name+' has '+str(self.tokenCount)+' tokens remaining.'
        return boardImage

    def removeToken(self, index):
        """ removes a token from the pile in space specified by the 
            input index
        """
        if self.tokenAllocation[index] > 0:
            self.tokenAllocation[index] -= 1
            self.tokenCount -= 1

    def hasWon(self):
        """ returns whether the player has emptied its board """
        return self.tokenCount == 0

def rateWLD(board):
    """ calculates the expected win-lose-draw probability in a 
        2-player game
    """
    if len(board.players) != 2:
        print "please use a 2-player board"
        return
    WLD = rateWLDHelper(board.players[0], 
                        board.players[1], board.probabilityVector)
    print "This player is expected to win" WLD[0] "% of games"
    print "lose" WLD[1] "% of games"
    print "and draw" WLD[2] "% of games"
    print "against this opponent"
    return

def rateWLDHelper(p1, p2, vector):
    """ helper function for rateWLD()
        recursively calculates the WLD rates for the matchup.
    """
    #base cases
    if p1.hasWon():
        return [100.,0,0]
    elif p2.hasWon:
        return [0,0,100.]
    elif p1.tokenAllocation == p2.tokenAllocation:
        return [0,100.,0]

    #recursive step
    """
    else:
        WLD = [0,0,0]
        for p in vector:
            WLD += addLists(WLD,
            constMult(vector[i],rateWLDHelper(p1.removeToken[i],p2.removeToken[i],vector)))
        return WLD
    """
        #TODO: change WLD type to matrix
    return [0,0,0]

def addLists(L1, L2):
    "adds two lists as vectors. assumes lists to be of same len"
    newL = []
    for i in range(len(L1)):
        newL[i]=L1[i]+L2[i]:
    return newL
def constMult(c,L):
    "multiplies a constant by a vector, represented as a list"
    newL = []
    for i in range(len[L]):
        newL += c*L[i]
    return newL







