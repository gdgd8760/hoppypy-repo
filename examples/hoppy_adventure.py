"""
🐸 HoppyPy 冒险游戏 — Hoppy's Terminal Adventure
===================================================
一个在终端里运行的文字冒险 RPG！

通过回答 Python 编程问题来帮助 Hoppy 击败 Bug 怪兽，
拯救被困在错误代码中的程序员们！

运行方法:
    python examples/hoppy_adventure.py

💡 完整的互动学习体验请访问: https://www.hoppypy.com
"""

import random
import time
import sys


# ============================================================
# 🎨 工具函数
# ============================================================

def slow_print(text: str, delay: float = 0.02) -> None:
    """逐字打印，营造打字机效果"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def print_separator() -> None:
    print(f"\n{'═' * 50}")


def print_hp_bar(name: str, hp: int, max_hp: int, emoji: str = "❤️") -> None:
    """显示 HP 进度条"""
    bar_len = 20
    filled = int(bar_len * hp / max_hp)
    bar = "█" * filled + "░" * (bar_len - filled)
    print(f"  {emoji} {name}: [{bar}] {hp}/{max_hp}")


# ============================================================
# 📦 游戏数据
# ============================================================

HOPPY_ART = """
      @..@
     (----)
    ( >__< )
    ^^    ^^
"""

BOSS_ART = """
     ╔══╗
    ╔╝🐛╚╗
    ║ BUG ║
    ╚══╦══╝
       ║
"""

VICTORY_ART = """
    ╔═══════════════════════════════╗
    ║   🏆  VICTORY!  🏆           ║
    ║   Hoppy saved the code!      ║
    ╚═══════════════════════════════╝
"""

GAME_OVER_ART = """
    ╔═══════════════════════════════╗
    ║   💀  GAME OVER  💀          ║
    ║   The bugs won this time...  ║
    ╚═══════════════════════════════╝
