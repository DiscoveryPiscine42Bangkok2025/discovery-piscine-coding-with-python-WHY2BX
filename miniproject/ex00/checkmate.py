def checkmate(board):
    rows = board.splitlines()   # ['R...', '.K..', '..P.', '....']
    board_size = len(rows)
    
    king_pos = None
    for r in range(board_size):
        for c in range(board_size):
            if rows[r][c] == "K":
                king_pos = (r, c)
                break
    kr, kc = king_pos
    pawn_attack = [(kr-1, kc-1), (kr-1, kc+1)]  # ช่องที่ Pawn สามารถโจมตีได้

    for (r, c) in pawn_attack:
        if 0 <= r < board_size and 0 <= c < board_size and rows[r][c] == "P":
            return "Success"
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for dr, dc in directions:
        r, c = kr, kc
        while True:
            r += dr
            c += dc
            if not (0 <= r < board_size and 0 <= c < board_size):  # ออกนอกกระดาน
                break
            piece = rows[r][c]
            if piece != ".":   # เจอตัวแรก
                if piece in ("R", "Q"): 
                    return "Success"
                break
    directions = [(-1,-1), (-1,1), (1,-1), (1,1)]

    for dr, dc in directions:
        r, c = kr, kc
        while True:
            r += dr
            c += dc
            if not (0 <= r < board_size and 0 <= c < board_size):
                break
            piece = rows[r][c]
            if piece != ".":
                if piece in ("B", "Q"):
                    return "Success"
                break
    return "Fail"