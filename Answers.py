import random

FORCE_UNIVERSAL_ANSWER_RATE = 0.13

UNIVERSAL_ANSWERS = [
        "你说你马呢",
        "那没事了",
        "真别逗我笑啊",
        "那可真是有趣呢",
        "就这？就这？",
        "你品，你细品",
        "不会真有人觉得是这样的吧，不会吧不会吧不会吧"
        "那可真是有够好笑的呢"
]

STRONG_EMOTION_ANSWERS = [
        "你急了急了急了？",
        "他急了，他急了！"
]

QUESTION_ANSWERS = [
        "不会真有人还不知道吧？",
        "你不知道还说你马呢？"
]

Q_MARK_ANSWERS = [
        "不会这还有人发？吧，不会吧不会吧不会吧",
        "你？你马呢"
]

FXXK_WORD_PATTERNS = [
        "nmsl",
        "NMSL",
        "cnm",
        "CNM",
        "你妈"
        "没妈"
]

STRONG_EMOTION_PATTERNS = [
        "！",
        "？？？",
        "???",
        "气抖冷"
]

QUESTION_PATTERNS = [
        "怎么",
        "什么",
        "咋"
]

Q_MARK_PATTERNS = [
        "？",
        "?"
]

FXXK_WORD_ANSWERS = [
        "就这？",
        "换点新词吧，球球辣"
]

BOT_NAME = [
        "你是",
        "你算"
]

def CheckPatterns(str_in, patterns):
    for p in patterns:
        if p in str_in:
            return True
    return False


def PickAnswer(question):
    if random.random() < FORCE_UNIVERSAL_ANSWER_RATE:
        return random.choice(UNIVERSAL_ANSWERS)

    if CheckPatterns(question, BOT_NAME):
        return "爷是彩云，是你亲爹"
    elif CheckPatterns(question, STRONG_EMOTION_PATTERNS):
        return random.choice(STRONG_EMOTION_ANSWERS)
    elif CheckPatterns(question, QUESTION_PATTERNS):
        return random.choice(QUESTION_ANSWERS)
    elif CheckPatterns(question, Q_MARK_PATTERNS):
        return random.choice(Q_MARK_ANSWERS)
    elif CheckPatterns(question, FXXK_WORD_PATTERNS):
        return random.choice(FXXK_WORD_ANSWERS)
    else:
        return random.choice(UNIVERSAL_ANSWERS)

def main():
    while True:
        question = input("<<< ")
        print(">>> " + PickAnswer(question))

if __name__ == "__main__":
    main()
