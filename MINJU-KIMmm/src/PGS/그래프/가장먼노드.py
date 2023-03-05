import heapq, sys

def solution(n, edge):
    answer = 0
    
    connect = [[] for _ in range(n+1)]
    for a, b in edge:
        connect[a].append(b)
        connect[b].append(a)
    
    def dijkstra(start):
        INF = sys.maxsize
        
        dis_list = [INF for _ in range(n+1)]
        
        dis_list[start] = 0
        pq = []
        heapq.heappush(pq, (0, start))
        
        while pq:
            dis, node = heapq.heappop(pq)
            
            if dis_list[node]<dis:
                continue
                
            for n_node in connect[node]:
                if dis_list[n_node] > 1+dis_list[node]:
                    dis_list[n_node] = 1+dis_list[node]
                    heapq.heappush(pq, (dis_list[n_node], n_node))
        
        max_val = 0
        for d in dis_list:
            if d!=INF and max_val < d:
                max_val = d
                
        return dis_list.count(max_val)
            
    answer = dijkstra(1)
    return answer
