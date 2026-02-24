"""
🐸 HoppyPy 示例 02: 数据结构
==============================
Series 2 - The Architect | 架构师篇

在这个示例中，你将学习：
- 列表 (List) - 有序的数据集合
- 字典 (Dict) - 键值对数据存储
- 循环遍历和条件判断
- 列表推导式

💡 在 HoppyPy 平台上体验互动版本：
   https://www.hoppypy.com/en/learn/python-architect/00-the-workshop
"""

# ============================================================
# 🎯 列表 (List) - Hoppy 的冒险装备
# ============================================================

print("🎒 Hoppy 的冒险背包")
print("=" * 40)

backpack = ["Python 教程", "能量饮料", "Bug 喷雾", "调试眼镜"]

# 查看背包
for i, item in enumerate(backpack, 1):
    print(f"   {i}. {item}")

# 添加新装备
backpack.append("AI 魔杖")
print(f"\n✨ 获得新装备！背包里现在有 {len(backpack)} 件物品")

# 查看最后一件
print(f"🆕 最新装备: {backpack[-1]}")

# ============================================================
# 🎯 字典 (Dict) - Hoppy 的角色属性
# ============================================================

print("\n\n📊 Hoppy 的角色属性面板")
print("=" * 40)

hoppy_stats = {
    "name": "Hoppy",
    "level": 5,
    "hp": 100,
    "skills": ["print()", "input()", "for loop", "if/else"],
    "exp": 2500,
    "next_level_exp": 5000,
}

# 展示角色信息
print(f"   🐸 {hoppy_stats['name']} (Lv.{hoppy_stats['level']})")
print(f"   ❤️  HP: {'█' * (hoppy_stats['hp'] // 10)}{'░' * (10 - hoppy_stats['hp'] // 10)} {hoppy_stats['hp']}%")

# 经验值进度条
progress = hoppy_stats["exp"] / hoppy_stats["next_level_exp"]
bar_length = 20
filled = int(bar_length * progress)
print(f"   ⭐ EXP: {'▓' * filled}{'░' * (bar_length - filled)} {hoppy_stats['exp']}/{hoppy_stats['next_level_exp']}")

print(f"\n   🛡️ 已掌握技能:")
for skill in hoppy_stats["skills"]:
    print(f"      ✅ {skill}")

# ============================================================
# 🎯 实战：冒险任务系统
# ============================================================

print("\n\n🗺️ 冒险任务面板")
print("=" * 40)

quests = [
    {"name": "打印你的第一行代码", "difficulty": "⭐", "reward": 100, "completed": True},
    {"name": "用变量存储秘密", "difficulty": "⭐", "reward": 150, "completed": True},
    {"name": "编写循环求和程序", "difficulty": "⭐⭐", "reward": 300, "completed": True},
    {"name": "构建待办事项列表", "difficulty": "⭐⭐⭐", "reward": 500, "completed": False},
    {"name": "创建个人信息管理器", "difficulty": "⭐⭐⭐⭐", "reward": 800, "completed": False},
]

for quest in quests:
    status = "✅" if quest["completed"] else "🔲"
    print(f"   {status} {quest['name']}")
    print(f"      难度: {quest['difficulty']}  奖励: {quest['reward']} EXP")

# 统计完成情况
completed = [q for q in quests if q["completed"]]
total_reward = sum(q["reward"] for q in completed)
print(f"\n📈 完成进度: {len(completed)}/{len(quests)}")
print(f"💰 已获得奖励: {total_reward} EXP")

# ============================================================
# 🎯 列表推导式 - Python 的独门绝技
# ============================================================

print("\n\n⚡ 列表推导式 - 一行代码的魔法")
print("=" * 40)

# 生成乘法表
print("\n📐 九九乘法表 (部分):")
multiplication = [f"{i}×{j}={i*j}" for i in range(1, 4) for j in range(1, 4)]
for item in multiplication:
    print(f"   {item}")

# 过滤数据
numbers = list(range(1, 21))
evens = [n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 != 0]
print(f"\n🔢 1-20 中的偶数: {evens}")
print(f"🔢 1-20 中的奇数: {odds}")

print("\n🎉 太棒了！你已经掌握了 Python 的核心数据结构！")
print("👉 继续深造: https://www.hoppypy.com")
