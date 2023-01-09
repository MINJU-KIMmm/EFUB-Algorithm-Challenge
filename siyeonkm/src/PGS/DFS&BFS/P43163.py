# 알파벳이 한개만 다른 단어를 word에서 찾아서 변환
# 변환과정을 거쳐서 target 단어로 바꾸면됨
# 다만 최단방법을 찾자 -> 최단이니까 bfs를 떠올려보기
from queue import Queue


def bfs(begin, target, words):
    visited = []
    que = Queue()
    que.put((begin, 0))
    visited.append(begin)

    while que.qsize() > 0:
        now = que.get()
        now_word = now[0]
        now_len = now[1]
        print(now)

        if now_word == target:
            return now_len

        for i in range(len(words)):
            word = words[i]

            if word == now_word or word in visited:
                continue

            else:
                diff = 0
                print({"word": word, "now": now_word, "now_len": len(now_word)})
                for j in range(len(word)):
                    if word[j] != now_word[j]:
                        diff += 1

                if diff == 1:
                    que.put((word, now_len+1))
                    visited.append(word)

    return 0


def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer


if __name__ == '__main__':
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    output = solution("hit", "cog", wordList)
    print(output)
