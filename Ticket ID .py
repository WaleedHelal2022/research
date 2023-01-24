import random
chars = "1234567890"

while 1:
    Ticket_len = int(10)
    Ticket_count = int(1)
    for x in range(0, Ticket_count):
        TicketId = ""
        for x in range(0, Ticket_len):
            Ticket_char = random.choice(chars)
            TicketId = TicketId + Ticket_char
        print("Here is your TicketId : ", TicketId)

    quit()
