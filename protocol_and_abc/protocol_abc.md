## protocol vs abc(abstarct base class)


## Duck typing
* 만약 그것이 오리처럼 꽥꽥거리고 걷는다면 ,그것을 오리처럼 다루어라 (python 과 go 가 대표적)
  

## ABC 
* 클래스로 제한하여 해당 유형 또는 하위 유형만 허용
* 상속을 이용하여 
*  인터페이스를 제한하고 수행 작업에 필요한 인터페이스를 정의하는것
*  ABC를 상속한 클래스는 하위 클래스에 속하므로 , 프로그램 다른 위치에서 사용하는 클래스 계층의 일부 (수직적)
```python
class Parent(ABC)
```

## Protocol
* Protocol을 이용하면 서로 다른 라이브러리를 함께 연결하고   커플링을 줄일 수 있음
* Duck typing
* 인터페이스를 제한하고 수행 작업에 필요한 인터페이스를 정의하는것
* ABC와 다른것은 좀 더 사용하는곳에 ..속함(?)
* 여러번 정의 가능
* 단점도 있지 : super method 사용 못함


## ABC vs Protocol
* ABC는 인터페이스를 상속을 이용해서 해당 메소드를 구현 
* Protocl은