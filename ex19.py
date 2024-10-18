from collections import deque

def bfs(H, W, grid, start):
    # 移動可能な方向（上下左右）
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 幅優先探索のためのキュー
    queue = deque([start])
    
    # 訪問済みかどうかの記録
    visited = [[False] * W for _ in range(H)]
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y = queue.popleft()
        
        # 魚屋に到達した場合
        if grid[x][y] == 'g':
            return "Yes"
        
        # 四方向へ移動
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 範囲外や訪問済み、塀の場合は無視
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return "No"

# 入力処理
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

# スタート地点(s)とゴール地点(g)を見つける
start = None
for i in range(H):
    for j in range(W):
        if grid[i][j] == 's':
            start = (i, j)
            break
    if start:
        break

# 結果出力
print(bfs(H, W, grid, start))