"""

# Python 编程问题库
QUESTIONS: list[dict] = [
    # --- 简单 ---
    {
        "question": "在 Python 中，如何打印 'Hello World'？",
        "options": ["A) echo 'Hello World'", "B) print('Hello World')", "C) console.log('Hello World')", "D) printf('Hello World')"],
        "answer": "B",
        "difficulty": 1,
        "hint": 'Python 的输出函数和"打印"这个词的英文一样 🖨️',
    },
    {
        "question": "以下哪个是有效的 Python 变量名？",
        "options": ["A) 2name", "B) my-name", "C) my_name", "D) class"],
        "answer": "C",
        "difficulty": 1,
        "hint": "Python 变量名可以包含字母、数字和下划线，但不能以数字开头 📝",
    },
    {
        "question": "Python 中的 f-string 用什么符号标记？",
        "options": ["A) ${ }", "B) {{ }}", "C) %s", "D) { }"],
        "answer": "D",
        "difficulty": 1,
        "hint": "f-string 在字符串前加 f，用花括号包裹变量 🎯",
    },
    {
        "question": "len('Python') 的结果是什么？",
        "options": ["A) 5", "B) 6", "C) 7", "D) Error"],
        "answer": "B",
        "difficulty": 1,
        "hint": "len() 计算字符串中的字符数，数一数 P-y-t-h-o-n 🔤",
    },
    # --- 中等 ---
    {
        "question": "[1, 2, 3] + [4, 5] 的结果是？",
        "options": ["A) [5, 7]", "B) [1, 2, 3, 4, 5]", "C) Error", "D) 15"],
        "answer": "B",
        "difficulty": 2,
        "hint": "列表的 + 运算符是拼接，不是数学加法 📋",
    },
    {
        "question": "以下代码输出什么？\n   x = [1, 2, 3]\n   print(x[-1])",
        "options": ["A) 1", "B) 2", "C) 3", "D) Error"],
        "answer": "C",
        "difficulty": 2,
        "hint": "负数索引从列表末尾开始数，-1 就是最后一个 🎯",
    },
    {
        "question": "'hello'.upper() 的结果是？",
        "options": ["A) 'Hello'", "B) 'HELLO'", "C) 'hello'", "D) Error"],
        "answer": "B",
        "difficulty": 2,
        "hint": "upper() 把所有字母变成大写 📢",
    },
    {
        "question": "Python 字典中，如何安全地获取一个可能不存在的键？",
        "options": ["A) dict[key]", "B) dict.get(key)", "C) dict.find(key)", "D) dict.fetch(key)"],
        "answer": "B",
        "difficulty": 2,
        "hint": "有一个方法可以在键不存在时返回 None 而不是报错 🔒",
    },
    # --- 困难 ---
    {
        "question": "以下哪个是列表推导式？",
        "options": ["A) list(range(5))", "B) [x for x in range(5)]", "C) map(int, range(5))", "D) {x: x for x in range(5)}"],
        "answer": "B",
        "difficulty": 3,
        "hint": "列表推导式在方括号 [] 内使用 for 表达式 ⚡",
    },
    {
        "question": "lambda x: x * 2 是什么？",
        "options": ["A) 一个类", "B) 一个匿名函数", "C) 一个装饰器", "D) 一个错误"],
        "answer": "B",
        "difficulty": 3,
        "hint": "lambda 创建一个没有名字的小函数 🔧",
    },
    {
        "question": "try-except 中的 finally 块什么时候执行？",
        "options": ["A) 只在出错时", "B) 只在没出错时", "C) 无论是否出错都执行", "D) 永不执行"],
        "answer": "C",
        "difficulty": 3,
        "hint": "finally 的意思是'最终'，暗示了它的行为 🏁",
    },
    {
        "question": "以下代码输出什么？\n   def foo(a=[]):\n       a.append(1)\n       return a\n   print(foo(), foo())",
        "options": ["A) [1] [1]", "B) [1] [1, 1]", "C) [1, 1] [1, 1]", "D) Error"],
        "answer": "B",
        "difficulty": 3,
        "hint": "Python 的默认可变参数是一个经典陷阱！默认列表在函数定义时创建一次 🪤",
    },
]


# ============================================================
# 🎮 游戏核心逻辑
# ============================================================

class Game:
    """Hoppy 的终端冒险游戏"""

    def __init__(self) -> None:
        self.hoppy_hp = 100
        self.hoppy_max_hp = 100
        self.boss_hp = 0
        self.boss_max_hp = 0
        self.score = 0
        self.level = 1
        self.questions_answered = 0
        self.correct_answers = 0

    def show_title(self) -> None:
        """显示游戏标题"""
        print("\n" * 2)
        print("  ╔═══════════════════════════════════════════╗")
        print("  ║                                           ║")
        print("  ║   🐸 HOPPY'S TERMINAL ADVENTURE 🐸       ║")
        print("  ║                                           ║")
        print("  ║   用 Python 知识拯救世界！                ║")
        print("  ║                                           ║")
        print("  ╚═══════════════════════════════════════════╝")
        print(HOPPY_ART)

    def show_intro(self) -> None:
        """叙事开场"""
        print_separator()
        slow_print("📖 在一个被代码构建的世界里...")
        slow_print("   邪恶的 Bug 军团入侵了 Python 王国！")
        slow_print("   程序员们被困在无限循环中无法逃脱...")
        slow_print(f"   只有你和 Hoppy 能拯救他们！\n")
        slow_print("🎮 规则:")
        slow_print("   • 回答 Python 编程问题来攻击 Bug 怪兽")
        slow_print("   • 答对 = 对 Bug 造成伤害 💥")
        slow_print("   • 答错 = Hoppy 受到伤害 💔")
        slow_print("   • 输入 H 可以获取提示（但会减少得分）")
        slow_print("   • 击败所有 Boss 就能拯救 Python 王国！\n")
        input("  按 Enter 开始冒险... ")

    def start_boss_fight(self, boss_name: str, boss_hp: int) -> None:
        """开始 Boss 战"""
        self.boss_hp = boss_hp
        self.boss_max_hp = boss_hp
        print_separator()
        print(f"\n  ⚔️  BOSS 战: {boss_name}!")
        print(BOSS_ART)
        slow_print(f"  🐛 {boss_name} 出现了！HP: {boss_hp}")
        print()

    def show_battle_status(self, boss_name: str) -> None:
        """显示战斗状态"""
        print(f"\n  {'─' * 40}")
        print_hp_bar("Hoppy", self.hoppy_hp, self.hoppy_max_hp, "🐸")
        print_hp_bar(boss_name, max(0, self.boss_hp), self.boss_max_hp, "🐛")
        print(f"  ⭐ 得分: {self.score}")
        print(f"  {'─' * 40}")

    def ask_question(self, question_data: dict) -> bool:
        """提问并返回是否答对"""
        self.questions_answered += 1
        difficulty_stars = "⭐" * question_data["difficulty"]

        print(f"\n  ❓ [{difficulty_stars}] {question_data['question']}\n")
        for option in question_data["options"]:
            print(f"     {option}")

        while True:
            answer = input("\n  👉 你的答案 (A/B/C/D 或 H 获取提示): ").strip().upper()
            if answer == "H":
                print(f"\n  💡 提示: {question_data['hint']}")
                self.score = max(0, self.score - 5)
                continue
            if answer in ("A", "B", "C", "D"):
                break
            print("  ⚠️  请输入 A、B、C、D 或 H")

        if answer == question_data["answer"]:
            self.correct_answers += 1
            return True
        return False

    def battle_round(self, boss_name: str, question_data: dict) -> None:
        """一回合战斗"""
        self.show_battle_status(boss_name)
        correct = self.ask_question(question_data)

        if correct:
            damage = question_data["difficulty"] * 15 + random.randint(5, 15)
            self.boss_hp -= damage
            self.score += question_data["difficulty"] * 10
            print(f"\n  ✅ 正确！Hoppy 对 {boss_name} 造成了 {damage} 点伤害！💥")
        else:
            damage = question_data["difficulty"] * 10 + random.randint(5, 10)
            self.hoppy_hp -= damage
            correct_answer = question_data["answer"]
            correct_text = question_data["options"][ord(correct_answer) - ord("A")]
            print(f"\n  ❌ 错误！正确答案是: {correct_text}")
            print(f"     {boss_name} 对 Hoppy 造成了 {damage} 点伤害！💔")

    def run_chapter(self, chapter: int, boss_name: str, boss_hp: int, questions: list[dict]) -> bool:
        """运行一个章节，返回是否胜利"""
        print_separator()
        slow_print(f"\n  📖 第 {chapter} 章")
        self.start_boss_fight(boss_name, boss_hp)
        random.shuffle(questions)

        for q in questions:
            if self.boss_hp <= 0:
                print(f"\n  🎉 {boss_name} 被击败了！！")
                self.score += 50
                return True
            if self.hoppy_hp <= 0:
                return False
            self.battle_round(boss_name, q)

        return self.boss_hp <= 0

    def show_results(self) -> None:
        """显示最终结果"""
        print_separator()
        accuracy = (self.correct_answers / self.questions_answered * 100) if self.questions_answered > 0 else 0

        print(f"\n  📊 冒险统计")
        print(f"  {'─' * 35}")
        print(f"  ❓ 总题数:   {self.questions_answered}")
        print(f"  ✅ 答对:     {self.correct_answers}")
        print(f"  🎯 正确率:   {accuracy:.0f}%")
        print(f"  ⭐ 最终得分: {self.score}")

        if accuracy >= 80:
            print(f"\n  🌟 评价: Python 大师！你太强了！")
        elif accuracy >= 60:
            print(f"\n  👍 评价: 不错！继续努力学习！")
        else:
            print(f"\n  💪 评价: 加油！去 HoppyPy 多练练吧！")

        print(f"\n  {'─' * 35}")
        print(f"  📚 想要系统学习 Python？")
        print(f"  👉 https://www.hoppypy.com")
        print(f"  {'─' * 35}\n")

    def run(self) -> None:
        """运行游戏主循环"""
        self.show_title()
        self.show_intro()

        # 按难度分组
        easy = [q for q in QUESTIONS if q["difficulty"] == 1]
        medium = [q for q in QUESTIONS if q["difficulty"] == 2]
        hard = [q for q in QUESTIONS if q["difficulty"] == 3]

        chapters = [
            (1, "🐛 语法蠕虫 (Syntax Worm)", 50, easy),
            (2, "🕷️ 逻辑蜘蛛 (Logic Spider)", 70, medium),
            (3, "🐉 异常巨龙 (Exception Dragon)", 90, hard),
        ]

        for chapter_num, boss_name, boss_hp, questions in chapters:
            won = self.run_chapter(chapter_num, boss_name, boss_hp, questions)
            if not won:
                if self.hoppy_hp <= 0:
                    print(GAME_OVER_ART)
                    slow_print("  💀 Hoppy 倒下了...但不要放弃！")
                    slow_print("  📚 去 https://www.hoppypy.com 学习更多 Python 知识，再来挑战！\n")
                    self.show_results()
                    return

            # 战斗间恢复
            if self.hoppy_hp < self.hoppy_max_hp:
                heal = 30
                self.hoppy_hp = min(self.hoppy_max_hp, self.hoppy_hp + heal)
                print(f"  💚 Hoppy 休息了一下，恢复了 {heal} HP!")

        # 全部通关
        print(VICTORY_ART)
        slow_print("  🎊 恭喜！你和 Hoppy 成功拯救了 Python 王国！")
        slow_print("  🐸 Hoppy: '谢谢你，勇士！我们一起让代码变得更美好！'\n")
        self.show_results()


# ============================================================
# 🚀 启动游戏
# ============================================================

if __name__ == "__main__":
    try:
        game = Game()
        game.run()
    except KeyboardInterrupt:
        print("\n\n  👋 下次再来冒险吧！")
        print("  🐸 Hoppy 会在 https://www.hoppypy.com 等你！\n")
