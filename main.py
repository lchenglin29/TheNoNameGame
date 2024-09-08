import random
import time
import requests
import sys
import mydef

from mydef import load_json, write_js
run = True
start = True
letter_noti = True
name = ""
inp = ""

item_all_list = ["治療藥水","肉燥飯","尤加利葉","攻擊增強藥水","黃金","鐵礦","鮮魚","串燒豬肉","鮭魚","鰹魚","鯖魚","鐵桶","種子"]
fish_list = ["鮭魚","鯖魚","鰹魚"]
item_list = {
  "治療藥水":{"h":150,"a":0},
  "肉燥飯":{"h":15,"a":0},
  "鮮魚":{"h":5,"a":5},
  "尤加利葉":{"h":10,"a":5},
  "串燒豬肉":{"h":50,"a":50},
  "攻擊增強藥水":{"h":0,"a":150},
  "尖叫雞":{"h":5,"a":5}
}

shop_list = {
  "治療藥水":{"des":"葉政洧說喝了這個就會增加150滴血！","price":60},
  "攻擊增強藥水":{"des":"哥布林那邊幹來的東西，會增加150攻擊力...他們要這個幹嘛？","price":60},
  "串燒豬肉":{"des":"聽說吃了可以攻擊血量各回50！","price":40},
  "黃金":{"des":"雖然不能拿來補血或之類的，但是拿來買買東西還不錯啦！","price":20},
  "鐵桶":{"des":"可以拿來裝水，不然你想要幹嘛？","price":20},
  "尖叫雞" : {"des":"會尖叫，但也會幫你攻擊血量各加5","price":5},
  "政侑葉":{"des":"一種葉子，但不是尤加利葉！","price":20}
}

role_list = ["詹朝翔","葉政洧","無尾熊","蔡鎮澤","張閎翔","楊子毅"]
boss_list = ["葉•鎮鮪•政侑","戰潮詳","ㄘㄨㄚˋ政擇","章紅詳 家裡有礦","羊仔義"]
move_list = ["尋找人生意義","尖叫","被踢出宿舍","洗澡","拉屎","和女友接吻","目擊別人外遇","求偶","跳霹靂舞","大聲唱歌","吃飯","送別人尖叫雞"]
scn_list = ["廁所裡","百貨公司裡","別人的外遇現場","看流星雨的地方","宿舍裡","路邊"]
atk_list = ["幫你抓癢","呵呵笑","前滾翻","踢別人出宿舍","超派","拉屎","炸彈","攻擊藥水","變形","尖叫雞"]

ntips = '''\033[33m提示：
輸入「挖礦」來挖礦
輸入「冒險」來試著打怪升級
輸入「地牢」來挑戰地牢
輸入「使用」來使用物品
輸入「商店」來開啟商店選單與商品列表
\033[46m輸入「釣魚」來釣魚\033[0m
\033[46m輸入「處理生魚」來處理釣到的魚\033[0m
\033[33m輸入「寄信」來寄信
輸入「信箱」來開啟信箱
輸入「讀取」來讀取信件
輸入「關閉通知」來關閉每輪信件未讀通知
輸入「選單」來開啟選單
輸入「提示」來獲取提示
輸入「退出」來關閉遊戲\033[0m
'''
tips = ntips
print("\033[1m還沒想到名稱的遊戲！\033[0m")
print("載入中",end = '')
for i in range(3):
  time.sleep(0.5)
  print('.',end = '')
print(
  '''載入完成！
版本 beta1.0.7
\033[46m更新內容：「釣魚系統」！\033[0m
\n🐖•在商店購買新的串燒豬肉！
\n🎣•釣魚來獲得新鮮魚肉！
\n📨•和朋友寄信來聯絡感情吧！
\n👾•體驗新的地牢劇情！
'''
)

data_md = {"name":"", "hp":100, "atk":20, "lv":1, "exp":0,"back":{}}

def load_web(name):
  try:
    data = requests.get(f"https://4bf6858d-3eb9-4003-8651-fbb070c7b5fc-00-32cyicqpj0myc.janeway.replit.dev/load_json/{name}").json()
