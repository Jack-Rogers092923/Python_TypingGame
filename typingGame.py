import time
import random

# List of sentences
sentences = [
"Although the café boasted delicious pastries, the long line discouraged me from waiting ,forcing me to find another option.",
"After the intense workout, Nadia rewarded herself with a refreshing smoothie, replenishing her energy.",
"Because the history museum was closed, we decided to explore the park instead, enjoying the beautiful spring weather.",
"Even though he felt nervous, David took a deep breath and delivered a compelling presentation, surprising everyone with his confidence.",
"As the storm raged outside, the family huddled together by the fireplace for comfort, finding solace in each other's company.",
"If I had known you were coming, I would have baked cookies, but unfortunately, I don't have any on hand.",
"Unless you water the plants regularly, they will wilt and die, so be sure to give them a good drink.",
"While the children built sandcastles on the beach, their parents relaxed under colorful umbrellas, creating a picture-perfect scene.",
"Whenever I smell freshly cut grass, I'm reminded of carefree summer days as a kid, a time of pure joy and endless possibilities.",
"Since the deadline was approaching, Sarah pulled an all-nighter to finish her project, determined to meet her goals.",
]


best = float('inf')
total_wpm = 0
attempts = 0

while True:
    # Select a random sentence from the list
    sentence = random.choice(sentences)
    
    print("=================================")
    print(sentence)
    print("=================================")
    
    # Start the timer when the user starts typing
    start = time.time()
    
    # Wait for the user to press 'Enter' to stop typing
    print("Type the sentence and press Enter to stop...")
    user = input() # This will wait for the user to press Enter after typing
    end = time.time()
    taken = end - start
    taken = round(taken) # Round the time to a whole number

    # Calculating words per minute
    words_in_sentence = len(sentence.split())
    words_typed = len(user.split())
    minutes = taken / 60
    wpm = (words_typed / minutes)
    rounded = round(wpm)
    print(f"Your typing speed is approximately : {rounded} words per minute")
    
    # Calculate accuracy
    correct = sum(1 for w1, w2 in zip(sentence.split(), user.split()) if w1 == w2)
    accuracy = (correct / words_in_sentence) * 100
    #rounded = round(accuracy)
    print(f"Accuracy: {round(accuracy)}%")
    
    if taken < best:
        best = taken
        print(f"New best time: {best} seconds")
    
    # Update total WPM and attempts
    total_wpm += wpm
    attempts += 1
    average_wpm = total_wpm / attempts
    print(f"Average WPM: {round(average_wpm)}")
    
    again = input("Play again? (YES/NO): ")
    if again.upper() != "YES":
        break

