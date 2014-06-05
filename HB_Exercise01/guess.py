import random


def gen_rand_num():
    rand_num = random.randint(1, 100)
    #print rand_num #debug
    return rand_num


def main():
    prompt = "> "
    target = gen_rand_num()
    usr_name = raw_input("Please enter your name to play. \n%s" % prompt)
    print "Hi, %s. I'm thinking of a number between 1 and 100. Try to guess it!" % usr_name

    count =  0
    while True:

        if count == 5:
            print "Sorry, you're out of guesses. You lose."
            break

        else:
            guess = raw_input(prompt)

            if guess.isdigit():  #type check without using ValueError.
                count += 1
                guess = int(guess)

                if guess == target:
                    print "You guessed it. Great job! It only took you %s guesses." % count
                    break

                if guess > target:
                    message =  "Too high!"
                
                if guess < target:
                    message =  "Too low!"
                
                if count < 5:
                    message = message + " Try again. You have %d guesses left." % (5 - count)

                print message

            else:
                print "I said enter a NUMBER please."

if __name__ == "__main__":
    main()
