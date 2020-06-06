get_input <- function()
{ 
  number <- readline(prompt="Enter a number: ")
  if(!grepl("^[0-9]+$",number))
  {
    return(get_input())
  }
  return(as.integer(number))
}

num <- round(runif(1) * 100, digits = 0)
guess <- -1

cat("Guess a number between 0 and 100.\n")

while(guess != num)
{ 
  guess <- get_input()
  if (guess == num)
  {
    cat(num, "found\n")
  }
  else if (guess < num)
  {
    cat("too big\n")
  }
  else if(guess > num)
  {
    cat("too small\n")
  }
}