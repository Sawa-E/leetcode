# 242. Valid Anagram

- **難易度**: Easy
- **トピック**: 配列, ハッシュマップ, 文字列
- **URL**: https://leetcode.com/problems/valid-anagram/

## 問題概要

2つの文字列 `s` と `t` が与えられる。
`t` が `s` のアナグラムであれば `true`、そうでなければ `false` を返せ。

アナグラム = 文字の並び替えで同じになる（使う文字の種類と数が同じ）

### 例

```
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
```

### 制約

- 1 <= s.length, t.length <= 5 * 10^4
- `s` と `t` は小文字の英字のみ

### Follow-up

入力がUnicode文字を含む場合、どう対応するか？

## 考察

- アナグラム = 同じ文字を同じ回数使っている
- まず長さが違えば即 `False`
- 各文字の出現回数を数えて比較すればよい
- `collections.Counter` を使えば1行でカウントできる

## 解法

### Python（Counter）
```python
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return collections.Counter(s) == collections.Counter(t)
```
- **計算量**: 時間 O(n), 空間 O(n)
  - n = 文字列の長さ。全文字を走査してカウントするため O(n)
  - カウント用の辞書に最大 O(n) の空間が必要

### 別解：ソート
```python
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```
- **計算量**: 時間 O(n log n), 空間 O(n)

## 学んだこと・反省

- `Counter` は文字列をそのまま渡せる（`list()` 変換は不要）
- `Counter` 同士は `==` で比較できる
- 全分岐で値を返すことを忘れないようにする（`None` が返るバグに注意）
- Follow-up: Unicode対応でも `Counter` ならそのまま動く（固定長配列ではなく辞書ベースのため）
