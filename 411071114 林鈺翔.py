import numpy as np
from math import log
import cv2
#import matplotlib.pyplot as plt
#import pandas as pd
#import pygame
import prettytable as pt
import random
import time
import sys
import os
#from  moviepy.editor import *
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tqdm import tqdm 
#import wx
   
#a, b, c, d = 10, 100, 1000, 10000  #sells price
#abuy, bbuy, cbuy, dbuy = 1, 1, 1, 1, #import prise
#a_num, b_num, c_num, d_num = 0, 0, 0, 0 #Purchase quantity

packet = 10000 #財產 
day = 0
power = 6 #體力
x, y = 0, 0 #按鈕編號
cus = 0 #顧客
customer = {} #顧客性質儲存
good = {}
year_c, month_c, day_c, week_c = 2000, 1, 1, 6
#g_tb = ['Goods','Pen','Food','Hat','Jewelry']
p_tb = ["Price",0,0,0,0]
c_tb = ["Count",0,0,0,0]

class Customers_:
    def __init__(self, name, freq, is_come, c_buy, d_buy):
        self.name = name
        self.is_come = is_come
        self.freq = freq
        self.a_buy = 1
        self.b_buy = 1
        self.c_buy = c_buy
        self.d_buy = d_buy

class Goods_:
    def __init__(self, name, num, store_price, in_prise, good_kg, willbuy, frequency, alternatives):
                       #名稱, 數量, 販售價格,    進貨價格,  商品重量, 進店後購買率,購買平率(幾天買一次), 替代商品造成影響
        self.name = name
        self.num = num
        self.store_price = store_price
        self.in_prise = in_prise 
        self.good_kg = good_kg
        self.wiilbuy = willbuy
        self.frequency = frequency
        self.alternatives = alternatives 
        
class Store(): 
    #顧客數量
    def customer_n(cus,day):  #潛在客戶(知道有這間店的人)
        if day > 50 or cus > 1000:
            return cus +  random.randint(0,3)
        elif day % 5 == 0 and day < 61 and day != 0:
            return cus +  random.randint(0, int(log(day+1, 2.2))) + random.randint(3,6)
        elif day<30:
            return cus +  random.randint(0, int(log(day+1, 2.2)))
        else:
            return cus +  random.randint(0, int(log(day+1, 2)))
        
    #def customer_come(day, weather, ): #會進商店的顧客

    
    #inventory_cost 存貨成本
    def storehouse():   #存貨倉庫
        return 75
    
    def interest():     #銀行利息
        return 1.00002739726
    
    #def 
    
    # ordering_cost 物品成本
    def order_cost():   #物品成本
        pass
        
    def truck():        #運送成本 
        return 6 #1kg
    
    #shortage_cost 短缺商譽損失
    def compensation(): #賠償
        pass
    
    def ctmlose_shortage(n):  #顧客損失
        if n == 1:
            return -0.2
        else:
            return (-0.25)

class Control_: 
    
    def exit_tk():
        '''
        try:
            root.destroy()
        except:
            pass
        '''
        
        global root
        root.quit()
        root.destroy()
        
    def print_one(line_todo):
        for x in line_todo:
             print(x, end='')
             sys.stdout.flush()
             time.sleep(0.15)
             
                 
    def clock():
        global year_c, month_c, day_c, week_c
        print(str(year_c)+'年 \t'+str(month_c)+'月\t'+str(day_c)+'日\t',end='')#+' 星期'+str(week_c)
        if week_c == 1:
            print(' 星期一')
        elif week_c == 2:
            print(' 星期二')
        elif week_c == 3:
            print(' 星期三')
        elif week_c == 4:
            print(' 星期四')
        elif week_c == 5:
            print(' 星期五')
        elif week_c == 6:
            print(' 星期六')
        elif week_c == 7:
            print(' 星期天')
        
        #時間計算
        leap_year = 0
        m31 = ['1', '3', '5', '7', '8', '10', '12']
        m30 = ['4', '6', '9', '11']
        if year_c % 4 == 0 and year_c % 100 != 0:
            leap_year = 1
        elif year_c % 4 == 0 and year_c % 100 == 0 and year_c % 400==0:
            leap_year = 1
        else:
            leap_year = 0
        
        if week_c == 7:
            week_c = 1
        else:
            week_c += 1
        
        day_c += 1
        
        
        if day_c > 28 and  leap_year == 0 and month_c == 2:
            month_c += 1
            day_c = 1
        elif day_c > 29 and  leap_year == 1 and month_c == 2:
            month_c += 1
            day_c = 1
        elif day_c>30 and str(month_c) in m30:
            month_c += 1
            day_c = 1
        elif day_c>31 and str(month_c) in m31:
            if month_c == 12:
                month_c = 1
                day_c = 1
                year_c += 1
            else:
                month_c += 1
                day_c = 1
    
    def tb_add(a, b, c):
        pass 
    
    def tb_(a, b, c):
        pass
    
