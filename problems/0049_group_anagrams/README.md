# 49. Group Anagrams

- **難易度**: Medium
- **トピック**: 配列, ハッシュマップ, 文字列, ソート
- **URL**: https://leetcode.com/problems/group-anagrams/

## 問題概要

文字列の配列 `strs` が与えられる。アナグラム同士をグループにまとめて返せ。
順序は問わない。

### 例

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

### 制約

- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- `strs[i]` は小文字の英字のみ

## 考察

- 242 Valid Anagram の発展版。1対1の判定→グループ分けへ
- アナグラム同士はソートすると同じ文字列になる性質を利用
- ソート結果を辞書のキーにすれば、1回のループでグループ分けできる
- 全ペア比較は O(n²) で遅いので、辞書を使って O(n) のループにする

## 解法

### Python（ソート + ハッシュマップ）
```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    d = {}
    for i in range(len(strs)):
        key = "".join(sorted(strs[i]))
        if key in d:
            d[key].append(strs[i])
        else:
            d[key] = [strs[i]]
    return list(d.values())
```
- **計算量**: 時間 O(n * k log k), 空間 O(n * k)
  - n = 文字列の個数, k = 各文字列の最大長
  - 各文字列のソートに O(k log k)、それを n 回繰り返す

## 学んだこと・反省

- ソート結果を辞書のキーにするパターンは汎用性が高い
- `"".join(sorted(s))` でリストを文字列に変換してキーにできる
- `in` 演算子の向き: `key in d` であって `d in key` ではない
- 辞書に「キーがあれば追加、なければ新規作成」のパターンは頻出（`defaultdict(list)` を使うとさらに簡潔に書ける）
