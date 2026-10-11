from flask import Flask, render_template, request
from collections import deque

app = Flask(__name__)

# 0=open, 1=hazard/blocked
DEFAULT_GRID = [
    [0,0,0,0,0,0,0,0],
    [0,1,1,0,1,0,1,0],
    [0,0,0,0,1,0,1,0],
    [0,1,0,0,0,0,0,0],
    [0,0,0,1,1,1,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,0,1,0,1,0,0],
    [0,0,0,0,0,0,0,0],
]
START=(0,0)
GOAL=(7,7)

def bfs(grid, start, goal):
    q=deque([start]); parent={start:None}
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        cur=q.popleft()
        if cur==goal: break
        for dr,dc in dirs:
            nr,nc=cur[0]+dr,cur[1]+dc
            nxt=(nr,nc)
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==0 and nxt not in parent:
                parent[nxt]=cur; q.append(nxt)
    if goal not in parent: return []
    path=[]; cur=goal
    while cur is not None:
        path.append(cur); cur=parent[cur]
    return path[::-1]

@app.route("/", methods=["GET","POST"])
def home():
    grid=[row[:] for row in DEFAULT_GRID]
    path=bfs(grid,START,GOAL)
    if request.method=="POST":
        try:
            r=int(request.form.get("hazard_row")); c=int(request.form.get("hazard_col"))
            if (r,c) not in [START,GOAL] and 0<=r<len(grid) and 0<=c<len(grid[0]):
                grid[r][c]=1
                path=bfs(grid,START,GOAL)
        except (TypeError,ValueError):
            pass
    path_set=set(path)
    cells=[]
    for r,row in enumerate(grid):
        for c,value in enumerate(row):
            pos=(r,c)
            if pos==START: kind="start"
            elif pos==GOAL: kind="goal"
            elif value==1: kind="hazard"
            elif pos in path_set: kind="route"
            else: kind="open"
            cells.append({"r":r,"c":c,"kind":kind})
    return render_template("index.html", cells=cells, rows=len(grid),
                           cols=len(grid[0]), path=path,
                           moves=max(0,len(path)-1), found=bool(path))

if __name__=="__main__":
    app.run(debug=True)