class game_1():
      
    def drawBoard_():
    
        print("數字鍵對應位置")
        print(" " + "7" + " | " + "8" + " | " + '9')
        print("------------")
        print(" " + '4' + " | " + '5' + " | " + '6')
        print("------------")
        print(" " + '1' + " | " + '2' + " | " + '3')
        print('\n')

    def drawBoard(board):
    
        print(" " + board[7] + " | " + board[8] + " | " + board[9])
        print("------------")
        print(" " + board[4] + " | " + board[5] + " | " + board[6])
        print("------------")
        print(" " + board[1] + " | " + board[2] + " | " + board[3])
    
    # 玩家選擇所想用的棋子種類
    def inputPlayerLetter() :
    
        letter = ''
        while not (letter == 'X' or letter == 'O') :
            print("你要 \'x\' 還是 \'o\' ？",end='\n')
            # 自動將小寫轉化為大寫
            letter = input().upper()
    
        # 如果玩家選擇的X，則自動將O賦給電腦，反之一樣
        if letter == 'x' :
            return ['x','o']
        else :
            return ['o','x']
    
    # 這裡隨機生成0或者1來表示誰先落子
    def whoGoesFirst() :
    
        if random.randint(0,1) == 0 :
            return 'computer'
        else :
            return 'player'
    

    def makeMove(board, letter, move) :
    
        board[move] = letter
    
    #  根據井字棋規則判斷是否獲勝
    def isWinner(bo, le) :
    
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or
                (bo[4] == le and bo[5] == le and bo[6] == le) or
                (bo[1] == le and bo[2] == le and bo[3] == le) or
                (bo[7] == le and bo[4] == le and bo[1] == le) or
                (bo[8] == le and bo[5] == le and bo[2] == le) or
                (bo[9] == le and bo[6] == le and bo[3] == le) or
                (bo[7] == le and bo[5] == le and bo[3] == le) or
                (bo[9] == le and bo[5] == le and bo[1] == le))
    
    # 將已經在棋盤上的棋子備份,隨時更新
    def getBoardCopy(board) :
    
        dupeBoard = []
        for i in board :
            dupeBoard.append(i)
    
        return dupeBoard
    
    # 判斷棋盤是否還有可落子的地方
    def isSpaceFree(board, move) :
    
        return board[move] == ' '
    
    # 獲取玩家落子的位置
    def getPlayerMove(board) :
    
        move = ' '
        # 判斷落子的位置是否正確以及棋盤是否還能落子
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not game_1.isSpaceFree(board, int(move)) :
    
            print("What is your next move?(1-9)")
            move = input()
        return int(move)
    
    # 找到可以落子的地方，主要是計算機使用的
    def chooseRandomMoveFromList(board, moveList) :
    
        possibleMoves = []
        for i in moveList :
            if game_1.isSpaceFree(board, i) :
                possibleMoves.append(i)
    
        if len(possibleMoves) != 0 :
            return random.choice(possibleMoves)
        else :
            return None
        
    def getComputerMove(board, computerLetter) :
    
        # 給出棋盤上電腦和玩家棋子的型別
        if computerLetter == 'X' :
            playerLetter = 'O'
        else :
            playerLetter = 'X'
    
        for i in range(1,10) :
            # 在備份的棋盤中判斷是否有可以落子的地方
            copy = game_1.getBoardCopy(board)
            if game_1.isSpaceFree(copy, i) :
                # 如果有可以落子的地方,則先在備份的棋盤上落子
                game_1.makeMove(copy, computerLetter, i)
                # 落子後判斷電腦是否能贏,並且返回能贏的落子的位置
                if game_1.isWinner(copy, computerLetter) :
                    return i
    
        for i in range(1,10) :
            copy = game_1.getBoardCopy(board)
            if game_1.isSpaceFree(copy, i) :
                # 在備份的棋盤上模擬玩家落子
                game_1.makeMove(copy, playerLetter, i)
                # 如果下一次玩家落子就可以贏,返回玩家落子的位置,用於堵住玩家
                if game_1.isWinner(copy, playerLetter) :
                    return i
    
        # 隨機在四個角處落子
        move = game_1.chooseRandomMoveFromList(board,[1,3,7,9])
        if move != None :
            return move
    
        # 如果角處已被佔滿,則落子在中間位置5處
        if game_1.isSpaceFree(board, 5) :
            return 5
    
        # 如果角和中間都被佔滿,則隨機選擇邊上落子
        return game_1.chooseRandomMoveFromList(board,[2,4,6,8])
    
    # 判斷棋盤是否已滿
    def isBoardFull(board) :
    
        for i in range(1,10) :
            if game_1.isSpaceFree(board, i) :
                return False
        return True
    

