subject = ['국어', '영어', '수학', '사회', '과학']
print("성적을 입력하세요. (국어 영어 수학 사회 과학) : ")

# input()을 통해 각 과목의 성적을 받아온다.
# 성적은 공백을 기준으로 나눠서 리스트의 요소로 저장한다.
score = list(map(int, input().split()))

# 최고 점수와 최저 점수를 찾는다.
# max와 min을 이용하여 찾을 수 있다.
min_score = min(score)
max_score = max(score)

# 각 점수들의 인덱스를 찾는다.
min_index = score.index(min_score)
max_index = score.index(max_score)

# 각 과목명과 점수를 출력한다.
# 평균 점수에서 str()을 꼭 사용할 필요는 없지만 일관된 출력을 위해 적용했습니다!
print("최저 점수 : " + subject[min_index])
print("최고 점수 : " + subject[max_index])
print("평균 점수 : " + str(sum(score)/len(score)))