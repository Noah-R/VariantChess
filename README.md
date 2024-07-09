# VariantChess
A chess server for variants invented by me. Under active development.

Currently working on implementing chess in Python. To do:

    Test Insufficient Material
        KvK
        KBvK KNvK
        KBvKB same color
    
    Test 50/75 Move Rule

    More cleanup(make more helper functions)
    
Room for expansion:

    Formalize notation-based moving(currently runner.py uses an incomplete implementation as a temporary interface)

        In theory, it's possible that a move in algebraic notation will have to specify both the file and rank of a piece it's moving, ie: Qa2b1
        
        A move might not specify which file/rank the piece to move is on, even if there are two that can move there, if one moving there would leave the player in check, ie: Nd7 not Nbd7 with knights on b8 and f6, but the knight on f6 is pinned to the king