#    print(data)
    return data
  except Exception as e:
    print(e)
    return False
def write_wb(name,data):
  requests.post(f"https://4bf6858d-3eb9-4003-8651-fbb070c7b5fc-00-32cyicqpj0myc.janeway.replit.dev/write_js/{name}",json = data)
def online_req(name):
  requests.post(f"https://4bf6858d-3eb9-4003-8651-fbb070c7b5fc-00-32cyicqpj0myc.janeway.replit.dev/online",json = {"user":name})
  return "online"
def offline_req(name):
  requests.post(f"https://4bf6858d-3eb9-4003-8651-fbb070c7b5fc-00-32cyicqpj0myc.janeway.replit.dev/offline",json={"user":name})
  return "offline"

if not load_web("測試"):
  print("警告！伺服器不在線或網路異常！")
  sys.exit()


while run:
  while start == True:
    '''print("嗨嗨，跟我說說你叫什麼名字好嗎？")
    player_data["name"] = input()
    print(f"你好，{player_data['name']}！\n讓我們來進行新手教學吧！")
    start = False
    '''
    s = input("歡迎！你要登入還是要註冊呢？\n輸入「1」 登入\n輸入「2」 註冊")
    if s == "1":
      menu_data = load_web("menu")
      ac = input("請輸入帳號：")
      pw = input("請輸入密碼：")
      if ac in menu_data:
#        print("正常1")
        p_data = load_web(ac)
#        print("正常")
#        print(p_data[f"{ac}"]["password"])
        if str(pw) == p_data[f"{ac}"]["password"]:
          name = ac
          online_req(name)
          print("\033[32m登入成功！\033[0m")
#          print(f"{name}，你好！\033[46m你有{len(p_data[f'{name}']['mail_box'])}封郵件未讀！\033[0m")
          start = False
        else:
          print("\033[91m帳號或密碼錯誤！\033[0m")
      else:
        print("\033[91m帳號或密碼錯誤！\033[0m")
    elif s == "2":
      menu_data = load_web("menu")
      print("\033[41m請不要輸入真實的帳號密碼因為我會看到\033[0m")
      ac = input("請輸入帳號：")
      if ac in menu_data:
        print("\033[91m帳號已存在！\033[0m")
      else:
        menu_data.setdefault(f"{ac}",0)
        write_wb("menu",menu_data)
        pw = input("請輸入密碼：")
#        player_data = load_json(ac)
#        write_js("menu",menu_data)
        sdata = {}
        write_wb(ac,sdata)
        player_data = load_web(ac)
        player_data.setdefault(f"{ac}", {"password":str(pw), "player_data": {"name":f"{ac}", "hp":100, "atk":20, "lv":1, "exp":0,"back":{}},"mail_box":{}})
        write_wb(ac,player_data)
        name = ac
        start = False

  data = load_web(name)
