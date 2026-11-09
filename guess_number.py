"""猜数字游戏 —— 一个简单的命令行小游戏。

电脑随机想一个数，玩家来猜；猜错会提示"大了"或"小了"，
在规定的次数内猜中即获胜。

运行方式：
    python guess_number.py
"""

import random

# 难度配置：名称 -> (数字下界, 数字上界, 最大猜测次数)
DIFFICULTIES = {
    "简单": (1, 50, 10),
    "普通": (1, 100, 8),
    "困难": (1, 200, 6),
}


def choose_difficulty():
    """让玩家选择难度，返回 (数字下界, 数字上界, 最大猜测次数)。"""
    print("请选择难度：")
    for name, (low, high, chances) in DIFFICULTIES.items():
        print(f"  {name}：猜 {low}~{high} 之间的数，共 {chances} 次机会")

    while True:
        choice = input("输入难度（简单/普通/困难）：").strip()
        if choice in DIFFICULTIES:
            low, high, chances = DIFFICULTIES[choice]
            print(f"\n已选择「{choice}」难度，游戏开始！\n")
            return low, high, chances
        print("输入有误，请重新输入。")


def get_guess(low, high, used, max_chances):
    """让玩家输入一个数字，输入不合法时会提示并让其重新输入。"""
    while True:
        raw = input(f"[第 {used + 1}/{max_chances} 次] 请输入 {low}~{high} 之间的整数：").strip()
        try:
            num = int(raw)
        except ValueError:
            print("输入有误，请输入整数。")
            continue
        if low <= num <= high:
            return num
        print(f"数字需在 {low}~{high} 之间，请重新输入。")


def play_round():
    """进行一局游戏，猜中返回 True，否则返回 False。"""
    low, high, max_chances = choose_difficulty()
    answer = random.randint(low, high)
    used = 0

    while used < max_chances:
        guess = get_guess(low, high, used, max_chances)
        used += 1

        if guess == answer:
            print(f"恭喜你猜中了！答案是 {answer}，你只用了 {used} 次。")
            return True

        if used == max_chances:
            break

        hint = "小" if guess < answer else "大"
        print(f"猜{hint}了，还剩 {max_chances - used} 次机会。\n")

    print(f"很遗憾，机会用完了。正确答案是 {answer}。")
    return False


def main():
    """程序入口：循环进行游戏，退出时统计总战绩。"""
    print("=" * 42)
    print("        欢迎来到猜数字游戏！")
    print("=" * 42)

    total, wins = 0, 0
    while True:
        if play_round():
            wins += 1
        total += 1

        again = input("\n再来一局吗？按回车继续，输入 n 退出：").strip().lower()
        if again in ("n", "no", "不", "退出"):
            break

    print(f"\n游戏结束！你一共玩了 {total} 局，赢了 {wins} 局。再见！")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n游戏已退出，再见！")
