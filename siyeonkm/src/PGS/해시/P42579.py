# 장르별로 2개씩, 장르에 노래 1개면 1개만
# 장르>재생수>고유번호 순으로 출력

def findGenre(genres, plays):
    genre = {}
    for i in range(len(genres)):
        if genres[i] not in genre:
            genre[genres[i]] = plays[i]
        else:
            genre[genres[i]] += plays[i]
    return sorted(genre, key=lambda x: genre[x], reverse=True)


def findSong(genre, genres, plays):
    song = {}
    for i in range(len(genres)):
        if genres[i] == genre:
            song[i] = plays[i]

    list = sorted(song, key=lambda x: song[x], reverse=True)

    if len(list) > 2:
        return list[:2]
    else:
        return list


def solution(genres, plays):
    answer = []
    genreRank = findGenre(genres, plays)

    for genre in genreRank:
        songRank = findSong(genre, genres, plays)
        answer.extend(songRank)

    return answer