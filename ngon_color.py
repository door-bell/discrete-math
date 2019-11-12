# Answers the question: how many ways can you color an n-gon with k colors?

def countWays(sides, colors):
    result = []
    ngon = [None] * sides
    backtrack(ngon, colors, 0, result)
    return result

def backtrack(ngon, colors, current, result):
    if current == len(ngon):
        result.append(list(ngon))
        return
    for i in range(1, colors + 1):
        if isSafe(ngon, current, i):
            ngon[current] = i
            backtrack(ngon, colors, current + 1, result)
            ngon[current] = None

def isSafe(ngon, index, color):
    not_prev_color = ngon[index - 1] != color
    if index == len(ngon) - 1:
        return not_prev_color and ngon[0] != color
    return not_prev_color and ngon[index + 1] != color

if __name__ == "__main__":
    # Can also simply print countWays(n, k) to see each configuration.
    ways = countWays(5, 4)
    for way in ways:
        print(way)
    print(len(ways))