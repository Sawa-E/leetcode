# LeetCode 学習ガイド

## 進め方

### 1問の流れ

1. `/solve [問題番号 or URL]` を実行
2. 問題文を読み、自分で考える（最低5〜10分）
3. 方針が立ったらコードを書く
4. テストケースを通す（`./run.sh problems/.../solution.py`）
5. LeetCode上でSubmitする
6. 問題フォルダの `README.md` に考察・計算量・反省を記入

### 解けなかったとき

- ヒントを段階的にもらう（「ヒントちょうだい」と言えばOK）
- 15〜20分考えてダメなら解法を見る。**恥ではない**
- 解法を理解したら、見ずにもう一度自力で書く
- 2〜3日後にもう一度解き直す（間隔反復）

## 学習順序

トピック別に Easy → Medium と進む。各トピックの基礎を固めてから次へ。

| 順番 | トピック | 最初に解く問題 |
|------|---------|---------------|
| 1 | 配列 & ハッシュマップ | Two Sum, Contains Duplicate, Valid Anagram |
| 2 | Two Pointers | Valid Palindrome, Two Sum II, 3Sum |
| 3 | Sliding Window | Best Time to Buy and Sell Stock, Longest Substring Without Repeating |
| 4 | スタック | Valid Parentheses, Min Stack |
| 5 | 二分探索 | Binary Search, Search Insert Position |
| 6 | リンクリスト | Reverse Linked List, Merge Two Sorted Lists |
| 7 | 木 | Invert Binary Tree, Maximum Depth, Same Tree |
| 8 | BFS/DFS | Number of Islands, Clone Graph |
| 9 | ヒープ | Kth Largest Element, Top K Frequent Elements |
| 10 | DP | Climbing Stairs, House Robber, Coin Change |
| 11 | グラフ | Course Schedule, Pacific Atlantic Water Flow |
| 12 | バックトラッキング | Subsets, Permutations, Combination Sum |

## 言語の使い分け

- **Python**: メインで使用。記述が短く、面接で時間を節約できる
- **C++**: 速度が必要な問題や、C++指定の企業の面接対策時に使用

基本は Python 一本で進め、余裕があれば C++ でも解く。

## ローカル実行

```bash
./run.sh problems/0001_two_sum/solution.py    # Python
./run.sh problems/0001_two_sum/solution.cpp   # C++
```

## 面接に向けた意識

- **時間を測る**: 1問 Easy 15分、Medium 25分、Hard 40分を目安に
- **声に出して説明する**: 面接では思考プロセスを話しながら解く。普段から練習する
- **計算量を必ず答える**: 時間・空間の計算量はセットで把握する
- **エッジケースを考える**: 空配列、1要素、負の値、重複、最大値など

## 目安ペース

| 期間 | 目標 |
|------|------|
| 1週目 | 配列 & ハッシュマップの Easy を 5問 |
| 2週目 | Two Pointers + Sliding Window |
| 3〜4週目 | スタック、二分探索、リンクリスト |
| 5〜6週目 | 木、BFS/DFS |
| 7〜8週目 | DP、グラフ、バックトラッキング |
| 9週目〜 | Medium中心に周回、苦手トピック強化 |

時間はいくらでもあるとのことなので、このペースより速く進んでOK。
大事なのは**理解して定着させること**。数をこなすだけでは身につかない。
