class Game:
    def __init__(self):
        playing = True
        
        while playing:
            self.deck = classes.Deck()
            self.deck.shuffle()
            
            self.player_hand = classes.Hand()
            self.dealer_hand = classes.Hand(dealer=True)
            
            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())
            print("Your hand is:")
            self.player_hand.display()
            print()
            print("Dealer's hand is:")
            self.dealer_hand.display()

            game_over = False
            while not game_over:
                player_has_blkjk,dealer_has_blkjk = self.check()
                if player_has_blkjk or dealer_has_blkjk:
                    game_over = True
                    self.show_blackjack_results(player_has_blkjk,dealer_has_blkjk)
                    continue
                choice = input("PLease choose [Hit/Sick]: ").lower()
                while not choice in ["hit","h","stick","s"]:
                    choice = input("PLease choose [Hit/Sick]: ").lower()
                if choice in ["hit","h"]:
                    self.player_hand.add_card(self.deck.deal() )
                    self.player_hand.display()
                    if self.player_hand.get_value() > 21:
                        print("You have lost!")
                        has_won = True  #dealer won
                        game_over = True
                else:
                    print("Final Results")
                    print("Your hand:", self.player_hand.get_value())
                    print("Dealer's hand:", self.dealer_hand.get_value())
                    if self.player_hand.get_value() > self.dealer_hand.get_value():
                        print("You Win!")
                    else:
                        print("Dealer Wins!")
                        has_won = True
                    game_over = True
            again = input("Play Again? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter Y or N ")
            if again.lower() == "n":
                print("Thanks for playing!")
                playing = False
            else:
                has_won = False
    def check(self):
        player = self.player_hand.get_value() == 21
        dealer = self.dealer_hand.get_value() == 21
        return player,dealer
    def show_blackjack_results(self, player_has_blackjack,dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack! Draw!")
        elif player_has_blackjack:
            print("You have blackjack! You win!")
        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")
        
        
if __name__ == '__main__':
    import classes
    game = Game()