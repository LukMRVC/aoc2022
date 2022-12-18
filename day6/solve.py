
content = input()

PACKET_MARKER_LEN = 4
MESSAGE_MARKER_LEN = 14


i = 0
while i < len(content) - PACKET_MARKER_LEN:
    window = content[i:i+PACKET_MARKER_LEN]
    if len(set(window)) == PACKET_MARKER_LEN:
        break
    i += 1

print(i + PACKET_MARKER_LEN)

i = 0
while i < len(content) - MESSAGE_MARKER_LEN:
    window = content[i:i + MESSAGE_MARKER_LEN]
    if len(set(window)) == MESSAGE_MARKER_LEN:
        break
    i += 1

print(i + MESSAGE_MARKER_LEN)
