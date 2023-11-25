## Backend software engineer test : implementation of RUDP

The test consists of implementing a reliable communication stream protocol based on UDP (User Datagram Protocol). You are free to implement a protocol standard like [Reliable User Datagram Protocol](https://en.wikipedia.org/wiki/Reliable_User_Datagram_Protocol). However, for simplicity purposes the only requirements for this test is the reliability and flow control aspects. i.e: you don't have to follow the standard exactly. And since the time is limited, you should only focus on the correctness rather than performance.

For the programming language and framework used, it is preferable to work with one of the following:
- C/C++ (Any networking library)
- Python (sockets/asyncio)
- Golang (built-in net package)
- Rust (built-in net package/Tokio)

Other than the above requirements, feel free to test the protocol in any way you want (Server/Client, Peer-to-Peer ...etc)


## Resources
You can find some useful resources at:

- [UDP RFC 768](https://www.ietf.org/rfc/rfc768.txt)
- [Reliable UDP protocol draft](https://datatracker.ietf.org/doc/html/draft-ietf-sigtran-reliable-udp-00/)
