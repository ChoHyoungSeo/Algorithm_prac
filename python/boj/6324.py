n = int(input())

for i in range(1, n + 1):
    # URL을 입력받습니다.
    url = input()
    
    # "://"를 기준으로 프로토콜과 나머지 부분을 분리합니다.
    # maxsplit=1을 사용하여 첫 번째 "://"만을 대상으로 분리합니다.
    protocol, rest = url.split("://", 1)
    
    # 나머지 부분에서 호스트, 포트, 경로를 추출합니다.
    if "/" in rest:
        host_port, path = rest.split("/", 1)
    else:
        host_port = rest
        path = "<default>"
    
    if ":" in host_port:
        host, port = host_port.split(":")
    else:
        host = host_port
        port = "<default>"
    
    print(f"URL #{i}")
    print(f"Protocol = {protocol}")
    print(f"Host     = {host}")
    print(f"Port     = {port}")
    print(f"Path     = {path}")
    print()
