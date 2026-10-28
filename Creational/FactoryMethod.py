# 팩토리 메소드 패턴 (Factory Method Pattern)
# 팩토리 메소드 패턴은 객체 생성을 서브클래스(ConcreteCreatorA, ConcreteCreatorB)에 위임하여, 
# 객체 생성의 구현을 분리하는 패턴입니다.
# 참고: https://wikidocs.net/252293

# 파이썬 디자인패턴 소스파일 실행 터미널 명령어
# python Creational/FactoryMethod.py
# 참고: https://gemini.google.com/app/786ffe8164204817?hl=ko

# 소스코드 설명
# 참고: https://gemini.google.com/app/f3787d5da5081ba6?hl=ko

# abc 모듈은 '추상 클래스(Abstract Base Class)'를 만들기 위해 필요해요.
# 추상 클래스는 "이 클래스는 뼈대 역할만 하니까, 직접 사용하지 말고 상속받아서 쓰세요!"라고 정해두는 거예요.
from abc import ABC, abstractmethod

# ---------------------------------------------------------
# 1. 제품(Product) 부분: 무엇을 만들 것인가?
# ---------------------------------------------------------

# Product는 모든 제품이 공통으로 가져야 할 '기본 틀'이에요. (예: 모든 장난감의 기본 틀)
class Product(ABC):
    # @abstractmethod는 "이 제품을 상속받는 진짜 제품들은 무조건 use() 기능을 직접 만들어야 해!"라는 규칙입니다.
    @abstractmethod
    def use(self):
        pass

# ConcreteProductA는 Product의 틀을 바탕으로 만든 '진짜 제품 A'예요. (예: 로봇 장난감)
class ConcreteProductA(Product):
    def use(self):
        # 제품 A만의 작동 방식을 적어줍니다.
        print("Using Product A")

# ConcreteProductB도 Product의 틀을 바탕으로 만든 '진짜 제품 B'예요. (예: 곰 인형)
class ConcreteProductB(Product):
    def use(self):
        # 제품 B만의 작동 방식을 적어줍니다.
        print("Using Product B")


# ---------------------------------------------------------
# 2. 공장(Creator) 부분: 누가 어떻게 만들 것인가?
# ---------------------------------------------------------

# Creator는 제품을 생산하고 작동시키는 '기본 공장 틀'이에요.
class Creator(ABC):
    
    # 공장에서 제품을 만들어내는 핵심 스위치(메소드)예요. 
    # 하지만 기본 공장에서는 "무엇을 만들지" 결정하지 않고 비워둡니다. (하위 공장들이 결정할 거예요!)
    @abstractmethod
    def factory_method(self):
        pass

    # 제품을 생성하고 직접 사용해 보는 전체 과정이에요.
    def create_product(self):
        # 1. factory_method()를 눌러서 제품을 하나 뽑아냅니다. (이때 어떤 제품이 나올지는 하위 공장이 결정해요)
        product = self.factory_method()
        # 2. 뽑아낸 제품의 use() 기능을 실행합니다.
        product.use()


# ConcreteCreatorA는 Creator 틀을 바탕으로 만든 'A 전담 공장'이에요.
class ConcreteCreatorA(Creator):
    # 비어있던 factory_method()를 채워서, "나는 A 제품을 만들 거야!"라고 선언합니다.
    def factory_method(self):
        return ConcreteProductA()

# ConcreteCreatorB는 Creator 틀을 바탕으로 만든 'B 전담 공장'이에요.
class ConcreteCreatorB(Creator):
    # 비어있던 factory_method()를 채워서, "나는 B 제품을 만들 거야!"라고 선언합니다.
    def factory_method(self):
        return ConcreteProductB()


# ---------------------------------------------------------
# 3. 실제 실행해보기!
# ---------------------------------------------------------

# 1. A 전담 공장을 하나 세웁니다.
creator_a = ConcreteCreatorA()
# 2. A 공장에게 "제품 만들어서 작동시켜봐!"라고 명령합니다.
# 내부적으로 factory_method()가 A 제품을 만들고, 그 A 제품의 use()가 실행됩니다.
creator_a.create_product()  # 결과: Using Product A

# 1. B 전담 공장도 하나 세웁니다.
creator_b = ConcreteCreatorB()
# 2. B 공장에게도 "제품 만들어서 작동시켜봐!"라고 명령합니다.
creator_b.create_product()  # 결과: Using Product B

# 💡 핵심 요약
# 객체 생성의 분리: 부모 공장(Creator)은 "제품을 뽑아서 실행한다"는 과정만 관리합니다.

# 서브클래스에 위임: 진짜로 "어떤 제품(Product A or Product B)"을 뽑을지는 자식 공장(ConcreteCreator A, B)들이 결정합니다.

# 코드를 보시면서 장난감 공장의 원리를 천천히 음미해 보세요! 복잡해 보이던 설계 방식도 역할 분담의 관점에서 보면 훨씬 논리적이고 깔끔하게 다가올 거예요.