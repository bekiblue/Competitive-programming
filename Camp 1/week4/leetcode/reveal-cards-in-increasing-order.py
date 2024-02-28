class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        answer=[i for i in range(len(deck))]
        deck_queue=deque(answer)
        deck.sort()
        revealed=0
        while deck_queue:
            answer[deck_queue.popleft()]=deck[revealed]
            revealed+=1
            if deck_queue:
                deck_queue.append(deck_queue.popleft())
        return answer
            



            