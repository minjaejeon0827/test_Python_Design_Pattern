# 중재자 패턴 (Mediator Pattern)
# 중재자 패턴은 객체 간의 상호작용을 캡슐화하여 객체들이 직접 통신하지 않고, 
# 중재자를 통해 통신하도록 하는 패턴입니다.

# 참고: https://wikidocs.net/252293

# 파이썬 디자인패턴 소스파일 실행 터미널 명령어
# python Behavioral/Mediator.py
# 참고: https://gemini.google.com/app/786ffe8164204817?hl=ko

# 소스코드 설명
# 참고: https://gemini.google.com/app/f3787d5da5081ba6?hl=ko

# 행위 패턴의 여정을 훌륭하게 이어가고 계시네요! 이번에 만나볼 패턴은 '중재자 패턴(Mediator Pattern)'입니다.

# 이 패턴을 가장 쉽게 이해하려면 공항의 '비행기 관제탑(Control Tower)'을 상상해 보시면 됩니다.

# 하늘에 수십 대의 비행기가 떠 있다고 생각해 보세요. 만약 비행기들끼리 서로 "제가 먼저 착륙할게요!", "아닙니다, 제가 먼저 갈게요!" 하고 직접 무전을 주고받는다면 엄청나게 복잡하고 사고가 날 위험도 크겠죠? (이를 프로그램에서는 코드가 스파게티처럼 꼬인다고 표현합니다.)

# 그래서 비행기들은 서로 대화하지 않습니다. 오직 중앙의 '관제탑(Mediator)'하고만 대화하죠. 비행기가 관제탑에 "저 착륙합니다!"라고 알리면, 관제탑이 알아서 다른 비행기들에게 "잠시 대기하세요!"라고 교통정리를 해주는 방식입니다.

# 즉, 객체들이 서로 얽히고설켜서 직접 소통하는 대신, 중간에 '반장(중재자)'을 딱 한 명 세워두고 모든 소통을 반장을 통해서만 하도록 만드는 똑똑한 설계법이랍니다.

# 관제탑과 비행기의 비유를 생각하며 주석을 한 줄씩 천천히 살펴볼까요?

# 💡 머리에 쏙 들어오는 핵심 요약
# 스파게티 코드 방지: 만약 중재자가 없었다면, 비행기 1 코드 안에 component2.do_c()가 직접 들어가야 하고, 비행기들이 서로서로 얽히게 됩니다. 중재자 패턴은 "너희들끼리 직접 연락하지 마! 나(관제탑)한테만 말해!"라고 규칙을 정해서 코드가 꼬이는 것을 완벽하게 막아줍니다.

# 비행기는 자기 할 일만: 비행기(컴포넌트) 입장에서는 다른 비행기가 뭘 하든 관심이 없습니다. 그저 자기 할 일을 하고 관제탑에 "나 끝났어!"라고 무전만 치면 되니까 역할이 아주 단순하고 명확해집니다.

# 어디에 많이 쓰이나요? 카카오톡 같은 '채팅방 서버(사용자끼리 직접 연결되지 않고 서버를 거침)', 여러 버튼과 체크박스가 서로 영향을 주고받는 '복잡한 사용자 화면(GUI)', 혹은 공항의 실제 관제 시스템 등에 아주 유용하게 쓰인답니다!

# abc 모듈은 "이 클래스는 뼈대 역할만 하니 상속받아 써라!"라고 정해주는 도구입니다.
from abc import ABC, abstractmethod

# ---------------------------------------------------------
# 1. Mediator (중재자): '관제탑'이 지켜야 할 기본 규칙
# ---------------------------------------------------------
class Mediator(ABC):
    # 관제탑은 무조건 비행기들로부터 '무전(notify)을 받는 기능'이 있어야 합니다.
    @abstractmethod
    def notify(self, sender, event):
        pass

