# 217. Contains Duplicate

- **難易度**: Easy
- **トピック**: 配列, ハッシュマップ
- **URL**: https://leetcode.com/problems/contains-duplicate/

## 問題概要

整数の配列 `nums` が与えられる。
配列内に同じ値が **2回以上** 出現する場合は `true`、すべての要素がユニークなら `false` を返せ。

### 例

```
Input: nums = [1,2,3,1]
Output: true (1がインデックス0と3に出現)

Input: nums = [1,2,3,4]
Output: false (すべてユニーク)

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

### 制約

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

## 考察

- Two Sum と同じく辞書を使って「見た数」を記録していく
- 重複を見つけたら即 `return True`、最後まで見つからなければ `return False`
- `return False` をループの中に書くと最初の1要素で終了してしまうので注意

## 解法

### 解法1: 辞書

- **計算量**: 時間 O(n), 空間 O(n)
- ループしながら辞書に追加、追加前に存在チェック

```python
d = {}
for i in range(len(nums)):
    if nums[i] in d:
        return True
    else:
        d[nums[i]] = i
return False
```

### 解法2: set

- **計算量**: 時間 O(n), 空間 O(n)
- `set` は重複を自動除去する → 元の配列と長さが違えば重複あり

```python
return len(set(nums)) != len(nums)
```

## 学んだこと・反省

- `return` の位置（インデントの深さ）で動作が大きく変わる
- ループ内の `return False` はよくあるバグ。「全部見終わってから判定」を意識する
- 比較演算子（`==`, `!=`, `<`, `>`）の結果はそのまま `bool` 値なので `if X: return True else: return False` は `return X` と書ける
- `set` は重複を持てない集合。リストから作ると重複が自動除去される