#  print(data)
  player_data = data[f"{name}"]["player_data"]

  def use_item(item, amount):
    if item in item_list:
      if item in player_data["back"]:
        if player_data["back"][item] >= amount:
          player_data["hp"] += (item_list[item]["h"] * amount)
          player_data["atk"] += (item_list[item]["a"] * amount)
          player_data["back"][item] -= amount
          return f"你使用了\033[42m{item}\033[0m{amount}個，增加了\033[92m{item_list[item]['h'] * amount}\033[0m滴血及\033[91m{item_list[item]['a'] * amount}\033[0m攻擊力"
        else:
          return f"\033[31m你的{item}不夠！\033[0m"
      else:
        return f"\033[31m你的{item}不夠！\033[0m"
    else:
      return f"\033[31m{item}不存在，或者不是這樣用的！\033[0m"
    
  def drop_item(lev):
    random.randint(1,100)
    if lev == 1:
      drop_list = ["肉燥飯","尤加利葉"]
      if random.randint(1,10) >= 5:
        item = random.choice(drop_list)  
        amount = random.randint(1,2)
        player_data["back"].setdefault(f"{item}",0)
        player_data["back"][f"{item}"] += amount
        return f"意外收穫了{amount}個{item}！"
      else:
        return 0
    elif lev == 2:
      drop_list = ["串燒豬肉","攻擊增強藥水","治療藥水"]
      if random.randint(1,10) >= 0:
        for i in range(1,4):
          item = random.choice(drop_list)  
          amount = random.randint(3,5)
          player_data["back"].setdefault(f"{item}",0)
          player_data["back"][f"{item}"] += amount
          print(f"意外收穫了{amount}個{item}！")
      else:
        return 0

  def show_back():
    if len(player_data["back"])==0:
      print("你什麼都沒有，笑死")
    else:
      for key,value in player_data["back"].items():
        print(f"{key}：{value}個")

  def send_mail(to,title,text,object,amount):
    menu_data = load_web("menu")
    if to in menu_data:
      if object == None:
        id = requests.get(f"https://4bf6858d-3eb9-4003-8651-fbb070c7b5fc-00-32cyicqpj0myc.janeway.replit.dev/getid").text
        to_data = load_web(str(to))
        to_data[str(to)]["mail_box"].setdefault(f"{id}",{"author":f"{name}","title":str(title),"text" : str(text)})
        write_wb(str(to),to_data)
        print("信件已寄出！")
      else:
        if object in item_all_list:
          if amount <= player_data["back"][object]:
            id = requests.get(f"https://4bf6858d-3eb9-4003-8651-fbb070c7b5fc-00-32cyicqpj0myc.janeway.replit.dev/getid").text
            to_data = load_web(str(to))
            to_data[str(to)]["mail_box"].setdefault(f"{id}",{"author":f"{name}","title":str(title),"text" : str(text),"item":str(object),"amount":int(amount)})
            write_wb(str(to),to_data)
            player_data["back"][str(object)] -= int(amount)
            print("信件已寄出！")
          else:
            print(f"\033[91m你的背包沒有這麼多「{item}」！\033[0m")
        else:
          print(f"\033[91m{item}不存在\033[0m")
    else:
      print(f"\033[91m{to}不存在！\033[0m")

  def battle(mon,mh,ma):
    print(f"第 {player_data['un']['floor']} 層")
    ba = True
    while ba==True:
      defn = False
      if mh <= 0:
        print(f"{mon}：看來，你打贏了我")
        time.sleep(1)
        print(f"{mon}：但是地牢從來沒有盡頭...只要你還在，只要你還能輸入，後面就還有東西等著你...")
        lu = random.randint(10,40)
        
        print(f"\033[33m你戰勝了{mon}，升了{lu}等！\033[0m")
        player_data["lv"] += lu
        player_data["un"]["floor"]+=1
        player_data["un"]["mh"] = 500 + 500*player_data["un"]["floor"]
        player_data["un"]["ma"] = 300 + 200*player_data["un"]["floor"]
        drop_item(2)
        ba = False
        break
      if player_data["hp"] <= 0:
        print(f"{mon}：如你所知，你即將死亡，作何感想？哼。")
        time.sleep(2)
        ba = False
        break
      print(f'''
怪獸資訊
怪獸名稱：{mon}
怪獸血量：{mh}
最大攻擊：{ma}

你的資訊
你的血量：{player_data["hp"]}
最大攻擊：{player_data["atk"]}
      ''')
      ac = input("1 攻擊\n2 防禦\n3 使用道具\n4 離開地牢")
      if ac == "1":
        at = random.randint(1,player_data["atk"])
        mh -= at
        print(f"\033[33m你對{mon}造成了{at}點傷害！\033[0m")
      elif ac == "2":
        if random.randint(1,10)>=9:
          print("\033[36m防禦成功，該回合免傷！\033[0m")
          defn = True
        else:
          print("\033[91m防禦失敗\033[0m")
      elif ac == "3":
        if input("你需要先看一下背包嗎？(y/n)") == "y":
          show_back()
        item = input("輸入道具名稱：")
        amount = input("輸入使用數量：")
        use_item(item,int(amount))
      elif ac == "4":
        print("\033[91m你逃跑了！\033[0m")
        player_data["un"]["mh"] = mh
        player_data["un"]["ma"] = ma
        ba = False
        break      
      if random.randint(1,10)>=1:
        if defn == False:
          tma = random.randint(ma-20,ma)
          player_data["hp"] -= tma
          print(f"{mon}使出了\033[43m{random.choice(atk_list)}\033[0m，你的生命值-{tma}")
        else:
          print(f"\03346[m你擋下了{mon}的{random.choice(atk_list)}！\033[0m")
      else:
        print(f"{mon}：哼，像你這樣的東西，我也不屑動手打你！")
      player_data["un"]["mh"] = mh
      player_data["un"]["ma"] = ma


  def buy(item,amount):
    if item in shop_list:
      if item != "黃金":
        price = shop_list[item]["price"]
        if "黃金"  in player_data["back"]:
          if player_data["back"]["黃金"] >= price * amount:
            player_data["back"]["黃金"] -= price * amount
            player_data["back"].setdefault(f"{item}",0)
            player_data["back"][f"{item}"] += amount
            print(f"\033[43m你購買了{amount}個{item}\033[0m\n總價：{price * amount}個黃金")
          else:
            print("\033[91m黃金不夠啦！\033[0m")
        else:
          print("\033[91m沒有黃金還敢來亂喔？\033[0m")
      elif item == "黃金":
        price = shop_list[item]["price"]
        if "鐵礦" in player_data["back"]:
          if player_data["back"]["鐵礦"] >= price * amount:
            player_data["back"]["鐵礦"] -= price * amount
            player_data["back"].setdefault(f"{item}",0)
            player_data["back"][f"{item}"] += amount
            print(f"\033[43m你買了{amount}個{item}！\033[0m\n總價：{price * amount}個鐵礦")
          else:
            print("\033[91m鐵礦不夠啦！\033[0m")
        else:
          print("\033[91m沒有鐵礦還敢來亂喔？\033[0m")
    else:
      print(f"\033[91m我們沒賣{item}\033[0m")

  if player_data["hp"] <= 0:
