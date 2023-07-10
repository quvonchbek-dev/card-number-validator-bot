import asyncio


async def format_number(card_num):
    res = ""
    for i in range(len(card_num)):
        res += card_num[i]
        if i % 4 == 3 and i and i != len(card_num) - 1:
            res += "-"
    return res


async def validate_credit_card(card_number: str) -> bool:
    if len(str) != 16:
        return False
    card_number = [int(num) for num in card_number]
    check_igit = card_number.pop(-1)
    card_number.reverse()
    card_number = [num * 2 if idx % 2 == 0
                   else num for idx, num in enumerate(card_number)]

    card_number = [num - 9 if idx % 2 == 0 and num > 9
                   else num for idx, num in enumerate(card_number)]
    card_number.append(check_igit)
    return sum(card_number) % 10 == 0


async def main():
    print(await format_number("1234567890123456"))


if __name__ == "__main__":
    asyncio.run(main())
