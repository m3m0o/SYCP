import socket
import struct


def translate_mac(mac: bytes) -> str:
    return ':'.join(f'{byte:02x}' for byte in mac)


def get_ethernet_frame(data: bytes) -> tuple:
    dest_mac, source_mac, frame_type = struct.unpack('!6s6sH', data[:14])

    return translate_mac(dest_mac), translate_mac(source_mac), frame_type, data[14:]


def get_ip(ip: bytes) -> str:
    return '.'.join(map(str, ip))


def get_ip_header(data: bytes) -> tuple:
    version_ihl, tos, lenght, identification, flags_offset, ttl, protocol, checksum, source_ip, dest_ip = struct.unpack('!BBHHHBBH4s4s', data[:20])

    version = version_ihl >> 4
    header_lenght = version_ihl & 15

    x_bit = (flags_offset >> 15) & 1 
    do_not_fragment = (flags_offset >> 14) & 1
    more_fragments_follow = (flags_offset >> 13) & 1

    offset = flags_offset & 8191

    return version, header_lenght, tos, lenght, identification, x_bit, do_not_fragment, more_fragments_follow, offset, ttl, protocol, checksum, get_ip(source_ip), get_ip(dest_ip)


with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3)) as s:
    s.bind(('wlp3s0', 0))

    while True:
        data, _source = s.recvfrom(65535)

        dest_mac, source_mac, frame_type, packet_data = get_ethernet_frame(data)
        version, header_lenght, tos, lenght, identification, x_bit, do_not_fragment, more_fragments_follow, offset, ttl, protocol, checksum, source_ip, dest_ip = get_ip_header(packet_data)

        print('Quadro Ethernet')
        print(f'\tMAC de origem: {source_mac}, MAC de destino: {dest_mac}')
        print(f'\n\tPacote IP')
        print(f'\t\tVersão: {version}, Comprimento do cabeçalho: {header_lenght}, TOS: {tos}, Comprimento total: {lenght}')
        print(f'\t\tID: {identification}, Flags: {x_bit} | {do_not_fragment} | {more_fragments_follow}, TTL: {ttl}, Offset: {offset}')
        print(f'\t\tProtocolo: {protocol}, Checksum: {checksum}, IP de Origem: {source_ip}, IP de destino: {dest_ip}\n\n')