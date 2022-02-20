## reference
> * https://www.youtube.com/watch?v=l9lX_YOLwW0
## asyncio 모듈
> * 비동기 프로그램을 위한 모듈 
> * 코루틴과 이벤트루프 방식으로 비동기 처리
> * async : 
    비동기 함수를 생성하는 키워드이다. 기존의 함수 선언 키워드인 def 앞에 async 키워드를 붙여서 비동기 함수를 생성한다.
      async 키워드를 통해서 생성된 비동기 함수를 coroutine이라고 한다
> * await:
> 비동기 함수를 호출하는 키워드이다. 비동기 함수, coroutine을 일반 함수와 같이 호출하는 경우 coroutine 객체를 반환한다.
await 키워드를 통해서 호출해야지 비동기 함수를 실행시킬 수 있다

## 코루틴 함수
> * 일시 중지나 재시작을 할 수 있는 비동기 함수
> * 호출하면 실제 객체가 실행되는것이 아니라 코루틴 객체가 반환 , 이 객체가 이벤트 루프로 전달되어 실행


## 이벤트 루프
> * 코루틴을 실행하고 입출력을 처리하는 실행 장치(프로그램)
> * 이벤트 루프에 코루틴을 등록하면 어떤 코루틴을 실행 도중 입출력은 잠시 중단 , 다른 코루틴이 먼저 실행 
> * 이벤트 루프에 코루틴을 등록하는 과정 , corutine을 위한 Task를 생성하고 루프 시작 , corutine이 종료되면 loop도 종료
```python
loop = asyncio.get_event_loop()
loop.run_until_complete(corutine)
loop.close()    
``` 

## task
> * 테스크를 만들어 실행하면 멀티 테스크 동시 실행 간으
```python
import asyncio
async def say(what :str  ,delay : int):
    await asyncio.sleep(delay)
    print(what)

loop = asycio_get_event_loop()
task1 = loop.create_task(say("first say" , 2))
task2 = loop.create_task(say("second say" , 2))
loop.run_until_complete(task1)
loop.run_until_complete(task2)
loop.close()
```

## asyncio.gater()
> *  여러 함수를 동시에 호출할 때 사용