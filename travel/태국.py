class 태국패키지:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행(야시장 투어) 50만원")

if __name__ == "__main__": #name이 main이라면
    print("태국 모듈을 직접 실행")
    print("이 문장을 모듈을 직접 실행할 때만 실행돼요")
    trip_to = 태국패키지()
    trip_to.detail()
else:
    print("태국 외부에서 모듈 호출")
