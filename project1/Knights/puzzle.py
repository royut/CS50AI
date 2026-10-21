from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Statements for each puzzle
# puzzle 0
AStatement0 = And(AKnight, AKnave)
# puzzle 1
AStatement1 = And(AKnave, BKnave)
# puzzle 2
AStatement2 = Or(And(AKnight, BKnight), And(AKnave, BKnave))
BStatement2 = Or(And(AKnight, BKnave), And(AKnave, BKnight))
# puzzle 3
AStatement3a = Symbol('A says "I am a knave"')
AStatement3b = Symbol('A says "I am a knight"')
AStatement3 = And(Or(AStatement3a, AStatement3b), Not(And(AStatement3a, AStatement3b)))
BStatement3a = And(
    Implication(BKnight, AStatement3a),
    Implication(BKnave, Not(AStatement3a))
)
BStatement3b = CKnave
CStatement3 = AKnight

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Implication(AKnight, AStatement0),
    Implication(AKnave, Not(AStatement0))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Implication(AKnight, AStatement1),
    Implication(AKnave, Not(AStatement1)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Implication(AKnight, AStatement2),
    Implication(AKnave, Not(AStatement2)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Implication(BKnight, BStatement2),
    Implication(BKnave, Not(BStatement2))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    AStatement3,
    Implication(AStatement3a, And(
        Implication(AKnight, AKnave),
        Implication(AKnave, Not(AKnave))
    )),
    Implication(AStatement3b, And(
        Implication(AKnight, AKnight),
        Implication(AKnave, Not(AKnight))
    )),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    BStatement3a,
    Implication(BKnight, BStatement3b),
    Implication(BKnave, Not(BStatement3b)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    Implication(CKnight, CStatement3),
    Implication(CKnave, Not(CStatement3))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                # print(knowledge, symbol, model_check(knowledge, symbol))
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
