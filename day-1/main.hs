module Main where

-- sort list in order
quicksort :: (Ord a) => [a] -> [a]  
quicksort [] = []  
quicksort (x:xs) =
    let smaller = quicksort [a | a <- xs, a <= x]
        bigger = quicksort [a | a <- xs, a > x]
    in  smaller ++ [x] ++ bigger

next [] = Nothing
next (x:xs) = head xs

-- finds two integers in a given list that sum to a given value
sumToGivenVal :: [Int] -> Int -> [Int]
sumToGivenVal (x:xs) goal
                | (goal - x) `elem` xs = [x, goal - x]
                | otherwise = sumToGivenVal xs goal

-- finds three integers in a given list that sum to a given value
sumThreeToVal :: [Int] -> Int -> [Int]
sumThreeToVal numbers goal = [a * b * c | a <- numbers, b <- numbers, c <- numbers, a + b + c == 2020]

main :: IO ()
main = do
    expenses <- readFile "expenseReport.txt"
    let intValues = quicksort $ map (read::String -> Int) (lines expenses)
    -- only use values below 2020
    let valid = [x | x <- intValues, x < 2020]
    let finalValues = sumToGivenVal valid 2020
    print finalValues
    print $ head finalValues * finalValues!!1
    print $ head $ sumThreeToVal valid 2020