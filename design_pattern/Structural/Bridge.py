# 브리지 패턴 (Bridge Pattern)
# 브리지 패턴은 구현부에서 추상층을 분리하여 각각을 독립적으로 변형할 수 있게 하는 패턴입니다. 
# 이를 통해 기능 계층과 구현 계층을 분리하여 유연성을 높입니다.

# 참고: https://wikidocs.net/252293

# 파이썬 디자인패턴 소스파일 실행 터미널 명령어
# python Structural/Bridge.py
# 참고: https://gemini.google.com/app/786ffe8164204817?hl=ko

# 소스코드 설명
# 참고: https://gemini.google.com/app/f3787d5da5081ba6?hl=ko

# 이번에는 '브리지 패턴(Bridge Pattern)'이군요! 이름처럼 두 개의 섬을 부드럽게 이어주는 '다리(Bridge)' 역할을 하는 아주 똑똑한 패턴이에요.

# 이해하기 쉽게 우리가 매일 쓰는 '만능 리모컨'과 'TV'를 상상해 볼까요?

# 기능(추상층, Abstraction): 사용자가 누르는 '리모컨'입니다. (예: 전원 버튼, 볼륨 버튼)

# 구현(구현층, Implementation): 리모컨의 신호를 받아 실제로 켜지고 꺼지는 'TV'입니다. (예: 삼성 TV, LG TV)

# 만약 이 패턴을 쓰지 않고 '삼성 TV 리모컨', 'LG TV 리모컨'을 따로따로 만들면, 나중에 '스마트 리모컨'이라는 새로운 기능이 나왔을 때 '삼성 스마트 리모컨', 'LG 스마트 리모컨'을 또 각각 만들어야 해요. 제품이 늘어날수록 코드가 기하급수적으로 복잡해지죠.

# 하지만 브리지 패턴을 써서 리모컨(기능)과 TV(구현)를 분리하고 둘 사이를 '다리'로 연결해 주면, 리모컨은 리모컨대로 발전하고 TV는 TV대로 발전할 수 있답니다.

# 어떤 원리인지 주석을 통해 한 줄씩 살펴볼까요?

# 💡 머리에 쏙 들어오는 핵심 요약
# 기능과 실제 작동의 분리: 겉보기엔 하나의 덩어리 같지만, 사실 사용자가 만지는 부분(Abstraction)과 뒤에서 실제로 돌아가는 부분(Implementation)을 둘로 쪼개놓은 거예요.

# 유연한 조립(독립적 변형): 리모컨 안에 TV가 아예 내장되어 있는 게 아니라, 어떤 TV든 연결선(다리)만 꽂으면 작동하는 방식입니다. 덕분에 TV 브랜드가 100개로 늘어나도 리모컨 코드는 단 하나도 수정할 필요가 없어요.

# 언제 쓰나요? 기능(예: 리모컨, 스마트 리모컨)도 계속 종류가 늘어나고, 구현(예: TV, 에어컨, 로봇청소기)도 계속 종류가 늘어날 때, 이 둘을 하나하나 짝지어주기(조합하기) 너무 벅찰 때 다리를 놓아주면 아주 깔끔하게 해결됩니다!

# ---------------------------------------------------------
# 1. Implementation (구현층): 실제 작동을 담당하는 '기계(TV)'들의 기본 규칙
# ---------------------------------------------------------
class Implementation:
    def operation_impl(self):
        # "모든 기계는 작동(operation_impl)할 줄 알아야 한다"는 규칙입니다.
        pass

# 진짜 기계 A (예: 삼성 TV)
class ConcreteImplementationA(Implementation):
    def operation_impl(self):
        print("ConcreteImplementationA operation") # "삼성 TV가 켜집니다!"

# 진짜 기계 B (예: LG TV)
class ConcreteImplementationB(Implementation):
    def operation_impl(self):
        print("ConcreteImplementationB operation") # "LG TV가 켜집니다!"


# ---------------------------------------------------------
# 2. Abstraction (추상층): 사용자가 만지는 '만능 리모컨'
# ---------------------------------------------------------
class Abstraction:
    
    # 리모컨에 건전지를 넣을 때, '어떤 TV(기계)랑 연결할지' 설정해 줍니다.
    def __init__(self, implementation):
        # 리모컨 내부에 연결된 TV(implementation)를 기억해 둡니다. (이게 바로 '다리'입니다!)
        # 👇 바로 이 줄이 두 세계를 연결하는 '다리(Bridge)'입니다! 👇
        # 리모컨(Abstraction) 내부에 조종할 TV(implementation)를 연결해 두는 것이죠.
        self._implementation = implementation

    # 사용자가 리모컨의 '작동 버튼'을 누릅니다.
    def operation(self):
        # 리모컨이 직접 켜지는 게 아니라, 다리로 연결된 '진짜 기계'에게 작동하라고 신호를 보냅니다.
        # 놓여진 다리(self._implementation)를 타고 건너가서, 
        # 도착지에 있는 진짜 기계(TV)를 작동시킵니다.
        self._implementation.operation_impl()


# ---------------------------------------------------------
# 3. 실제 리모컨과 TV 연결해보기!
# ---------------------------------------------------------

# 1. 만능 리모컨(Abstraction)을 하나 사서, '기계 A(삼성 TV)'와 연결합니다.
abstraction_a = Abstraction(ConcreteImplementationA())
# 2. 리모컨의 작동 버튼을 누릅니다!
# 결과: 리모컨을 통해 기계 A가 작동합니다.
abstraction_a.operation()  

# 1. 이번에는 다른 방에 있는 '기계 B(LG TV)'와 만능 리모컨을 연결합니다.
abstraction_b = Abstraction(ConcreteImplementationB())
# 2. 리모컨의 작동 버튼을 누릅니다!
# 결과: 리모컨을 통해 기계 B가 작동합니다.
abstraction_b.operation()
