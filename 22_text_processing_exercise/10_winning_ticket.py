def check_ticket(ticket):
    if len(ticket) != 20:
        return f"invalid ticket"

    symbols = ["$", "@", "#", "^"]
    left_part = ticket[:10]
    right_part = ticket[10:]

    for symbol in symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbols_repetition = symbol * uninterrupted_match_length
            if winning_symbols_repetition in left_part and winning_symbols_repetition in right_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]

for ticket in tickets:
    print(check_ticket(ticket))
