import random

coins = 0
count = 0
if coins < 5:
    # 提示充值
    print("金币不足请充值！")
    while True:
        money = int(input("请输入充值金额："))
        if money % 10 == 0:
            # 10的倍数，20个金币
            coins += money // 10 * 20
            print("充值成功，当前余额%d" % coins)
            answer = input("是否开始游戏（y/n）？")
            while coins > 5 and answer == "y":
                # 扣除金币
                coins -= 5
                # 赠送金币
                coins += 1
                # 产生2个随机的骰子数
                ran1 = random.randint(1, 6)
                ran2 = random.randint(1, 6)
                guess = input("请猜大小：")
                if (guess == "大" and (ran1 + ran2) > 6) or (guess == "小" and (ran1 + ran2) <= 6):
                    print("恭喜，胜！")
                    coins += 2
                else:
                    print("猜错，败！")
                count += 1
                answer = input("是否继续游戏（y/n）？")
            print("共玩了%d次，剩余金币%d" % (count, coins))
            break
        else:
            print("不是10的倍数，充值失败！")
