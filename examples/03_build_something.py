"""
🐸 HoppyPy 示例 03: 构建实用工具
==================================
Series 3 · The Data Tinkerer | 数据与文本工具

在这个示例中，你将构建一个迷你文本分析器：
- 文件读写操作
- 字符串处理与统计
- 函数定义与调用
- 格式化输出

💡 在 HoppyPy 平台上体验更多项目：
   https://www.hoppypy.com/en/courses
"""

# ============================================================
# 🎯 迷你文本分析器
# ============================================================


def analyze_text(text: str) -> dict:
    """分析文本并返回统计数据"""
    words = text.split()
    sentences = text.count(".") + text.count("!") + text.count("?")
    unique_words = set(word.lower().strip(".,!?;:") for word in words)

    # 词频统计
    word_freq: dict[str, int] = {}
    for word in words:
        clean_word = word.lower().strip(".,!?;:")
        if clean_word:
            word_freq[clean_word] = word_freq.get(clean_word, 0) + 1

    # 按频率排序，取前 5
    top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]

    return {
        "characters": len(text),
        "words": len(words),
        "sentences": sentences,
        "unique_words": len(unique_words),
        "avg_word_length": round(sum(len(w) for w in words) / len(words), 1) if words else 0,
        "top_words": top_words,
    }


def display_report(stats: dict) -> None:
    """以精美格式展示分析报告"""
    print("\n" + "=" * 50)
    print("  🐸 HoppyPy 文本分析报告")
    print("=" * 50)

    print(f"\n  📊 基础统计")
    print(f"  {'─' * 35}")
    print(f"  📝 字符数      │ {stats['characters']:>10,}")
    print(f"  📖 单词数      │ {stats['words']:>10,}")
    print(f"  📄 句子数      │ {stats['sentences']:>10,}")
    print(f"  🔤 独立单词数  │ {stats['unique_words']:>10,}")
    print(f"  📏 平均词长    │ {stats['avg_word_length']:>10}")

    print(f"\n  🏆 高频词 TOP 5")
    print(f"  {'─' * 35}")
    for i, (word, count) in enumerate(stats["top_words"], 1):
        bar = "█" * min(count * 2, 20)
        print(f"  {i}. {word:<15} {bar} ({count})")

    # 词汇丰富度
    if stats["words"] > 0:
        richness = stats["unique_words"] / stats["words"] * 100
        print(f"\n  🎯 词汇丰富度: {richness:.1f}%")
        if richness > 70:
            print("     评价: 🌟 词汇丰富，表达多样！")
        elif richness > 50:
            print("     评价: 👍 用词不错，继续加油！")
        else:
            print("     评价: 💪 可以尝试使用更多不同的词汇！")

    print("\n" + "=" * 50)


# ============================================================
# 🎯 运行分析
# ============================================================

# 示例文本：Python 之禅（The Zen of Python）
sample_text = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases are not special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one obvious way to do it.
Although that way may not be obvious at first unless you are Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it is a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea. Let us do more of those.
"""

print("🐸 HoppyPy 文本分析器 v1.0")
print("   分析目标: The Zen of Python")

stats = analyze_text(sample_text)
display_report(stats)

print("\n🎉 你刚刚构建了一个真正的文本分析工具！")
print("💡 挑战: 试着修改代码，让它能分析你自己的文本")
print("👉 学习更多实战项目: https://www.hoppypy.com")
