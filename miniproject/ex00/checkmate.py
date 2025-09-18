def checkmate(board):
    rows = board.splitlines()
    board_size = len(rows)
    
    king_pos = None
    for r in range(board_size):
        for c in range(board_size):
            if rows[r][c] == "K":
                king_pos = (r, c)
                break
    kr, kc = king_pos
    pawn_position = [(kr+1, kc-1), (kr+1, kc+1)]  # พิกัดที่ถ้า pawn อยู่ king จะโดน check

    for (r, c) in pawn_position:
        if 0 <= r < board_size and 0 <= c < board_size and rows[r][c] == "P":
            return "Success"
    
    # ตรวจหา R, Q แนวตั้งและแนวนอน
    plus_directions = [(-1,0), (1,0), (0,-1), (0,1)]
    for pdr, pdc in plus_directions:
        r, c = kr, kc
        while True:
            r += pdr
            c += pdc
            if not (0 <= r < board_size and 0 <= c < board_size):  # ออกนอกกระดาน
                break
            check_pos = rows[r][c]
            if check_pos != ".":   #กันเจอหมากซ้อนกัน (กินไม่ถึง)
                if check_pos in ("R", "Q"): 
                    return "Success"
                break

    # ตรวจหา B, Q แนวแทยง
    diag_directions = [(-1,-1), (-1,1), (1,-1), (1,1)]
    for ddr, ddc in diag_directions:
        r, c = kr, kc
        while True:
            r += ddr
            c += ddc
            if not (0 <= r < board_size and 0 <= c < board_size):
                break
            check_pos = rows[r][c]
            if check_pos != ".":
                if check_pos in ("B", "Q"):
                    return "Success"
                break
    
    return "Fail"