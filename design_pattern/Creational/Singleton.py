# 싱글톤 패턴 (Singleton Pattern)
# 싱글톤 패턴은 클래스의 인스턴스를 하나만 생성하고, 
# 그 인스턴스를 어디서든지 참조할 수 있도록 보장하는 패턴입니다.
# 참고: https://wikidocs.net/252293

# 파이썬 디자인패턴 소스파일 실행 터미널 명령어
# python Creational/Singleton.py
# 참고: https://gemini.google.com/app/786ffe8164204817?hl=ko

# 소스코드 설명
# 참고: https://gemini.google.com/app/f3787d5da5081ba6?hl=ko
class Singleton:
    # _instance는 '진짜 객체'가 들어갈 빈 자리에요.
    # 처음에는 아무것도 없으니 None(비어 있음) 상태로 시작합니다.
    _instance = None

    # __new__는 파이썬에서 객체가 실제로 만들어질 때 가장 먼저 호출되는 '입구' 같은 함수예요.
    def __new__(cls, *args, **kwargs):
        # 만약 _instance가 None이라면? (즉, 아직 객체가 한 번도 안 만들어졌다면?)
        if cls._instance is None:
            # super().__new__(cls)를 통해 진짜 객체를 딱 하나 생성해서 _instance에 보관합니다.
            cls._instance = super().__new__(cls, *args, **kwargs)
        
        # 이미 객체가 있다면 새로 만들지 않고, 보관 중인 _instance를 그대로 돌려줍니다.
        return cls._instance

# 1. 첫 번째로 Singleton 객체를 만들어봅니다. (새로 생성됨)
singleton1 = Singleton()

# 2. 두 번째로 Singleton 객체를 만들어봅니다. (이미 있으니 기존 것을 돌려받음)
singleton2 = Singleton()

# 두 변수가 가리키는 객체가 '정말로 같은 것'인지 확인해볼까요?
print(singleton1 is singleton2)  # 결과는 당연히 True! (둘은 완전히 같은 하나입니다.)