#!/usr/bin/env python3

class Message:
    pass

class State:
    pass

class StateMachine:
    def __init__(self):
        self.states = []

    def recieve_message(self, message):
        raise NotImplementedError

class Protocol:
    pass
