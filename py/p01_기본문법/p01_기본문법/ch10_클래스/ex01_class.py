# 크래스 정의
class Character:
    # 생성자 (Constructor): 객체가 만들어질 때 처음 자동으로 실행되는 특별한 함수
    # __init__ 메소드는 Python 클래스의 생성자(constructor)로, 객체가 생성될 때 자동으로 호출되어 초기화 작업을 수행합니다. 
    # 이를 통해 클래스 인스턴스의 속성을 설정하거나 초기값을 지정할 수 있습니다.
    def __init__(self, name, hp):
        self.name = name  # 인스턴스 변수 (속성, Attribute)
        self.hp = hp      # 인스턴스 변수

    # 메서드 (Method): 클래스 내부에 정의된 함수 (기능)
    def take_damage(self, damage):
        self.hp -= damage
        print(f"[{self.name}]이(가) {damage}의 피해를 입었습니다! (남은 HP: {self.hp})")


# 1. 서로 다른 데이터(이름, 체력)를 가진 객체 2개 생성
warrior = Character("전사", 100)
wizard = Character("마법사", 60)

# 2. 각 객체의 속성(데이터) 접근
print(warrior.name)  # 출력: 전사
print(wizard.hp)     # 출력: 60

# 3. 각 객체의 메서드(기능) 실행
warrior.take_damage(20)  # 출력: [전사]이(가) 20의 피해를 입었습니다! (남은 HP: 80)
wizard.take_damage(15)   # 출력: [마법사]이(가) 15의 피해를 입었습니다! (남은 HP: 45)



class Person:
    def __init__(self, name, age):
        self.name = name # 인스턴스 변수 초기화
        self.age = age

def introduce(self):
    print(f"안녕하세요! 제 이름은 {self.name}이고, 나이는 {self.age}살입니다.")

# 객체 생성 및 초기화
    person1 = Person("Alice", 25)
    person1.introduce() # 출력: 안녕하세요! 제 이름은 Alice이고, 나이는 25살입니다