#    run = False
    player_data = data_md
    data[f"{name}"]["player_data"] = player_data
    write_wb(name,data)
    print("\033[91m死亡，全部重來！\033[0m")
#    break

  if len(data[name]["mail_box"]) != 0:
    if letter_noti == True:
      print(f"\033[46m你有{len(data[name]['mail_box'])}封信未讀！\033[0m")
  
  inp = input(tips).encode("utf-8").decode("utf-8")

  if inp == "選單":
    ans = input("輸入「1」 開啟背包\n輸入「2」 開啟個人檔案")
    if ans == "1":
      print(f"你的背包：")
      if len(player_data["back"]) == 0:
        print("你什麼都沒有，笑死")
      else:
        for key,value in player_data["back"].items():
#          if value == 0:
#            player_data["back"].pop(key)
          print(f"{key}：{value}個")
    elif ans == "2":
      print(f'''你的個人檔案：
  名字：{name}
  等級：{player_data['lv']}
  血量：{player_data['hp']}
  攻擊力：{player_data['atk']}
    ''')
    else:
      print(f"沒有{ans}這個選項")

  elif inp == "挖礦":
    if random.randint(1,100) <= 30:
      player_data["back"].setdefault("黃金",0)
      gold = random.randint(1,10)
      player_data["back"]["黃金"] += gold
      print(f"\033[43m挖到了{gold}個黃金！\033[0m")
    else:
      player_data["back"].setdefault("鐵礦",0)
      fe = random.randint(10,30)
      player_data["back"]["鐵礦"] += fe
      print(f"\033[100m挖到了{fe}個鐵礦！\033[0m")
    di = drop_item(1)
    if di != 0:
      print(di)

  elif inp == "釣魚":
    if random.randint(1,10) >= 6:
      amount = random.randint(3,5)
      fish = random.choice(fish_list)
      player_data["back"].setdefault(fish, 0)
      player_data["back"][fish] += amount
      print(f"\033[44m你釣到了{amount}個{fish}！\033[0m")
    else:
      print("你沒釣到任何東西")

  elif inp == "處理生魚":
    handle = True
    while handle == True:
      fish = input("輸入魚種：（輸入1退出介面）")
      if fish == "1":
        print("\033[91m離開介面！\033[0m")
        handle = False
        break
      amount = int(input("輸入數量："))
      if fish in player_data["back"]:
        if player_data["back"][fish] >= amount:
          player_data["back"][fish] -= amount
          player_data["back"].setdefault("鮮魚", 0)
          player_data["back"]["鮮魚"] += amount*2
          print(f"\033[44m你處理了{amount}個{fish}，獲得了{amount*2}個鮮魚！\033[0m")
        else:
          print(f"\033[91m你沒有這麼多{fish}\033[0m")
      else:
        print(f"\033[91m你沒有{fish}！\033[0m")

  elif inp == "冒險":
    role = random.choice(role_list)
    move = random.choice(move_list)
    scn = random.choice(scn_list)
    print(f"你遇到了正在{scn}{move}的{role}！跟他戰鬥？(y/n)")
    ans = input()
    if ans == "y":
      ma = random.randint(10,40) + int((player_data["atk"])*0.6)
      mh = random.randint(20,60) + int((player_data["hp"])*0.5)
      lmh = mh
      battle = True
      while battle:
        defn = False
        
        if mh <= 0:
          lu = random.randint(1,int(lmh/10))
          player_data["lv"]+=lu
          print(f"\033[33m你戰勝了{role}並升了{lu}級！\033[0m")
          battle = False
          break
        if player_data["hp"] <= 0:
          print("\033[91m你死了，全部重來！\033[0m")
          battle = False
          break
        print(f"怪獸資訊：\n怪獸名稱：{role}\n怪獸血量：{mh}\n最大攻擊：{ma}\n")
        print(f"你的資訊：\n你的血量：{player_data['hp']}\n最大攻擊：{player_data['atk']}\n")
        act = input("1 攻擊\n2 防禦\n3 道具")
        
        if act == "1":
          hurt = random.randint(1,player_data["atk"])
          mh-=hurt
          print(f"\033[33m你對{role}造成了{hurt}點傷害!\033[0m")

        if act == "2":
          if random.randint(1,10) > 2:
            defn = True
            print("\033[32m防禦成功，該回合免傷！\033[0m")
          else:
            print("\033[91m防禦失敗！\033[0m")
          
        if act == "3":
          print("\033[41m警告！若沒有使用成功會被跳過一回合！\033[0m")
          if input("你需要看一下背包嗎？(y/n)") == "y":
            show_back()
          item = input("請輸入物品名稱：")
          amount = input("請輸入數量：")
          msg = use_item(item,int(amount))
          print(msg)

        if random.randint(1,100) <= 60:
          if defn:
            print(f"{role}的攻擊被你\033[32m防禦\033[0m掉了！")
          else:
            a = random.randint(1,ma)
            player_data["hp"]-=a
            print(f"{role}使出了\033[43m「{random.choice(atk_list)}」\033[0m！你的生命值-{a}")
          
        else:
            print(f"{role}選擇了微笑逃避！")

    else:
      print("\033[91m怪物離開了ùwú\033[0m")


