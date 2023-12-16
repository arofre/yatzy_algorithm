from random import randint

class Game:
    def __init__(self):
        self.player = Player(1)
        self.ai_player = AIPlayer(2)
        self.player_list = [self.player, self.ai_player]

        self.turn = None

        self._run()

    def _run(self):#
        
        self.turn = max(self.player, self.ai_player, key=lambda x: x._roll_dice())

        while True:

            while self.turn.throws_left > 0:

                if self.turn.throws_left == 3:
                    self.turn.dices = [Player._roll_dice() for throws in range(5)]
                else:
                    self.turn.throw()

                    print(self.turn.dices)
                self.turn.throws_left -= 1



    def _change_turn(self):
        turn_idx = self.turn.idx % 2 + 1
        self.turn = self.player_list[turn_idx - 1]




            


class Player:
    def __init__(self, idx):
        self.idx = idx
        self.throws_left = 3
        self.dices = None

    def __str__(self):
        return_string = f'Player index: {str(self.idx)}'
        if isinstance(self, AIPlayer):
            return_string += ", AI controlled"
        return return_string
    
    @staticmethod
    def _roll_dice():
        return randint(1,6)
    
    def throw(self):
        print(f'Which dices to throw away? \n{self.dices}')

        while True:
            try:
                not_kept = eval(input('Input indexes in terms of a list: '))
                if type(not_kept) != list:
                    raise ValueError
                
                if any(element > 5 for element in not_kept):
                    raise IndexError

                break

            except KeyboardInterrupt:
                print('\nProgram terminated by user.')
                exit()
            except (IndexError):
                print('Index was above 5')
            except:
                print('That was not a valid list. Please try again.')

        for idx, item in enumerate(not_kept):
            not_kept[idx] = item - 1

        throw_amount = 5 - len(not_kept)

        for not_kept_dice_index in not_kept:
            self.dices[not_kept_dice_index] = 0
        
        self.dices.sort(reverse = True)

        new_thrown_dices = [Player._roll_dice() for i in range(5 - throw_amount)]
        
        for empty_dice_positions in range(5-len(new_thrown_dices), 5):
            self.dices[empty_dice_positions] = new_thrown_dices.pop()


class AIPlayer(Player):
    def __init__(self, idx):
        super().__init__(idx)

        self.next_move = None



if __name__ == "__main__":
    game = Game()
    player = game.player
    ai_player = game.ai_player
