class Game:
    stone = 30 # 石の総数
    lowerLimit = 2 # 取る石の最小値
    upperLimit = 4 # 取る石の最大値
    turn = None # CPかユーザのターン決定
    
    def __init__(self):
        self.describeGame()
        self.start()
    
    def describeGame(self):
        # ゲーム説明の表示。\をプログラムの途中で書くと複数行に書ける。
        print('交互に' + str(self.lowerLimit) + '-' + str(self.upperLimit) + \
            '個の石をとっていき、最後の石をとったほうが負けです。')
    
    # 石が残っているかどうかチェックする関数＝勝敗を見る関数
    # playerは手番（youのときはあなた）を示す
    # stoneCountは石の総数、引数stoneを与える
    def checkStone(self):
        # 石の総数が0以下なら負け。
        if (self.stone <= 0):
            if (self.turn == 'you'): # 0以下のときのプレイヤーがあなたかどうか。
                print('あなたの負けです...')
            else:
                print('素晴らしい! あなたの勝ちです.')
            return True # 勝敗がついたらTrueを返す。
        else:
            return False # 勝敗がついていなければFalseを返す。

    # あなたが石を取る関数
    def yourTurn(self):
        your = int(input('あなたはいくつ取りますか? '))
        # ゲームで指定した最小値、最大値か確認する。
        if (your < self.lowerLimit or your > self.upperLimit):
            print('それはダメ!')
            return False # ここでは操作が完了しなければFalseを返して関数の実行は中断（returnの効果）
        self.stone -= your # 石の総数から選択した数を抜き取る
        print('あなたは ' + str(your) + ' 個とりました.')
        return True # ここでは操作が無事に完了すればTrueを返す。

    # 私（コンピューター）が石を取る関数
    def myTurn(self):
        mine = (self.stone - self.lowerLimit) % (self.lowerLimit + self.upperLimit) # 私がとる石を算出
        if (mine < self.lowerLimit):
            mine = self.lowerLimit # 算出した値が最小値より小さければ値を最小値に変更
        if (mine > self.upperLimit):
            mine = self.upperLimit # 算出した値が最大値より大きければ値を最大値に変更
    
        print('私は ' + str(mine) + ' 個とります.')
        self.stone -= mine # 石の総数から選択した数を抜き取る

    def start(self):
        # このプログラムの本体
        # 石が0個になるまで続ける
        while(self.stone > 0):

            # あなたの手番-------------------------------------------------------
            print(str(self.stone) + ' 個 残っています.') # 石の数を表示

            # あなたの石を取る関数の操作をして結果がFalseか確認してFalseなら実行
            if (self.yourTurn() == False):
                continue # 先頭に戻る

            # 石の総数をチェック
            self.turn = 'you'
            if (self.checkStone()):
                if(self.isRestart()):
                    # 各値を初期化してから再度start()を実行
                    self.stone = 30
                    self.turn = None
                    self.start()
                else:
                    print('--おしまい.')

            # コンピューターの手番-----------------------------------------------
            print(str(self.stone) + ' 個 残っています.') # 石の数を表示

            # コンピューターの石を取る関数
            self.myTurn()

            # 石の総数をチェック
            self.turn = 'me'
            if (self.checkStone()):
                if(self.isRestart()):
                    # 各値を初期化してから再度start()を実行
                    self.stone = 30
                    self.turn = None
                    self.start()
                else:
                    print('--おしまい.')
                
    def isRestart(self):
        while(1):
            rslt = input('再開しますか? (y/n) ')
            if(rslt != 'y' and rslt != 'n'):
                print("不正な入力です.")
            else:
                break
        
        if(rslt == 'y'):
            return True # 再度start()を実行させる
        else:
            return False # ゲームを終了させる
            
    def __str__(self):
        return('stone:' + str(self.stone) + '\n' 
               'upperLimit:' + str(self.upperLimit) + '\n' 
               'lowerLimit:' + str(self.lowerLimit) + '\n') 
    