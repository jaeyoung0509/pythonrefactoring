from typing import Any, Awaitable
from iot.devices import HueLightDevice, SmartSpeakerDevice, SmartToiletDevice
from iot.message import Message, MessageType
from iot.service import IOTService
import asyncio


async def run_sequence(*functions : Awaitable[Any]) -> None:
    (await function for function in functions)

async def run_parallel(*functions : Awaitable[Any]) -> None:
    await  asyncio.gather(*functions)


async def main() -> None:
    # create a IOT service
    service = IOTService()

    # create and register a few devices
    hue_light = HueLightDevice()
    speaker = SmartSpeakerDevice()
    toilet = SmartToiletDevice()
    # 병렬로 처리하기 asyncio.gater
    hue_light_id , speaker_id , toilet_id = await asyncio.gather(
        service.register_device(hue_light) ,
        service.register_device(speaker) ,
         service.register_device(toilet)
    )
    # create a few programs
    wake_up_program = [
        Message(hue_light_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.PLAY_SONG, "Miles Davis - Kind of Blue"),
    ]

    sleep_program = [
        Message(hue_light_id, MessageType.SWITCH_OFF),
        Message(speaker_id, MessageType.SWITCH_OFF),
        Message(toilet_id, MessageType.FLUSH),
        Message(toilet_id, MessageType.CLEAN),
    ]

    # run the programs
    await service.run_program(wake_up_program)
    await service.run_program(sleep_program)


if __name__ == "__main__":
    asyncio.run(main())