#  elif inp == "關閉提示":
#    print("\033[91m提示關閉！\033[0m")
#    tips = ""

  elif inp == "提示":
    print(ntips)
    tips = ntips

  elif inp == "地牢":
    if input("你確定你要進入地牢？(y/n)") == "y":
      if "un" in player_data:
        print("你又回來了啊...")
        time.sleep(1)
        battle(boss_list[player_data["un"]["floor"]%5],player_data["un"]["mh"],player_data["un"]["ma"])
      else:
        print("有個聲音從你背後傳來了！")
        if player_data["lv"] >= 15:
          print("？？？：所以，你殺了很多所謂的「怪物」是嗎？")
          ans = input("1 沒有，你根本毫無證據！\n2 是，那又怎樣？那些都是怪物啊！")
          if ans == "1":
            print("你：沒有，你根本毫無證據！")
            time.sleep(1)
            print(f"？？？：毫無證據？哼，你看看你的等級吧！{player_data['lv']}等，每一等都是踩著你所謂怪物的鮮血加上去的！")
            time.sleep(1)
            print("你：你到底是誰？")
            time.sleep(1)
            print("？？？：那重要嗎？重點是，現在，你將為了你無情殺死的「怪物」而付出代價！")
            time.sleep(1)
            player_data.setdefault("un",{"floor":0,"mh":500,"ma":300})
            battle(boss_list[player_data["un"]["floor"]%5],player_data["un"]["mh"],player_data["un"]["ma"])
          else:
            print("你：是，那又怎樣？那些都是怪物啊！")
            time.sleep(1)
            print("？？？：你又如何知道那是怪物？誰跟你說的？你一次又一次進行所謂的「冒險」，你怎麼知道你究竟殺了什麼？你怎麼知道你不是弒去了一個又一個的勇者，屠遍了所有村莊？")
            time.sleep(1)
            print("你：你究竟是誰？")
            time.sleep(1)
            print("？？？：不重要，重點是，你今天\n不\n會\n走\n出\n這\n裡")
            player_data.setdefault("un",{"floor":0,"mh":500,"ma":300})
            battle(boss_list[player_data["un"]["floor"]%5],player_data["un"]["mh"],player_data["un"]["ma"])
        else:
          print("你的等級不夠！至少要15等！")
          print("？？？：看起來，你還沒有到真正的時候...出去吧，不要再冒險了，也不要再回來了。")
    else:
      print("你看著地牢，決定先不要進去...")

  elif inp == "使用":
    item = input("請輸入物品名稱：")
    amount = input("請輸入數量：")
    msg = use_item(item,int(amount))
    print(msg)

  elif inp == "寄信":
    to = input("收件者名稱：")
    title = input("請輸入標題：")
    text = input("請輸入內容：")
    if input("你要寄出物品嗎？還是這樣就好？(y/n)") == "y":
      item = input("請輸入物品名稱：")
      amount = input("請輸入數量：")
      send_mail(to,title,text,item,int(amount))
    else:
      send_mail(to,title,text,None,0)

  elif inp == "信箱":
    if len(data[name]["mail_box"]) == 0:
      print("    空空如也owo")
    else:
      for key,value in data[name]["mail_box"].items():
        if "item" in value:
          print(f'''
  寄件者：{value["author"]}
  ID：{key}
  標題：{value["title"]}
  內文：{value["text"]}
  物品：{value["item"]}
  數量：{value["amount"]}
  ========================''')
        else:
          print(f'''
  寄件者：{value["author"]}
  ID：{key}
  標題：{value["title"]}
  內文：{value["text"]}
  ========================''')

  elif inp == "讀取":
    id = input("請輸入信件ID：")
    if id in data[name]["mail_box"]:
      if "item" in data[name]["mail_box"][id]:
        item = data[name]["mail_box"][id]["item"]
        player_data["back"].setdefault(item,0)
        player_data["back"][item]+=data[name]["mail_box"][id]["amount"]
        print(f"你領取了{item}x{data[name]['mail_box'][id]['amount']}")
        data[name]["mail_box"].pop(id)
        write_wb(name,data)
      else:
        print("信件已標示為讀取！")
        data[name]["mail_box"].pop(id)
        write_wb(name,data)

    else:
      print("\033[91m未查到該信件！\033[0m")

  elif inp == "新增好友":
    user = input("請輸入用戶名稱：")
    menu_data = load_web("menu")
    friend_apply = load_web("friend_apply")
    data = load_web(name)
    if user == name:
      print("\033[91m沒必要吧🈹\033[0m")
    elif user in friend_apply[name]:
      print("\033[91m他已經對你發出了申請！試試看輸入「好友申請」來同意吧！\033[0m")
    elif user in data[name]["friend"]:
      print("\033[91m他已經是你的好友了!\033[0m")
    elif user in menu_data:
      requests.post(f"https://dbtest.lchenglin29.repl.co/friend_apply",json={"rqer":name,"user":user})
      print("好友申請已發送！")
    else:
      print("\033[91m該用戶不存在！\033[0m")

  elif inp == "刪除好友":
    data.setdefault("friend",[])
    user = input("請輸入好友名稱：")
    if user in data[name]["friend"]:
      data[name]["friend"].remove(user)
      print(f"已移除{user}！")
    else:
      print(f"\033[91m{user}不在你的好友清單內！\033[0m")

  elif inp == "好友申請":
    apply_data = load_web("friend_apply")
    if name in apply_data:
      if len(apply_data[name]) != 0:
        inap = True
        while inap:
          apply_data = load_web("friend_apply")
          if len(apply_data[name]) != 0:
            for ap in apply_data[name]:
              print(f"  {ap}")
              user = input("請輸入用戶名稱：\n輸入1退出頁面！")
              if user == "1":
                inap = False
                break
              if user in apply_data[name]:
                ans = input("是否同意？(y/n)")
                if ans == "y":
                  requests.post(f"https://dbtest.lchenglin29.repl.co/friend_accept",json={"rqer":name,"user":user})