class Game_:

    #井字遊戲
    def game_1():
        #print('game_1')
        print("\nWelcome to 井字遊戲 !!!")
        
        game_WWGG = 0 #分數
        
        for i in range(3):
            print("第 "+str(i+1)+' 場遊戲 , 共 3 場')
            # 初始化棋盤為空
            theBoard = [' '] * 10
            # 玩家和電腦棋子型別的選擇
            playerLetter, computerLetter = game_1.inputPlayerLetter()
           
            # 範例 
            game_1.drawBoard_() 
           
            # 先後順序的決定
            turn = game_1.whoGoesFirst()
            print(' \''+ turn + '\'會先執行')
            
            # 遊戲開始的標誌位,當遊戲結束時變成False
            game_1.gameIsPlaying = True
            
            
            
            while game_1.gameIsPlaying :
                # 玩家先行
                if turn == 'player' :
                    game_1.drawBoard(theBoard)
                    # 獲取玩家下棋的位置
                    move = game_1.getPlayerMove(theBoard)
                    # 將玩家的棋子傳入列表相應的位置
                    game_1.makeMove(theBoard, playerLetter, move)
        
                    # 如果玩家獲勝,標誌位變為False
                    if game_1.isWinner(theBoard, playerLetter) :
                        game_1.drawBoard(theBoard)
                        print("You win !")
                        game_WWGG += 1
                        game_1.gameIsPlaying = False
                    # 否則則判斷棋盤是否已滿
                    else :
                        if game_1.isBoardFull(theBoard) :
                            game_1.drawBoard(theBoard)
                            print("Tie !1")
                            game_WWGG += 0.5
                            break
                        # 若棋盤未滿,且玩家已落子,則下一次落到計算機落子
                        else :
                            turn = 'computer'
                # 電腦先行
                else :
                    # 電腦隨機選擇位置落子
                    move = game_1.getComputerMove(theBoard, computerLetter)
                    game_1.makeMove(theBoard, computerLetter, move)
        
                    # 如果電腦落子獲勝,則遊戲結束
                    if game_1.isWinner(theBoard, computerLetter) :
                        game_1.drawBoard(theBoard)
                        print("You lose !")
                        game_1.gameIsPlaying = False
                    else :
                        if game_1.isBoardFull(theBoard) :
                            game_1.drawBoard(theBoard)
                            print("Tie")
                            break
                        else :
                            turn = 'player'
        
            # 玩家沒有再次開始遊戲,則跳出迴圈
            #if not game_1.playAgain():
            #    break
        global power
        if game_WWGG >= 2:
            print('體力增加!!!')
            power += 2
            
        elif game_WWGG == 1.5:
            print('體力增加!!!')
            power += 1
        elif game_WWGG < 1.5:
            print('你也太爛...')
            power -= 1
            
    #幾A幾B
    def game_2():
        os.system("start /wait python app_one.py")
        file = open("project_score.txt", mode="r")
        ti = file.read()
        global power
        if ti == '-1':
            print('你也太爛...')
            power -= 1
        elif ti == '1':
            print('體力增加!!!')
            power += 1
        elif ti == '2':
            print('體力增加!!!')
            power += 2
        else:
            print('error !')
            
        file = open("project_score.txt", mode="w")
        file.write('-1')
        
        del ti
        file.close()
 
    #瑪莉喔
    def game_3():
        print("\n歡迎遊玩馬力歐遊戲！！！")
        time.sleep(2)
        driver_path = 'D:\應用程式\WebDriver\chromedriver.exe'
        driver = webdriver.Chrome(driver_path)
        
        time.sleep(2)
        url = 'https://www.google.com.tw'
        driver.get(url)
        driver.maximize_window()
         
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        time.sleep(0.8)
        search_field.send_keys('supermario-game.com') #傳送值
        time.sleep(0.8)
        search_field.submit()
        
        driver.implicitly_wait(6) #等待網站載入
        driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/h3').click()
        time.sleep(0.8)
        
        url_2 ="https://supermario-game.com/fullscreen"
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(url_2)
        
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(0.2)
        driver.close()
        
       # def selenium_DriverClosed():
       #     #global driver
       #    if driver:
       #         if not driver.window_handles:
       #             return True
       #         else:
       #             return False'''
                
        while True:
            if not driver.window_handles:
                print('(視窗已被使用者關閉關閉)')
                global power
                power += 1
                break
        

    #貪吃蛇
    def game_4(): 
        Game_.game_2()


