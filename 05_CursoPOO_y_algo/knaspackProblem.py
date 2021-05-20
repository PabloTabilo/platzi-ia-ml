
def recursiveSolve(s, w, v, n):
    if n==0 or s==0:
        return 0
    if w[n-1] > s:
        return recursiveSolve(s, w, v, n-1)
    return max(v[n-1] + recursiveSolve(s - w[n-1], w, v, n-1), recursiveSolve(s, w, v, n-1))

def solve(s,w,v,n):
    dp = [0 for i in range(n)]
    # {A}, {B}, {C}, {D}
    for i in range(n):
        vis =[False for i in range(n)]
        vis[i] = True
        ac = w[i]
        dp[i] = v[i]
        k = 1
        # {A,B}, {A,C}, {A,D}
        # {{A,B},C}, {{A,B},D}
        while k<n-1:
            best = dp[i]
            for j in range(n):
                if not vis[j] and ac+w[j]<=s and best < dp[i] + v[j]:
                    best = dp[i] + v[j]
                    t_ac=ac+w[j]
                    bestJ=j
            vis[bestJ]=True
            dp[i] = best
            ac += t_ac
            k+=1
    print(dp)
    return max(dp)

if __name__ == "__main__":
    v = [60, 105, 145, 3]
    w = [15, 20, 25, 2]
    s = 38
    #v = [60, 100, 120]
    #w = [10, 20, 30]
    #s = 50
    n = len(v)
    print(solve(s, w, v, n))