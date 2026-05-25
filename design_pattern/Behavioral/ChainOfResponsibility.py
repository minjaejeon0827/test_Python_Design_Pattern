# 책임 연쇄 패턴 (Chain of Responsibility Pattern)
# 책임 연쇄 패턴은 요청을 처리할 수 있는 객체들이 체인으로 연결되어, 
# 각 객체가 순서대로 요청을 처리하는 패턴입니다.

# 참고: https://wikidocs.net/252293

# 파이썬 디자인패턴 소스파일 실행 터미널 명령어
# python Behavioral/ChainOfResponsibility.py
# 참고: https://gemini.google.com/app/786ffe8164204817?hl=ko

# 소스코드 설명
# 참고: https://gemini.google.com/app/f3787d5da5081ba6?hl=ko

# 행위 패턴의 여정을 훌륭하게 이어가고 계시네요! 이번에 만나볼 패턴은 '책임 연쇄 패턴(Chain of Responsibility Pattern)'입니다.

# 이 패턴을 가장 쉽게 이해하려면 회사 고객센터의 '상담원 연결(ARS) 시스템'이나 결재 서류가 올라가는 '결재 라인'을 떠올려 보시면 됩니다.

# 고객이 전화를 걸면 먼저 '1차 상담원'이 받습니다. 자기가 아는 내용이면 바로 해결해 주지만, 모르는 내용이면 "해당 부서로 연결해 드리겠습니다" 하고 '2차 상담원'에게 넘깁니다. 2차 상담원도 모르면 '팀장'에게 넘기죠.

# 이처럼 "내가 해결할 수 있으면 내가 하고, 못하면 내 다음 사람에게 책임을 떠넘기는(사슬처럼 연결된) 구조"가 바로 책임 연쇄 패턴입니다!

# 고객센터의 비유를 머릿속에 그리며 주석을 한 줄씩 천천히 살펴볼까요?

# 💡 머리에 쏙 들어오는 핵심 요약
# 요청을 보내는 쪽의 편리함: 고객은 이 회사에 A 상담원이 있는지, B 상담원이 있는지 복잡한 구조를 알 필요가 없습니다. 그냥 무조건 대표번호(handler_a)에 전화해서 원하는 걸 말하기만 하면, 알아서 담당자를 찾아갑니다.

# 유연한 연결 고리: 프로그램 실행 중에도 언제든지 상담원의 순서를 바꾸거나 새로운 C 상담원을 추가(handler_b.set_next(handler_c))하기가 너무 쉽습니다. 코드를 뜯어고칠 필요 없이 블록 장난감처럼 끼웠다 뺐다 할 수 있죠.

# 어디에 많이 쓰이나요? 웹 프로그래밍에서 사용자가 로그인했는지 확인하고, 권한이 있는지 확인하고, 데이터를 안전하게 걸러내는 등의 '필터링 과정(Middleware)'을 만들 때 아주 강력하게 쓰이는 패턴입니다!

# abc 모듈은 "이 클래스는 뼈대 역할만 하니까, 상속받아서 써라!"라고 정해주는 도구입니다.
from abc import ABC, abstractmethod

# ---------------------------------------------------------
# 1. Handler (처리자): 모든 상담원이 지켜야 할 '기본 규칙'
# ---------------------------------------------------------
class Handler(ABC):
    # 상담원이 처음 자리에 앉을 때(생성될 때) 하는 일입니다.
    def __init__(self):
        # "내가 해결 못 하면 다음번엔 누구한테 넘기지?" 다음 담당자(next_handler)를 일단 비워둡니다.
        self._next_handler = None

    # set_next: 다음 담당자가 누구인지 지정해주는(연결해주는) 기능입니다.
    def set_next(self, handler):
        # 내 다음 사람으로 지정받은 사람(handler)을 기억해 둡니다.
        self._next_handler = handler
        # 이렇게 돌려주면(return) A.set_next(B).set_next(C) 처럼 기차처럼 길게 연결할 수 있어요.
        return handler

    # 고객의 '요청(request)'이 들어왔을 때 기본적으로 어떻게 대처할지 정합니다.
    @abstractmethod
    def handle(self, request):
        # 만약 내 뒤에 연결된 '다음 담당자'가 있다면?
        if self._next_handler:
            # "난 모르겠으니, 다음 담당자님 부탁해요!" 하고 떠넘깁니다(return).
            return self._next_handler.handle(request)
        
        # 내 뒤에 아무도 없는데 나도 해결을 못했다면? "처리 불가(None)"라고 알려줍니다.
        return None


# ---------------------------------------------------------
# 2. ConcreteHandler A, B (진짜 상담원들)
# ---------------------------------------------------------

# A 상담원 (예: 환불 담당 부서)
class ConcreteHandlerA(Handler):
    def handle(self, request):
        # 만약 고객의 요청이 "A(예: 환불)"라면?
        if request == "A":
            # "아, 그건 제 전문이죠! A 상담원이 처리했습니다." 하고 결과를 돌려줍니다.
            return f"Handler A handled {request}"
        # 내 담당이 아니라면? (else)
        else:
            # 부모(super) 클래스인 Handler의 규칙대로, '다음 담당자'에게 떠넘깁니다.
            return super().handle(request)

# B 상담원 (예: 기술 지원 부서)
class ConcreteHandlerB(Handler):
    def handle(self, request):
        # 만약 고객의 요청이 "B(예: 기술 지원)"라면?
        if request == "B":
            # "제가 해결해 드리겠습니다! B 상담원이 처리했습니다."
            return f"Handler B handled {request}"
        # 내 담당이 아니라면? (else)
        else:
            # 역시 부모 규칙에 따라 '다음 담당자'에게 토스합니다.
            return super().handle(request)


# ---------------------------------------------------------
# 3. 실제 고객센터 연결하고 운영해보기!
# ---------------------------------------------------------

# 1. A 상담원과 B 상담원을 출근시킵니다.
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()

# 2. A 상담원에게 "당신이 못하는 건 B 상담원에게 넘기세요!"라고 사슬(Chain)을 연결해 줍니다.
handler_a.set_next(handler_b)


# 3. 고객이 대표번호(A 상담원)로 "A(환불)" 요청을 보냅니다.
# 결과: A 상담원이 자기 담당이므로 바로 척척 처리합니다.
print(handler_a.handle("A"))  # Handler A handled A

# 4. 고객이 대표번호(A 상담원)로 "B(기술 지원)" 요청을 보냅니다.
# 결과: A 상담원은 못 하니 B 상담원에게 토스하고, 전달받은 B 상담원이 무사히 처리합니다!
print(handler_a.handle("B"))  # Handler B handled B

# 5. 고객이 대표번호(A 상담원)로 "C(CEO 면담)" 요청을 보냅니다.
# 결과: A도 못하고, 토스받은 B도 못하고, B 뒤에는 아무도 없어서 결국 처리 실패(None)가 됩니다.
print(handler_a.handle("C"))  # None