


def countsegs(segset):
    ret, points = 0,set()
    for a, b,c,d in segset:
        ret + = abs(a-c) + abs(b-d) + 1 - ((a, b) in points) - ((c,d) in points)
        points.update({(a, b),(c,d)})
    return ret


def dijkstra(data, start,end):
    import heapq
    from collections import defaultdict
    dirs = [(1, 0),(0,1),(-1,0),(0,-1)]
    distances = defaultdict(lambda:(float("inf"), set()))
    distances[* start, 1] = (0,set())
    queue = [(0, * start, 1)]
    while queue:
        dist, px,py,di = heapq.heappop(queue)
        _, p_set = distances[(px, py, di)]
        for ndi in range(-1, 2):
            dix, diy = dirs[(di + ndi) % 4]
            npx, npy, ndist = px + dix, py + diy, dist + 1 + 1000 * (ndi != 0)
            while (data[npx][npy] != "#" and data[npx + diy][npy+dix] == "#" and data[npx-diy][npy-dix] == "#"):
                npx, npy, ndist = npx + dix, npy + diy, ndist + 1

            nset = p_set | {seg(px, py, npx, npy)}

            if (npx, npy) == end:
                return (ndist, countsegs(nset))

            if data[npx][npy] != "#":
                o_dist, o_set = distances[(npx, npy, (di + ndi) % 4)]
                if o_dist == ndist:
                    if any((pos not in o_set) for pos in nset):
                        o_set.update(nset)
                        heapq.heappush(queue, (ndist,npx,npy,(di + ndi) % 4))
                elif o_dist > ndist:
                    distances[(npx, npy, (di + ndi) % 4)] = (ndist, nset)
                    heapq.heappush(queue, (ndist, npx, npy, (di + ndi) % 4))
    return distances 
