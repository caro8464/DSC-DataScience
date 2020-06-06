function guess_the_number()
number = rand(0:100)
		print("Guess a number between 0 and 100.")
    while (guess = readline()) != dec(number)
        if all(isdigit, guess)
            print("too ", parse(Int, guess) < number ? "small" : "big")
        else
            print("Enter a number:")
				end
    end
    println("found")
end
 
guesswithfeedback()