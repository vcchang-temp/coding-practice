# Logger Rate Limiter
# Design a logger system that receive stream of messages 
# along with its timestamps, each message should be printed 
# if and only if it has not printed in the last 10 seconds.

# Given a message and a timestamp (in seconds granularity), 
# return true if the message should be printed in the given 
# timestamp, otherwise returns false.

# .shouldPrint() analysis
# Time: O(1)  -> lookup in dictionary and calculation are constant 
#                time operations 
# Space: O(1) -> output stays constant regardless of input size

class Logger:
    def __init__(self):
        self.msg_timestamp = dict()

    def log(self, msg: str, currTime: int):
        self.msg_timestamp[msg] = currTime

    def shouldPrint(self, msg: str, timestamp: int):
        return msg in self.msg_timestamp and self.msg_timestamp[msg] + 10 <= timestamp

if __name__ == "__main__":
    logger = Logger()

    logger.log("hi", 1)
    assert logger.shouldPrint("hi", 11) ==  True

    logger.log("hello", 2)
    assert logger.shouldPrint("hello", 10) ==  False

    logger.log("anyeong", 3)
    assert logger.shouldPrint("anyeong", 100) ==  True
    
    logger.log("hej", 6)
    assert logger.shouldPrint("hej", 3) ==  False

    print("Successfully determined whether to print or not!")