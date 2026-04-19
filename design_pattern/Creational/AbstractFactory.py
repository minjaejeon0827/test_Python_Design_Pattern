# 추상 팩토리 패턴 (Abstract Factory Pattern)
# 추상 팩토리 패턴은 관련된 객체의 그룹을 생성하는 인터페이스를 제공하는 패턴으로, 
# 구체적인 클래스는 지정하지 않습니다.
# 참고: https://wikidocs.net/252293

# 파이썬 디자인패턴 소스파일 실행 터미널 명령어
# python Creational/AbstractFactory.py
# 참고: https://gemini.google.com/app/786ffe8164204817?hl=ko

# 소스코드 설명
# 참고: https://gemini.google.com/app/f3787d5da5081ba6?hl=ko

# abc 모듈은 "이 클래스는 직접 쓰지 말고, 규칙서(도면)로만 써라!"라고 정해주는 도구입니다.
from abc import ABC, abstractmethod

# ---------------------------------------------------------
# 1. 제품(Product)들의 '기본 도면' 만들기
# ---------------------------------------------------------

# 세상의 모든 '의자(Chair)'가 지켜야 할 기본 규칙서입니다.
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        # 의자라면 무조건 '앉기(sit_on)' 기능이 있어야 한다고 규칙을 정합니다.
        pass

# 빅토리아풍 의자: 의자 규칙서를 바탕으로 만든 진짜 제품입니다.
class VictorianChair(Chair):
    def sit_on(self):
        print("Sitting on a Victorian chair")  # "고풍스러운 의자에 앉습니다"

# 모던(현대식) 의자: 마찬가지로 의자 규칙서를 바탕으로 만들었습니다.
class ModernChair(Chair):
    def sit_on(self):
        print("Sitting on a Modern chair")  # "현대식 의자에 앉습니다"

# 세상의 모든 '소파(Sofa)'가 지켜야 할 기본 규칙서입니다.
class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        # 소파라면 무조건 '눕기(lie_on)' 기능이 있어야 합니다.
        pass

# 빅토리아풍 소파: 소파 규칙서를 따른 진짜 제품입니다.
class VictorianSofa(Sofa):
    def lie_on(self):
        print("Lying on a Victorian sofa")  # "고풍스러운 소파에 눕습니다"

# 모던(현대식) 소파: 소파 규칙서를 따른 진짜 제품입니다.
class ModernSofa(Sofa):
    def lie_on(self):
        print("Lying on a Modern sofa")  # "현대식 소파에 눕습니다"


# ---------------------------------------------------------
# 2. 팩토리(Factory, 가구 브랜드 공장)의 '기본 도면' 만들기
# ---------------------------------------------------------

# 모든 '가구 브랜드(Factory)'가 지켜야 할 기본 규칙서입니다.
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        # 가구 브랜드라면 무조건 의자를 만들 줄 알아야 합니다.
        pass

    @abstractmethod
    def create_sofa(self):
        # 가구 브랜드라면 무조건 소파도 만들 줄 알아야 합니다.
        pass


# ---------------------------------------------------------
# 3. 진짜 '세트 전문 공장(브랜드)' 만들기
# ---------------------------------------------------------

# '고풍스러운(Victorian) 가구만 전문으로 만드는 공장'입니다.
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        # 의자를 주문하면 무조건 '빅토리아풍 의자'를 줍니다.
        return VictorianChair()

    def create_sofa(self):
        # 소파를 주문하면 무조건 '빅토리아풍 소파'를 줍니다.
        return VictorianSofa()

# '현대식(Modern) 가구만 전문으로 만드는 공장'입니다.
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        # 의자를 주문하면 무조건 '현대식 의자'를 줍니다.
        return ModernChair()

    def create_sofa(self):
        # 소파를 주문하면 무조건 '현대식 소파'를 줍니다.
        return ModernSofa()


# ---------------------------------------------------------
# 4. 고객(Client)이 가구를 주문하고 사용하는 과정
# ---------------------------------------------------------

# 고객은 어떤 브랜드(factory)인지 신경 쓰지 않고, 그냥 "의자랑 소파 줘!"라고 주문만 합니다.
def client(factory: FurnitureFactory):
    # 입력받은 공장(브랜드)에서 의자를 뽑습니다.
    chair = factory.create_chair()
    # 입력받은 공장(브랜드)에서 소파를 뽑습니다.
    sofa = factory.create_sofa()
    
    # 뽑은 가구들을 사용해 봅니다.
    chair.sit_on()
    sofa.lie_on()


# 고객이 '빅토리아풍 가구 공장'에 주문을 넣습니다.
# 결과: 고풍스러운 의자에 앉고, 고풍스러운 소파에 눕게 됩니다. (스타일이 완벽히 일치!)
client(VictorianFurnitureFactory())  

# 고객이 '현대식 가구 공장'에 주문을 넣습니다.
# 결과: 현대식 의자에 앉고, 현대식 소파에 눕게 됩니다. (역시 스타일이 완벽히 일치!)
client(ModernFurnitureFactory())

# 💡 머리에 쏙 들어오는 핵심 요약
# 스타일(테마)의 통일: 추상 팩토리 패턴은 여러 가지 객체(의자, 소파)를 만들 때, 서로 어울리는 것들끼리 묶어서(빅토리아풍 세트, 현대식 세트) 만들어주는 공장을 세우는 방법이에요.

# 실수 방지: 만약 이 패턴을 쓰지 않고 프로그래머가 직접 chair = VictorianChair(), sofa = ModernSofa() 이렇게 섞어서 만들다 보면, 나중에 프로그램 안에서 테마가 꼬이는 실수가 생길 수 있어요.

# 고객(client)의 편리함: 코드를 사용하는 사람 입장에서는 "빅토리아 의자, 빅토리아 소파 주세요"라고 복잡하게 말할 필요 없이, "빅토리아 공장에 세트로 주문해 줘!"라고 한 번만 말하면 알아서 척척 세트가 나옵니다.

# 팩토리 메소드 패턴이 **'하나의 제품(장난감)'**을 누가 만들지 정하는 거였다면, 추상 팩토리 패턴은 **'여러 제품의 세트(가구 세트)'**를 통째로 책임지는 브랜드를 정하는 거라고 이해하시면 완벽합니다!