# ---------------------------------------------------------
# 2. ConcreteMediator (구체적 중재자): '진짜 관제탑(예: 인천공항 관제탑)'
# ---------------------------------------------------------
class ConcreteMediator(Mediator):
    # 관제탑이 처음 세워질 때, 자기가 관리할 비행기 1과 비행기 2를 등록합니다.
    def __init__(self, component1, component2):
        self.component1 = component1
        # 비행기 1의 무전기에 '이 관제탑'을 주파수로 맞춰줍니다.
        self.component1.set_mediator(self)
        
        self.component2 = component2
        # 비행기 2의 무전기에도 '이 관제탑'을 주파수로 맞춰줍니다.
        self.component2.set_mediator(self)

    # 비행기로부터 무전(notify)이 들어왔을 때, 관제탑이 교통정리를 하는 곳입니다.
    def notify(self, sender, event):
        # 만약 "A"라는 무전(이벤트)이 들어왔다면?
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            # 관제탑이 알아서 비행기 2에게 "C 행동을 해라!"라고 지시합니다.
            self.component2.do_c()
            
        # 만약 "D"라는 무전(이벤트)이 들어왔다면?
        if event == "D":
            print("Mediator reacts on D and triggers following operations:")
            # 관제탑이 알아서 비행기 1에게 "B 행동을 해라!"라고 지시합니다.
            self.component1.do_b()


# ---------------------------------------------------------
# 3. BaseComponent: 모든 '비행기'가 공통으로 가질 '무전기' 부품
# ---------------------------------------------------------
class BaseComponent:
    def __init__(self):
        # 처음 비행기가 만들어질 때는 아직 연결된 관제탑이 없습니다.
        self.mediator = None

    def set_mediator(self, mediator):
        # 비행기 무전기에 담당 관제탑(mediator)을 연결해 주는 스위치입니다.
        self.mediator = mediator


# ---------------------------------------------------------
# 4. Component 1, 2 (구체적 컴포넌트): '진짜 비행기들'
# ---------------------------------------------------------

# 첫 번째 비행기 (예: 대한항공)
class Component1(BaseComponent):
    def do_a(self):
        # 1. 비행기 1이 자기가 할 일(A)을 합니다.
        print("Component 1 does A.")
        # 2. 자기 할 일을 마치고, 상대방에게 직접 말하지 않고 **관제탑**에 "나 A 했어!"라고 무전을 칩니다.
        self.mediator.notify(self, "A")

    def do_b(self):
        print("Component 1 does B.")

# 두 번째 비행기 (예: 아시아나항공)
class Component2(BaseComponent):
    def do_c(self):
        print("Component 2 does C.")

    def do_d(self):
        # 1. 비행기 2가 자기가 할 일(D)을 합니다.
        print("Component 2 does D.")
        # 2. 자기 할 일을 마치고, 역시 **관제탑**에 "나 D 했어!"라고 무전을 칩니다.
        self.mediator.notify(self, "D")


# ---------------------------------------------------------
# 5. 실제 관제탑과 비행기들의 통신 시작!
# ---------------------------------------------------------

# 1. 비행기 1과 비행기 2를 띄웁니다.
component1 = Component1()
component2 = Component2()

# 2. 이 두 비행기를 묶어서 관리할 '인천공항 관제탑'을 세웁니다.
mediator = ConcreteMediator(component1, component2)

# 3. 비행기 1이 자발적으로 "A 작동"을 시작합니다.
# 결과: 비행기 1이 작동 -> 관제탑에 무전 보냄 -> 관제탑이 비행기 2에게 "C 작동" 지시함!
component1.do_a()

print("-" * 30)  # 보기 편하게 구분선을 그어드릴게요!

# 4. 이번엔 비행기 2가 자발적으로 "D 작동"을 시작합니다.
# 결과: 비행기 2가 작동 -> 관제탑에 무전 보냄 -> 관제탑이 비행기 1에게 "B 작동" 지시함!
component2.do_d()