#button
class button_main():
    def button_work():
        print('<<Work Today>>')
            
        global x #全域變數
        x = 1
      
        Control_.exit_tk()
            
    def button_play():
        print('<<Play Today>>')
        global x #全域變數
        x = 2
      
        Control_.exit_tk()
    
    def button_rest():
        print('<<Rest Today>>')
        global x #全域變數
        x = 3
      
        Control_.exit_tk()
        
    def button_end():
        print('====================================================\n')
        print('<<The End>>')
        global x #全域變數
        x = 4
      
        Control_.exit_tk()

# work button


def button_changeprise():
    pass
            
def work_event():
    country = mycombobox.get()
    global power
    power -= 1
    Control_.exit_tk()      
    
    if country == '查看系統資訊':
        print('查看系統資訊~')
        for i in range(1,5):
            print(good[i].name+"進貨價格:",good[i].in_prise,"元")
        print()
        print("運送價格：",Store.truck(),"元/kg")
        print()
        for i in range(1,5):
            print(good[i].name+"商品重量:",good[i].good_kg,"kg")
        
       
    #elif country == '查看前次資料':
    #    file = open("cos_inf_day.txt", mode="r")
    #    for line in file:
    #        print(line)
    #    file.close()
    
    
      #['文具','便當','安全帽','珠寶']  
    elif country == '進貨':
        global packet
        kg_buy = 0
        print('進貨~  剩餘財產為：'+str(packet)+'元')
        
        for i in ['文具','便當','安全帽','珠寶']:

            if i=='文具':
                aaa = int(input(i + '進貨數量？')) 
                if aaa == '0' or str(aaa) == '' or aaa<0:
                    pass
                else:
                    if (packet-(good[1].in_prise*aaa)) > 0:
                        print("購買",aaa,"個文具")
                        kg_buy += good[1].good_kg*aaa
                        print("扣除",good[1].in_prise*aaa,"元")
                        packet -= good[1].in_prise*aaa
                        good[1].num += aaa
                    else:
                        print('金額不夠')
                        
            elif i=='便當':
                bbb = int(input(i + '進貨數量？'))
                if bbb == '0' or str(bbb) == '' or bbb<0:
                    pass
                else:
                    if (packet-(good[2].in_prise*bbb)) > 0:
                        print("購買",bbb,"個便當")
                        kg_buy += good[2].good_kg*bbb
                        print("扣除",good[2].in_prise*bbb,"元")
                        packet -= good[2].in_prise*bbb
                        good[2].num +=bbb
                    else:
                        print('金額不夠')
                        
            elif i=='安全帽':
                ccc = int(input(i + '進貨數量？')) 
                if ccc == '0' or str(ccc) == '' or ccc<0:
                    pass
                else:
                    if (packet-(good[3].in_prise*ccc)) > 0:
                        print("購買",ccc,"個安全帽")
                        kg_buy += good[3].good_kg*ccc
                        print("扣除",good[3].in_prise*ccc,"元")
                        packet -= good[3].in_prise*ccc
                        good[3].num +=ccc
                    else:
                        print('金額不夠')
                
            elif i=='珠寶':
                ddd = int(input(i + '進貨數量？')) 
                if ddd == '0' or str(ddd) == '' or ddd<0:
                    pass
                else:
                    if (packet-(good[4].in_prise*ddd)) > 0:
                        print("購買",ddd,"個珠寶")
                        kg_buy += good[4].good_kg*ddd
                        print("扣除",good[4].in_prise*ddd,"元")
                        packet -= good[4].in_prise*ddd
                        good[4].num += ddd
                    else:
                        print('金額不夠')
                        
        #運費：
        print()
        print("商品總重：",kg_buy,"kg")
        truck_q = Store.truck()*((kg_buy//1)+1) if kg_buy % 1 != 0 else Store.truck()*((kg_buy//1))
        #Store.truck()*(kg_buy//1)
        print("扣除運費",truck_q,"元")
        packet -= truck_q
        packet = int(packet)
        
        del aaa,bbb,ccc,ddd,kg_buy,truck_q
        
    elif country == '更改價格':
        print('更改價格~')
         
        for i in ['文具','便當','安全帽','珠寶']:
           
           if i=='文具':
               aaa = int(input(i + '價格？'))
               good[1].store_price = aaa
           elif i=='便當':
               bbb = int(input(i + '價格？'))
               good[2].store_price = bbb
           elif i=='安全帽':
               ccc = int(input(i + '價格？'))
               good[3].store_price = ccc
           elif i=='珠寶':
               ddd = int(input(i + '價格？'))
               good[4].store_price = ddd
               
        del aaa,bbb,ccc,ddd
         
    elif country == '開店':
        #open the store
        
        if len(customer) == 0:
            print("你還沒有顧客")
        else:    
            for i in tqdm(range(len(customer))):
                file = open("cos_inf_day.txt", mode="w")
                file.write(str(year_c)+'年 \t'+str(month_c)+'月\t'+str(day_c)+'日') #今天日期
                file.write('\n')
                file.close()
                z = 0 #是否會進店
                if bool(customer[i].is_come) == True:
                    #customer[i].freq -= 1
                    if  customer[i].a_buy == 1:           #good[j].num
                        # 是否會進店-> 商品價格 -> 商品數量 ->  寫入統資資料 "a" cos_inf_day.txt
                        #是否會進店
                        if bool(random.randint(0,(7-customer[i].freq+1))) or not(random.randint(0,good[1].frequency)):
                            
                            #商品價格 依照pq曲線
                            z =1 #是否會進店
                            if good[1].store_price >50 : 
                                Q=False #太貴
                            elif good[1].store_price>30:
                                Q = not(bool(random.randint(0,((good[1].store_price // 5)-1))))
                            elif good[1].store_price>10:
                                Q = not(bool(random.randint(0,((good[1].store_price // 4)-1))))
                            else:
                                Q = True
                            #購買
                            if Q:
                                #商品是否足夠
                                if good[1].num>0:
                                    #global packet
                                    q_num = random.randint(1,7) #購買幾件商品
                                    if good[1].num > q_num: #量足夠
                                        good[1].num -= q_num
                                        packet += good[1].store_price*q_num
                                        file = open("cos_inf_day.txt", mode='a')
                                        file.write("編號"+str(i)+"購買"+str(q_num)+"個文具")
                                        file.write('\n')
                                        file.close()
                                    else:
                                        q_num = good[1].num #量不夠
                                        good[1].num -= q_num
                                        packet += good[1].store_price*q_num
                                        customer[i].is_come -= Store.ctmlose_shortage(1) #商譽損失
                                        file = open("cos_inf_day.txt", mode='a')
                                        file.write("編號"+str(i)+"購買"+str(q_num)+"個文具")
                                        file.write('\n')
                                        file.close()
                                        
                                elif good[1].num<0: #沒東西
                                    customer[i].is_come -= Store.ctmlose_shortage(2)
                                    file = open("cos_inf_day.txt", mode='a')
                                    file.write("編號"+str(i)+"沒買到商品")
                                    file.write('\n')
                                    file.close()

                                
                    if customer[i].b_buy == 1:
                        
                        if z==1:
                            if good[2].store_price >350 : 
                                Q=False #太貴
                            elif good[2].store_price>125:
                                Q = not(bool(random.randint(0,(good[2].store_price // 5))))
                            elif good[2].store_price>90:
                                Q = not(bool(random.randint(0,((good[2].store_price // 10)-1))))
                            elif good[2].store_price>60:
                                Q = not(bool(random.randint(0,((good[2].store_price // 10)-2))))
                            elif good[2].store_price>50:
                                Q = not(bool(random.randint(0,((good[2].store_price // 10)-1))))
                            else:
                                Q = True
                            #購買
                            if Q:
                                #商品是否足夠
                                if good[2].num>0:
                                    if good[2].frequency:
                                        #global packet
                                        q_num = random.randint(1,5) #購買幾件商品
                                        if good[2].num > q_num: #量足夠
                                            good[2].num -= q_num
                                            packet += good[2].store_price*q_num
                                            file = open("cos_inf_day.txt", mode='a')
                                            file.write("編號"+str(i)+"購買"+str(q_num)+"個便當")
                                            file.write('\n')
                                            file.close()
                                        else:
                                            q_num = good[2].num #量不夠
                                            good[2].num -= q_num
                                            packet += good[2].store_price*q_num
                                            customer[i].is_come -= Store.ctmlose_shortage(1) #商譽損失
                                            file = open("cos_inf_day.txt", mode='a')
                                            file.write("編號"+str(i)+"購買"+str(q_num)+"個便當")
                                            file.write('\n')
                                            file.close()
                                            
                                    elif good[2].num<0: #沒東西
                                        customer[i].is_come -= Store.ctmlose_shortage(2)
                                        file = open("cos_inf_day.txt", mode='a')
                                        file.write("編號"+str(i)+"沒買到商品")
                                        file.write('\n')
                                        file.close()
                            
                    
                    if customer[i].c_buy == 1:
                        if z==1:
                            if not(random.randint(0,good[3].frequency)):
                                if good[3].store_price >3000: 
                                    Q=False #太貴
                                elif good[3].store_price>2000:
                                    Q = not(bool(random.randint(0,(good[3].store_price // 50))))
                                elif good[3].store_price>1500:
                                    Q = not(bool(random.randint(0,((good[3].store_price // 100)-1))))
                                elif good[3].store_price>1000:
                                    Q = not(bool(random.randint(0,((good[3].store_price // 100)-2))))
                                elif good[3].store_price>500:
                                    Q = not(bool(random.randint(0,((good[3].store_price // 100)-1))))
                                elif good[3].store_price>300:
                                    Q = not(bool(random.randint(0,((good[3].store_price // 100)))))
                                else:
                                    Q = True
                                #購買
                                if Q:
                                    #商品是否足夠
                                    if good[3].num>0:
                                        #global packet
                                        q_num = random.randint(1,5) #購買幾件商品
                                        if good[3].num > q_num: #量足夠
                                            good[3].num -= q_num
                                            packet += good[3].store_price*q_num
                                            file = open("cos_inf_day.txt", mode='a')
                                            file.write("編號"+str(i)+"購買"+str(q_num)+"個便當")
                                            file.write('\n')
                                            file.close()
                                        else:
                                            q_num = good[3].num #量不夠
                                            good[3].num -= q_num
                                            packet += good[3].store_price*q_num
                                            customer[i].is_come -= Store.ctmlose_shortage(1) #商譽損失
                                            file = open("cos_inf_day.txt", mode='a')
                                            file.write("編號"+str(i)+"購買"+str(q_num)+"個便當")
                                            file.write('\n')
                                            file.close()
                                            
                                    elif good[3].num<0: #沒東西
                                        customer[i].is_come -= Store.ctmlose_shortage(2)
                                        file = open("cos_inf_day.txt", mode='a')
                                        file.write("編號"+str(i)+"沒買到商品")
                                        file.write('\n')
                                        file.close()
                            
                    
                    if customer[i].d_buy == 1:
                        if z==1:
                            if not(random.randint(0,good[4].frequency)):
                                if good[4].store_price >300000: 
                                    Q = not(bool(random.randint(0,3)))
                                elif good[4].store_price>20000:
                                    Q = not(bool(random.randint(0,(good[4].store_price // 10))))
                                elif good[4].store_price>15000:
                                    Q = not(bool(random.randint(0,((good[4].store_price // 10)-1))))
                                elif good[4].store_price>10000:
                                    Q = not(bool(random.randint(0,((good[4].store_price // 10)-2))))
      
                                else:
                                    Q = True
                                #購買
                                if Q:
                                    #商品是否足夠
                                    if good[4].num>0:
                                        #global packet
                                        q_num = random.randint(1,5) #購買幾件商品
                                        if good[4].num > q_num: #量足夠
                                            good[4].num -= q_num
                                            packet += good[4].store_price*q_num
                                            file = open("cos_inf_day.txt", mode='a')
                                            file.write("編號"+str(i)+"購買"+str(q_num)+"個便當")
                                            file.write('\n')
                                            file.close()
                                        else:
                                            q_num = good[4].num #量不夠
                                            good[4].num -= q_num
                                            packet += good[4].store_price*q_num
                                            customer[i].is_come -= Store.ctmlose_shortage(1) #商譽損失
                                            file = open("cos_inf_day.txt", mode='a')
                                            file.write("編號"+str(i)+"購買"+str(q_num)+"個便當")
                                            file.write('\n')
                                            file.close()
                                            
                                    elif good[4].num<0: #沒東西
                                        customer[i].is_come -= Store.ctmlose_shortage(2)
                                        file = open("cos_inf_day.txt", mode='a')
                                        file.write("編號"+str(i)+"沒買到商品")
                                        file.write('\n')
                                        file.close()
                    
                time.sleep(0.05)  
                del z
                    
        
        
        
        global y
        y = 1
    
    print()   
    print("------------------------------------------")
    print() 
     
# play button
def play_event():
    
    #print(mycombobox.current(), mycombobox.get()) #mycombobox.get()
    #buttonText.set('idx:' + str(mycombobox.current()) + ', ' + mycombobox.get())
    country = mycombobox.get()
    Control_.exit_tk()
    
    print("開始"+country+"遊戲", end="")

    Control_.print_one("......\n")

    #print('\n')
    
     
    #global y #全域變數
    if country == 'Game_1':
         #y = 1
         Game_.game_1()
    elif country == 'Game_2':
         #y = 2
         Game_.game_2()
    elif country == 'Game_3':
         #y = 3
         Game_.game_3()
    elif country == 'Game_4':
         #y = 4
         Game_.game_4()

def rest_event():
    
    #print(mycombobox.current(), mycombobox.get()) #mycombobox.get()
    #buttonText.set('idx:' + str(mycombobox.current()) + ', ' + mycombobox.get())
    country = mycombobox.get()
    Control_.exit_tk()

    if country == '畫圖':
        Control_.print_one('又是耍廢的一天呢~~~\n')
        #print('又是耍廢的一天呢~~~')
        #print('\n')
        Draw_.draw_random()
        
    elif country == '機會命運':
         pass
    elif country == '看股票':
         pass
    elif country == '去旅遊':
         pass
    elif country == '自動馬力歐':
         pass

class Draw_:
    
    def draw_random():
     
        # 1.创建白色背景图片
        d = 200
        img = np.ones((d, d, 3), np.uint8) * 255
     
        # 2.循环随机绘制实心圆
        for i in range(0, 100):
            # 随机中心点
            center_x = np.random.randint(0, high=d)
            center_y = np.random.randint(0, high=d)
     
            # 随机半径与颜色
            radius = np.random.randint(5, high=d/5)
            color = np.random.randint(0, high=256, size=(3, )).tolist()
     
            cv2.circle(img, (center_x, center_y), radius, color, -1)
     
        # 3.显示结果
        cv2.imshow("img", img)
        cv2.waitKey()
        cv2.destroyAllWindows()    
     
# main 
if __name__ == "__main__":
    #第一個視窗
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost',1) #至頂
    messagebox.showinfo('Introduce', '這是一個有關創業的模擬器')
    
    #商品性質 首次設定
    #name, num, store_price, in_prise, good_kg, willbuy, frequency, alternatives
    #名稱, 數量, 販售價格,    進貨價格,  商品重量, 進店後購買率,購買平率(幾天買一次), 替代商品造成影響
    
    good[1] = Goods_("文具", 0, 0, 3, 0.01, 1, 20, 1)
    good[2] = Goods_("便當", 0, 0, 40, 0.5, 1, 1, 1)
    good[3] = Goods_("安全帽", 0, 0, 600, 1, 1, 365, 1)
    good[4] = Goods_("珠寶", 0, 0, 5600, 0.05, 1, 180, 1)
    
    while True:
        
        '''遊戲狀況判斷'''        
        if power <= 0: # or 
            print("你累死了")    
            break
        elif packet <= 0:
            print("請去借錢後再繼續遊戲")
            #銀行系統
            break
        
        
        #來客數
        tmp = cus
        cus = Store.customer_n(cus, day)
        #print(cus)
        
        #顧客性質
        for i in range(tmp,cus):
            data1 = [0,0,0,0,1]
            data2 = [0,0,0,0,0,0,0,0,0,1]
            
            customer[i] = Customers_(i, 
                                   #True if random.uniform(0,5) != 0 else False
                                   random.choice([0,1,1]),
                                   random.choice([2, 3, 4, 5]),
                                   random.choice(data1),
                                   random.choice(data2))
            del data1, data2
        del tmp  
        '''for i in range(cus):
            print(customer[i].name)
            print(customer[i].is_come)
            print(customer[i].c_buy)
            print(customer[i].d_buy)'''
        
        
        
        #ewwer
        
        #日期
        Control_.clock()
        
        #表格
        day += 1
        print("Day: ",day, '\t', "財產: ", packet , '\t', "體力： ", power)
        
        p_tb[1:5] = [good[1].store_price,good[2].store_price,good[3].store_price,good[4].store_price]
        c_tb[1:5] = [good[1].num,good[2].num,good[3].num,good[4].num]  
        
        tb1 = pt.PrettyTable()
        tb1.field_names = ['Goods','Pen','Food','Hat','Jewelry']
        tb1.add_row(p_tb)
        tb1.add_row(c_tb)
        tb1.set_style(pt.DEFAULT)
        print(tb1)
        
        print('')
      
        #等待
        time.sleep(0.5)
        
        #選擇事件視窗
        root = tk.Tk()
        root.title('Mini創業')
        root.geometry('540x540+350+180')
        root.wm_attributes('-topmost',1)
        
        mylabel = tk.Label(root, text='第'+str(day)+'天, 要做什麼?',font=('Arial', 30))
        #mylabel = tk.Label(root, text='今天要做什麼?',font=('Arial', 25))
        mylabel.pack()
    
        '''   
        x = str(input("你今天要做什麼?  "))
        #print(type(x))
        
        '''    
    
        mybutton = tk.Button(root, text='Work', height=4 , width=30, command=button_main.button_work , font=('Arial', 15))
        mybutton.pack()
        
        mybutton = tk.Button(root, text='Play', height=4 , width=30, command=button_main.button_play, font=('Arial', 15))
        mybutton.pack()
        
        mybutton = tk.Button(root, text='Rest', height=4 , width=30, command=button_main.button_rest, font=('Arial', 15))
        mybutton.pack()
        
        mybutton = tk.Button(root, text='End Game', height=4 , width=30, command=button_main.button_end, font=('Arial', 15))
        mybutton.pack()
    
        root.mainloop()
        
        #回來了
        #print(x)
        while True:    
            if x == 1: #開工
                root = tk.Tk()
                root.title('work')
                root.geometry('300x100+650+350')
                root.wm_attributes('-topmost',1)
                
                comboboxList = ['查看系統資訊','進貨','更改價格','開店'] #結束一天 ,'查看前次資料'
                mycombobox = ttk.Combobox(root, state='readonly')
                mycombobox['values'] = comboboxList
                
                mycombobox.pack(pady=10)
                mycombobox.current(0)
                
                buttonText =  tk.StringVar()
                buttonText.set('確認')
                tk.Button(root, text='確認',textvariable=buttonText, command=work_event).pack()
                
                root.mainloop()
                
                if y == 0:
                    time.sleep(0.5)
                    continue
                elif y == 1:
                    break
                
            elif x == 2:  #玩遊戲
                root = tk.Tk()
                root.title('play')
                root.geometry('300x100+650+350')
                root.wm_attributes('-topmost',1)
                
                comboboxList = ['Game_1','Game_2','Game_3','Game_4']
                mycombobox = ttk.Combobox(root, state='readonly')
                mycombobox['values'] = comboboxList
                
                mycombobox.pack(pady=10)
                mycombobox.current(0)
                
                buttonText =  tk.StringVar()
                buttonText.set('確認')
                tk.Button(root, text='確認',textvariable=buttonText, command=play_event).pack()
                
                root.mainloop()
                
                break
            elif x == 3: #休息
                root = tk.Tk()
                root.title('play')
                root.geometry('300x100+650+350')
                root.wm_attributes('-topmost',1)
                
                comboboxList = ['畫圖','機會命運','看股票','去旅遊','自動馬力歐']
                mycombobox = ttk.Combobox(root, state='readonly')
                mycombobox['values'] = comboboxList
                
                mycombobox.pack(pady=10)
                mycombobox.current(0)
                
                buttonText =  tk.StringVar()
                buttonText.set('確認')
                tk.Button(root, text='確認',textvariable=buttonText, command=rest_event).pack()
                
                root.mainloop()
                break
                
            elif x == 4: 
                break
        
        if x == 4: #結束遊戲
                break
        x = 0
        y = 0 
        
        #clipVideo = VideoFileClip("car.gif")
        #clipVideo.write_gif("car.gif")
        
        '''
        
        結束天數判斷
        
        '''
        
        #time+sys 輸出文字
        time.sleep(0.5)
        Control_.print_one("***恭喜妳過了第"+str(day)+"天***")
        
        print()
        print('\n====================================================\n')
        
        #break #for test
    
#結算程式   
print("遊戲結算",end='')
Control_.print_one("......")

print('\n')
if power <= 0 or packet <= 0:
    print(
    '''
    \ \   / /          | |
     \ \_/ /__  _   _  | | ___   _____ ___
      \   / _ \| | | | | |/ _ \ / ___// _ \ 
       | | (_) | |_| | | | (_) (__  )/  __/
       |_|\___/ \__,_| |_|\___/____/ \___/ you lose...
    '''
    )

    #os._exit()
else:
    print(
    '''
                      ,  ,
                       \\ \\
                       ) \\ \\    _p_
                       )^\))\))  /  ^\  
                        \_|| || / /^`-' 讚喔~
               __       -\ \\--/ /      感謝遊玩~
             <'  \\___/   ___. )'
                  `====\ )___/\\
                       //     `"
                       \\    /  \  
    '''
    )
    
print('''
  _____ __                __
 /_  __/ /_  ____  ____  / /__  ____
  / / / __ \/ __ \/ __ \/ // // ___/
 / / / / / / /_/ / / / / , < (__  )
/_/ /_/ /_/\__,_/_/ /_/_/|_|/____/ 
'''
)

sys.exit(0)