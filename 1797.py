"""
1797. Design Authentication Manager

There is an authentication system that works with authentication tokens. For 
each session, the user will receive a new authentication token that will 
expire timeToLive seconds after the currentTime. If the token is renewed, 
the expiry time will be extended to expire timeToLive seconds after the 
(potentially different) currentTime.

Implement the AuthenticationManager class:

- AuthenticationManager(int timeToLive) constructs the AuthenticationManager 
  and sets the timeToLive.
- generate(string tokenId, int currentTime) generates a new token with the given 
  tokenId at the given currentTime in seconds.
- renew(string tokenId, int currentTime) renews the unexpired token with the 
  given tokenId at the given currentTime in seconds. If there are no unexpired 
  tokens with the given tokenId, the request is ignored, and nothing happens.
- countUnexpiredTokens(int currentTime) returns the number of unexpired tokens 
  at the given currentTime.

Note that if a token expires at time t, and another action happens on 
time t (renew or countUnexpiredTokens), the expiration takes place before 
the other actions.
"""

from typing import Dict, Optional


class Node:
    def __init__(self, token_id: str):
        self.token_id = token_id
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class AuthenticationManager:
    # TODO
    def __init__(self, timeToLive: int):
        pass

    def generate(self, token_id: str, currentTime: int) -> None:
        pass

    def renew(self, token_id: str, currentTime: int) -> None:
        pass

    def countUnexpiredTokens(self, currentTime: int) -> int:
        pass

    def add_node(self, node: Node) -> None:
        pass

    def expire(self, currentTime: int) -> int:
        pass
