class Solution:

  def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
    m, n = len(img), len(img[0])
    res = [[0] * n for _ in range(m)]

    for i in range(m):
      for j in range(n):
        total_sum = 0
        count = 0
        for r in range(max(0, i - 1), min(m, i + 2)):
          for c in range(max(0, j - 1), min(n, j + 2)):
            total_sum += img[r][c]
            count += 1
        res[i][j] = total_sum // count

    return res