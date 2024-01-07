def eval_hand(line, face):
    """
  Evaluates a hand of cards and its bid based on the given line and face values.

  :param line: String containing a hand of cards and its bid.
  :param face: String representing face values to be used for translation.
  :return: Tuple containing the score of the hand, the hand itself, and the bid.
  """
    hand, bid = line.split()
    # Translate hand to the specified face values
    hand = hand.translate(str.maketrans('TJQKA', face))
    # Determine the best score for the hand
    best = max(calculate_hand_score(hand.replace('0', r)) for r in hand)
    return best, hand, int(bid)


def calculate_hand_score(hand):
    """
  Calculates the score of a hand.

  :param hand: String representing a hand of cards.
  :return: Sorted list of counts of each card in the hand, in descending order.
  """
    return sorted(map(hand.count, hand), reverse=True)


def main():
    """
  Main function to process the puzzle input and calculate the total score.
  """
    total_scores = []
    for face in ('ABCDE', 'A0CDE'):
        # Read the file and evaluate each line
        evaluated_hands = [eval_hand(line, face) for line in open('puzzle_input')]
        # Sort the evaluated hands by their scores
        evaluated_hands.sort()
        # Calculate the total score
        total_score = sum(rank * bid for rank, (_, _, bid) in enumerate(evaluated_hands, start=1))
        total_scores.append(total_score)

    # Print the total scores for each face value set
    for score in total_scores:
        print(score)


if __name__ == '__main__':
    main()
