from blackjack import Blackjack 
from writeFile import WriteFile

bj = Blackjack()

i = 0
y = 5000

#create the log
writeFile = WriteFile()
headers = ['game_status','dealer_total', 'dealer_cards','player_name', 'player_total', 'player_cards', 'player_wager', 'player_balance','running_count','deck_remaining', 'true_count', 'remaining_cards']
writeFile.createFile(headers)


while i < y:
    bj.playHand()
    i += 1
    for gamer in bj.gamePlayers:
        print gamer.name+ ' ' + str(gamer.balance)