deck_a = list(map(int, input().split()))
deck_b = list(map(int, input().split()))

score_a = 0
score_b = 0
results = []

for i in range(0, 10):
    if   deck_a[i] > deck_b[i]:
        score_a += 3
        results.append("A")
    elif deck_a[i] < deck_b[i]:
        score_b += 3
        results.append("B")
    else:
        score_a += 1
        score_b += 1
        results.append("D")

if   score_a > score_b:
    result = "A"
elif score_a < score_b:
    result = "B"
else:
    if "A" in results or "B" in results:
        while "D" in results:
            results.remove("D")
        result = results[len(results) - 1]
    else:
        result = "D"
print(score_a, score_b, sep = " ", end = "\n")
print(result)