#                  write_wb(name,data)
                  print("好友申請已同意！")
                  apply_data = load_web("friend_apply")
                  apply_data[name].remove(user)
                  write_wb("friend_apply",apply_data)
                if ans == "n":
                  print("好友申請已拒絕！")
                  apply_data = load_web("friend_apply")
                  apply_data[name].remove(user)
                  write_wb("friend_apply",apply_data)
          else:
            print("  空空如也owo")
            inap = False
            break
      else:
        print("  空空如也owo")
    else:
      print("  空空如也owo")
              
  elif inp == "好友列表":
    menu_data = load_web("menu")
    data[name].setdefault("friend",[])
    if len(data[name]["friend"]) != 0:
      for friend in data[name]["friend"]:
        if menu_data[friend] == 1:
          print(f"  {friend} 🔴")
        else:
          print(f"  {friend} 🟢")
    else:
      print("  空空如也owo")

  elif inp == "農田":
    player_data.setdefault("農田",{})
    if len(player_data["農田"]) == 0:
      print(f"  空空如也owo")
    else:
      for plant,grow in player_data["農田"]:
        print(f"  {plant} 成長度{grow}")

  elif inp == "種植":
    player_data.setdefault("農田",{})
    plant = input("請輸入植物名稱：")
    if plant in player_data["農田"]:
      if player_data["農田"][plant]:
        player_data["農田"].setdefault(plant,0)
        player_data["農田"][plant] += 1
  
  elif inp == "關閉通知":
    letter_noti = False
    print("\033[91m每輪信件通知關閉\033[0m")
  
  elif inp == "退出":
    print("\033[41m遊戲關閉！\033[0m")
    offline_req(name)
    run = False

  elif inp == "商店":
    if input("你需要看一下你的背包嗎？(y/n)") == 'y':
      show_back()
    print("")
    for it,val in shop_list.items():
      if it != "黃金":
        print(f"商品名稱：{it}\n描述：{val['des']}\n價格：{val['price']} 黃金 \033[43m(你可以買：{int(player_data['back']['黃金']/val['price'])}個)\033[0m\n")
      else:
        print(f"商品名稱：{it}\n描述：{val['des']}\n價格：{val['price']} 鐵礦 \033[43m(你可以買：{int(player_data['back']['鐵礦']/val['price'])}個)\033[0m\n")
    item = input("請輸入想買的東西：")
    amount = input("請輸入想買的數量：")
    buy(item,int(amount))
  
  else:
    print(f"\033[91m你在打什麼啦{player_data['name']}？「{inp}」是什麼？\033[0m")

  tips = ""
  data = load_web(name)
  data[f"{name}"]["player_data"] = player_data
  requests.post(f"https://4bf6858d-3eb9-4003-8651-fbb070c7b5fc-00-32cyicqpj0myc.janeway.replit.dev/write_js/{name}",json=data)
  write_js(name,data)