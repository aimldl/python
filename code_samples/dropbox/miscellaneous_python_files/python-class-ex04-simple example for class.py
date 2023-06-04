# 점프 투 파이썬, 박응용, 이지스 퍼블리싱
#   05-1. 파이썬 프로그래밍의 핵심, 클래스
#     이야기 형식으로 클래스 기초 쌓기
#       pp.177-179

class Service:
	# 클래스 변수
	secret = "오늘 영화 보헤미안 랩소디를 보러간다."
	# 클래스 함수
	def sum( self, a, b ):
		result = a + b
		print( "%s + %s = %s" % (a,b,result))

pey = Service()
print( pey.secret )
pey.sum(1, 1)